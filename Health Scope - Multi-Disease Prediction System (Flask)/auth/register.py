from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

def register(mysql, bcrypt):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        conform_password = request.form["conform_password"]

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
        cur.execute("INSERT INTO user_details (name, email, password, conform_password) VALUES (%s, %s, %s, %s)",
                    (name, email, hashed_password, hashed_password))
        mysql.connection.commit()
        cur.close()

        flash("Registration successful! You can log in now.", "success")
        return redirect(url_for("login_user"))
    
    return render_template("register.html")
