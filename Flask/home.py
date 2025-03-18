from flask import Flask, render_template, request
import requests
import os
import loguru

API_URL = os.getenv("API_URL")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Récupérer les données du formulaire
    data = request.form.to_dict()
    # Make the API request
    response = requests.post(f"{API_URL}/predict", json=data)

    # Render the response on a new page
    return render_template("result.html", prediction=response.json())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)
