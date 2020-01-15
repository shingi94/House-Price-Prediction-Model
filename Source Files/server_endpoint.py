from flask import Flask
from waitress import serve
from flask import request
import json

app = Flask(__name__)

@app.route("/predict_price", methods=['POST'])
def predict_house():
    json = request.get_json()
    # expect X in format [[1, 2, 4, 5]]
    X = json["X"]
    model = joblib.load("model.pkl")
    return str(model.predict(X))
	
# This is important so that the server will run when the docker container has been started. 
# Host=0.0.0.0 needs to be provided to make the server publicly available.
if __name__ == "__main__":
    serve(app,host='0.0.0.0', port=5000)