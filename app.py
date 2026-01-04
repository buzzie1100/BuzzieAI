from flask import Flask, render_template, request, jsonify
from services import generate_design
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")
    result = generate_design(user_prompt)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
