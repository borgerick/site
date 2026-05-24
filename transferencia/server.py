import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/iphone-para-iphone")
def iphone_iphone():
    return render_template("iphone_iphone.html")

@app.route("/android-para-iphone")
def android_iphone():
    return render_template("android_iphone.html")

@app.route("/conheca-a-poc")
def conheca_poc():
    return render_template("poc.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)