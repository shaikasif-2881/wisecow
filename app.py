from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # Redirect to another route inside the app
    return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    return "Welcome to Wisecow App!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)  # Must use 0.0.0.0 for Kubernetes

