from flask import Flask, render_template, url_for

app = Flask(__name__)

app.secret_key = "abcdefg"

@app.route("/")
def home_page():
    return render_template("room.html", room_code="Under development")

@app.route("/login")
def login_page():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)