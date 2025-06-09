from chatgpt_app import app
from flask import Flask, render_template, request, jsonify
import random
import cohere
import os

cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.ClientV2(api_key=cohere_api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_medicine", methods=["POST"])
def get_medicine():
    symptom = request.json.get("symptom", "").lower()
    
    messages=[
                {"role": "system", "content": "You are a helpful medical assistant. Give only over-the-counter (OTC) medicine suggestions. Do not give prescriptions. Give short answer"},
                {"role": "user", "content": f"I have the following symptom: {symptom}. What OTC medicine should I take?"}
            ]
    res = co.chat(
    model="command-a-03-2025",
    messages=messages ,
)
    result = res.message.content[0].text
    return jsonify({"response": result})
