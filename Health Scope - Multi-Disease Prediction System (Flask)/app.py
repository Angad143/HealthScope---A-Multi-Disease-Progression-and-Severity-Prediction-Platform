from flask import Flask, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config
from auth.login import login
from auth.register import register
from auth.forgot_password import forgot_password, reset_password
from auth.activate_account import activate_account
from functools import wraps


# Create a Flask web application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL and Bcrypt (to be used in the Flask app)
mysql = MySQL(app)
bcrypt = Bcrypt(app)

# # Login required decorator
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'username' not in session:
#             flash('Please log in to access this page.', 'warning')
#             return redirect(url_for('dashboard'))
#         return f(*args, **kwargs)
#     return decorated_function

# Main index route
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Set up routes and views for login
@app.route("/login", methods=["GET", "POST"])
def login_user():
    return login(mysql, bcrypt)

# Set up routes and views for registration
@app.route("/register", methods=["GET", "POST"])
def register_user():
    return register(mysql, bcrypt)

# Set up routes and views for account activation
@app.route("/activate_account")
def activate_account_route():
    return activate_account(mysql)

# Set up routes and views for forgot password and reset password
@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password_user():
    return forgot_password(mysql)

@app.route("/reset_password", methods=["GET", "POST"])
def reset_password_user():
    return reset_password(mysql, bcrypt)

# Set up routes and views for about and help pages
@app.route("/help")
def help_questions():
    return render_template("help.html")

# Set up dashboard route (requires user to be logged in)
@app.route("/dashboard")
def dashboard():
    if session.get("logged_in"):  # ✅ Use .get() to avoid KeyError
        return render_template("dashboard.html", user=session["user_name"])
    else:
        flash("Please log in first!", "warning")
        return redirect(url_for("login_user"))
# Dashboard Routes
# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', username=session.get('username'))

# Details about different disease route
@app.route("/disease_details")
def disease_details():
    if session.get("logged_in"):  # ✅ Use .get() to avoid KeyError
        return render_template("disease_details.html", user=session["user_name"])
    else:
        flash("Please log in first!", "warning")
        return redirect(url_for("login_user"))

# Set up logout route (clears session data and flashes a message)
@app.route("/logout")
def logout():
    session.clear()  # Clears all session data, including flash messages
    # flash("You have been logged out!", "info")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
