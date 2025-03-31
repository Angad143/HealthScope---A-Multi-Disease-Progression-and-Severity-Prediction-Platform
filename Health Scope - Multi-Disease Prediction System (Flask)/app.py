from flask import Flask, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config
from auth.login import login
from auth.register import register
from auth.forgot_password import forgot_password, reset_password

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register_user():
    return register(mysql, bcrypt)

@app.route("/login", methods=["GET", "POST"])
def login_user():
    return login(mysql, bcrypt)

@app.route("/dashboard")
def dashboard():
    if "logged_in" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        flash("Please log in first!", "warning")
        return redirect(url_for("login_user"))

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    session.pop("user", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
