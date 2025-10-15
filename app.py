import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'en-hemlig-kod'
jwt = JWTManager(app)

users ={
    "madde" : "password1",
    "test-user" : "password1"
}

model_filename = 'penguins_topmodel.joblib'
label_filename = 'penguins_label_encoder.joblib'
scaler_filename = 'penguins_scalers.joblib'

try:
    loaded_model = joblib.load(model_filename)
    print("Modellen är laddad!")
except FileNotFoundError:
    print("Error, modellen inte laddad")

label_encoder = joblib.load(label_filename)
scaler = joblib.load(scaler_filename)

new_penguin = np.array([[51, 230, 5500], [45, 190, 3900], [40, 180, 2900]])
scaled_penguin = scaler.transform(new_penguin)
predict = loaded_model.predict(scaled_penguin)
predicted_species = label_encoder.inverse_transform(predict)

print(predicted_species)

#Ovanför testar jag för att se att modellen funkar


#bill_length_mm, flipper_length_mm, body_mass_g | Det jag ska skicka in

@app.route('/penguins/login', methods = ['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password") #användarnamn och lösenord hämtas

    if username in users: #kontrollerar användarnamnet
        if users[username] == password: #kontrollerar att lösenordet matchar vår användare
            access_token = create_access_token(identity = username)
            return jsonify(access_token = access_token) #skapar vår token om användarnamn och lösenord stämde
        else:
            return jsonify({'Error:': 'fel lösenord'}), 400 #felhantering, får meddelande och 400 om det är fel lösenord
    else:
        return jsonify({'Error:': 'fel användarnamn'}), 400 #felhantering, får meddelande och 400 om det är fel användarnamn
    



@app.route('/penguins', methods = ["POST"])
@jwt_required()
def predict_species():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'Error:': 'Ingen data mottagen'}), 400 #felhantering, skickar meddelande och 400 om det inte finns någon data 
    

        features = ['bill_length_mm', 'flipper_length_mm', 'body_mass_g']
        values = [[data[feature] for feature in features]] #görs en lista med funktioner och sen fylls den med json värderna

        df = pd.DataFrame(values, columns = features) #skapar en padas dataframe
        scaled = scaler.transform(df) #skalar datan så det blir till det som förväntas
        prediction = loaded_model.predict(scaled) #här görs förutsägelsen
        predicted = label_encoder.inverse_transform(prediction)[0] #gör den till en art

        return jsonify({
            "Inskickade värden": data,
            "Art": predicted
        }) #skickas tillbaka som en json objekt
    
    except KeyError as e:
        return jsonify({'Error': f'Saknar värde i JSON: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 #felhantering, först om det saknas ett värde så står det vart. eller andra typer av fel
    




if __name__ == '__main__':
    app.run(debug = True)