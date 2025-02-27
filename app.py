from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to suggest a remedy and confidence level
def suggest_remedy(symptoms):
    symptoms = symptoms.lower()

    disease_data = {
        "lumpy skin disease": {
            "conditions": ["fever", "skin nodules"],
            "remedy": "Isolate animal, apply antiseptic, administer antibiotics, and vaccinate healthy animals.",
            "confidence": 90
        },
        "foot-and-mouth disease": {
            "conditions": ["fever", "mouth ulcers", "drooling"],
            "remedy": "Isolate infected animal, provide soft food, apply saline solution, and report severe cases.",
            "confidence": 85
        },
        "mastitis": {
            "conditions": ["fever", "swollen udder", "pus in milk"],
            "remedy": "Milk out infected udder, apply warm compresses, use prescribed antibiotics, and maintain udder hygiene.",
            "confidence": 88
        },
        "bovine tuberculosis": {
            "conditions": ["fever", "persistent coughing", "weight loss"],
            "remedy": "Isolate & test animal, avoid consuming meat/milk, and report to a vet immediately.",
            "confidence": 80
        },
        "anthrax": {
            "conditions": ["sudden death", "blood oozing"],
            "remedy": "Do NOT open carcass, report immediately, and burn & bury carcass safely.",
            "confidence": 95
        },
        "preventive care": {
            "conditions": ["no symptoms"],
            "remedy": "Follow vaccination schedules, provide proper nutrition, ensure biosecurity measures, and maintain hygiene.",
            "confidence": 100
        },
        "general fever": {
            "conditions": ["fever"],
            "remedy": "Provide clean water, balanced diet, and consult a vet if persists.",
            "confidence": 70
        }
    }

    for disease, data in disease_data.items():
        if all(cond in symptoms for cond in data["conditions"]):
            return {"remedy": data["remedy"], "confidence": data["confidence"]}

    return {"remedy": "No matching remedy found. Consult a vet.", "confidence": 50}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_remedy', methods=['GET'])
def get_remedy():
    symptoms = request.args.get('symptoms', '').strip()
    
    if not symptoms:
        return jsonify({"error": "No symptoms provided. Please enter symptoms."}), 400
    
    result = suggest_remedy(symptoms)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
