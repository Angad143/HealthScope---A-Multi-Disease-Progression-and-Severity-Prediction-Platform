from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
import jwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from config import Config
import re  # Import regex module for password validation

# Ensure SECRET_KEY is correctly imported
SECRET_KEY = Config.SECRET_KEY  

# Function for generating activation token
def generate_activation_token(email):
    """Generate a secure activation token."""
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=24),  # Token valid for 24 hours
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Function for sending activation email
def send_activation_email(email, token):
    """Send activation email to the user."""
    activation_link = f"http://127.0.0.1:5000/activate_account?token={token}"

    sender_email = Config.EMAIL_USER
    sender_password = Config.EMAIL_PASS
    subject = "Activate Your Account"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    body = f"""
    Hello User,👋  

    Welcome to **HealthScope - A Multi-Disease Progression and Severity Prediction Platform**! 🚀  

    You're just one step away from unlocking personalized health insights. To activate your account, click the link below:  

    🔗 [Activate My Account]({activation_link})  

    This link will expire in **24 hours**, so make sure to activate your account soon!  

    If you didn't sign up for HealthScope, you can safely ignore this email.  

    Stay ahead in your health journey! 🌱  

    Best,  
    The HealthScope Team  

    """
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# For registration page 
def is_valid_password(password):
    """Checks if the password meets the required complexity."""
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        return "Password must contain at least one special character (!@#$%^&* etc.)."
    return None  # No issues with the password

def register(mysql, bcrypt):
    """Handles user registration."""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        conform_password = request.form["conform_password"]

        # Check password strength
        password_error = is_valid_password(password)
        if password_error:
            flash(password_error, "danger")
            return redirect(url_for("register_user"))

        if password != conform_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register_user"))

        cur = mysql.connection.cursor()
        cur.execute("SELECT email FROM user_details WHERE email=%s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            flash("Email already registered!", "warning")
            return redirect(url_for("register_user"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        activation_token = generate_activation_token(email)

        # Store user with `is_active = False`
        cur.execute(
            "INSERT INTO user_details (name, email, password, is_active, activation_token) VALUES (%s, %s, %s, %s, %s)",
            (name, email, hashed_password, False, activation_token),
        )
        mysql.connection.commit()
        cur.close()

        # Send Activation Email
        send_activation_email(email, activation_token)

        flash("Registration successful! Check your email to activate your account.", "success")
        return redirect(url_for("login_user"))

    return render_template("register.html")
