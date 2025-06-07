from chatgpt_app import app
from flask import render_template, request
import random

@app.route("/", methods=["GET", "POST"])
def index():
    return {}
