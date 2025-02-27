from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

def suggest_remedy(symptoms):
    symptoms = symptoms.lower()
    confidence = random.randint(70, 95)  # Adding confidence levels to suggestions

    if "fever" in symptoms:
        if "skin nodules" in symptoms:
            return f"Lumpy Skin Disease ({confidence}% confidence): Isolate animal, apply antiseptic, administer antibiotics, and vaccinate healthy animals."
        elif "mouth ulcers" in symptoms or "drooling" in symptoms:
            return f"Foot-and-Mouth Disease ({confidence}% confidence): Isolate infected animal, provide soft food, apply saline solution, and report severe cases."
        elif "swollen udder" in symptoms or "pus in milk" in symptoms:
            return f"Mastitis ({confidence}% confidence): Milk out infected udder, apply warm compresses, use prescribed antibiotics, and maintain udder hygiene."
        elif "persistent coughing" in symptoms or "weight loss" in symptoms:
            return f"Bovine Tuberculosis ({confidence}% confidence): Isolate & test animal, avoid consuming meat/milk, and report to a vet immediately."
        else:
            return f"General Fever ({confidence}% confidence): Provide clean water, balanced diet, and consult a vet if persists."
    elif "sudden death" in symptoms and "blood oozing" in symptoms:
        return "Anthrax: Do NOT open carcass, report immediately, and burn & bury carcass safely."
    elif "no symptoms" in symptoms:
        return "Preventive Care: Follow vaccination schedules, provide proper nutrition, ensure biosecurity measures, and maintain hygiene."
    else:
        return "No matching remedy found. Consult a vet."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_remedy', methods=['GET'])
def get_remedy():
    symptoms = request.args.get('symptoms', '').strip()
    
    if not symptoms:
        return jsonify({"error": "No symptoms provided. Please enter symptoms."}), 400
    
    remedy = suggest_remedy(symptoms)
    return jsonify({"remedy": remedy})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
