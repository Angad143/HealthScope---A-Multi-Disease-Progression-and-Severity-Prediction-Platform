from flask import request, redirect, url_for, flash
import jwt
from config import Config

SECRET_KEY = Config.SECRET_KEY  # Ensure SECRET_KEY is correctly imported

def activate_account(mysql):
    """Handles user account activation."""
    token = request.args.get("token")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email = payload["email"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT is_active FROM user_details WHERE email = %s", (email,))
        user = cur.fetchone()

        if user and user[0]:  # Check if already activated
            flash("Account already activated!", "info")
            return redirect(url_for("login_user"))

        cur.execute("UPDATE user_details SET is_active = True, activation_token = NULL WHERE email = %s", (email,))
        mysql.connection.commit()
        cur.close()

        flash("Account activated successfully! You can now log in.", "success")
        return redirect(url_for("login_user"))

    except jwt.ExpiredSignatureError:
        flash("Activation link expired. Please register again.", "danger")
    except jwt.InvalidTokenError:
        flash("Invalid activation link.", "danger")

    return redirect(url_for("register_user"))
