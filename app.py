from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample Python second time updated manuallyupdated locally Web App running on Flask Framework!"

