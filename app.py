import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/penguins', methods = ["POST"])
def predict_species():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'Error:': 'Ingen data mottagen'}), 400 #felhantering, skickar meddelande och 400 om det inte finns någon data 
    

        features = ['bill_length_mm', 'flipper_length_mm', 'body_mass_g']
        values = [[data[feature] for feature in features]] #görs en lista med funktioner och sen fylls den med json värderna

        df = pd.DataFrame(values, columns = features) #skapar en padas dataframe
        scaled = scaler.transform(df) #skalar datan såd et blir till det som förväntas
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