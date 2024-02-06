from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.secret_key = "abcdefg"

@app.route("/")
def home_page():
    return render_template("login.html")

@app.route("/room", methods=["POST","GET"])
def login_page():
    return render_template("room.html")

if __name__ == "__main__":
    app.run(debug=True)