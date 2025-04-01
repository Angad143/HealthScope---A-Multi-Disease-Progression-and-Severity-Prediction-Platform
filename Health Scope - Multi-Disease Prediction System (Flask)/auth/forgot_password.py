from flask import render_template, request, redirect, url_for, flash
import jwt
from datetime import datetime, timedelta
from config import Config

SECRET_KEY = Config.SECRET_KEY  # Ensure your config has a secret key

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

def reset_password(mysql, bcrypt):
    """Handles password reset."""
    token = request.args.get("token")
    email = verify_reset_token(token)

    if not email:
        flash("Invalid or expired token!", "danger")
        return redirect(url_for("forgot_password_user"))

    if request.method == "POST":
        new_password = request.form.get("password")
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")

        cur = mysql.connection.cursor()
        cur.execute("UPDATE user_details SET password = %s, reset_token = NULL WHERE email = %s",
                    (hashed_password, email))
        mysql.connection.commit()
        cur.close()

        flash("Password updated successfully! Please log in.", "success")
        return redirect(url_for("login_user"))

    return render_template("reset_password.html", token=token)
