from flask import render_template, request, redirect, url_for, flash
import jwt
from datetime import datetime, timedelta
from config import Config
import re

# Ensure your config has a secret key
SECRET_KEY = Config.SECRET_KEY  

def generate_reset_token(email):
    """Generate a secure reset token for the user."""
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(minutes=15),  # Token expires in 15 minutes
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def forgot_password(mysql):
    """Handles the forgot password request."""
    if request.method == "POST":
        email = request.form.get("email")

        # Check if email exists in database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user_details WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            reset_token = generate_reset_token(email)

            # Store token in database
            cur = mysql.connection.cursor()
            cur.execute("UPDATE user_details SET reset_token = %s WHERE email = %s", (reset_token, email))
            mysql.connection.commit()
            cur.close()

            flash("Password reset link generated! Copy and paste the URL below:", "info")
            flash(f"http://127.0.0.1:5000/reset_password?token={reset_token}", "success")
        else:
            flash("Email not found!", "danger")

        return redirect(url_for("forgot_password_user"))

    return render_template("forgot_password.html")

def verify_reset_token(token):
    """Verify and decode reset token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["email"]
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

def is_valid_password(password):
    """Validate password complexity."""
    if (len(password) < 8 or
        not re.search(r"[A-Z]", password) or  # At least one uppercase
        not re.search(r"[a-z]", password) or  # At least one lowercase
        not re.search(r"\d", password) or  # At least one digit
        not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):  # At least one special character
        return False
    return True

def reset_password(mysql, bcrypt):
    """Handles password reset with validation."""
    token = request.args.get("token")
    email = verify_reset_token(token)

    if not email:
        flash("Invalid or expired token!", "danger")
        return redirect(url_for("forgot_password_user"))

    if request.method == "POST":
        new_password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if passwords match
        if new_password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("reset_password_user", token=token))

        # Validate password strength
        if not is_valid_password(new_password):
            flash("Password must be at least 8 characters long, include an uppercase letter, lowercase letter, a number, and a special character.", "warning")
            return redirect(url_for("reset_password_user", token=token))

        # Hash and store the new password
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")

        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_details SET password = %s, reset_token = NULL WHERE email = %s",
                    (hashed_password, email))
        mysql.connection.commit()
        cur.close()

        flash("Password updated successfully! Please log in.", "success")
        return redirect(url_for("login_user"))

    return render_template("reset_password.html", token=token)
