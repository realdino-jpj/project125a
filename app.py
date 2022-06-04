from flask import Flask,request,jsonify
from Classifier import get_prediction

app = Flask(__name__)
@app.route("/predict-alphabet",method=["POST"])

def predict_data():
    image = request.files.get("alphabet")
    prediction = get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200

if __name__ == "__app__":
   app.run()

