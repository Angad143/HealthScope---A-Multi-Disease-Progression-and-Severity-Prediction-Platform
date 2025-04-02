from flask import render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

# login function 
def login(mysql, bcrypt):
    """Handles user login."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, name, password, is_active FROM user_details WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            user_id, name, hashed_password, is_active = user

            if not is_active:
                flash("Please activate your account first!", "warning")
                return redirect(url_for("login_user"))

            if bcrypt.check_password_hash(hashed_password, password):
                # ✅ Set session variables after successful login
                session["logged_in"] = True
                session["user_id"] = user_id
                session["user_name"] = name
                flash("Login successful!", "success")
                return redirect(url_for("dashboard"))

        flash("Invalid email or password!", "danger")

    return render_template("login.html")
