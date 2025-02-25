from flask import Flask, request, jsonify

app = Flask(__name__)

def suggest_remedy(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms:
        if "skin nodules" in symptoms:
            return "Lumpy Skin Disease: Isolate animal, apply antiseptic, administer antibiotics, and vaccinate healthy animals."
        elif "mouth ulcers" in symptoms or "drooling" in symptoms:
            return "Foot-and-Mouth Disease: Isolate infected animal, provide soft food, apply saline solution, and report severe cases."
        elif "swollen udder" in symptoms or "pus in milk" in symptoms:
            return "Mastitis: Milk out infected udder, apply warm compresses, use prescribed antibiotics, and maintain udder hygiene."
        elif "persistent coughing" in symptoms or "weight loss" in symptoms:
            return "Bovine Tuberculosis: Isolate & test animal, avoid consuming meat/milk, and report to a vet immediately."
        else:
            return "General Fever: Provide clean water, balanced diet, and consult a vet if persists."
    elif "sudden death" in symptoms and "blood oozing" in symptoms:
        return "Anthrax: Do NOT open carcass, report immediately, and burn & bury carcass safely."
    elif "no symptoms" in symptoms:
        return "Preventive Care: Follow vaccination schedules, provide proper nutrition, ensure biosecurity measures, and maintain hygiene."
    else:
        return "No matching remedy found. Consult a vet."

@app.route('/get_remedy', methods=['GET'])
def get_remedy():
    symptoms = request.args.get('symptoms', '')
    remedy = suggest_remedy(symptoms)
    return jsonify({"remedy": remedy})

if __name__ == "__main__":
    app.run(debug=True)
