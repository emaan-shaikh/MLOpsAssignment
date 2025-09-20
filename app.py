from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Iris Classifier API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Expecting: {"features": [sepal_length, sepal_width, petal_length, petal_width]}
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
