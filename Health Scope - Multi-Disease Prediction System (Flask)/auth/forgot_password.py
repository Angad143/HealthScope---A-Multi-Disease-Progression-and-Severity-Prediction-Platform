from flask import render_template, request, redirect, url_for, flash
import secrets
import smtplib

# Simulated email sending function (Replace with actual email service)
def send_email(to_email, reset_link):
    sender_email = "your-email@example.com"
    sender_password = "your-email-password"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        subject = "Password Reset Request"
        message = f"Click the link below to reset your password:\n\n{reset_link}"
        email_content = f"Subject: {subject}\n\n{message}"

        server.sendmail(sender_email, to_email, email_content)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

# Forgot Password Route
def forgot_password(mysql):
    if request.method == "POST":
        email = request.form["email"]

        # Check if the email exists in the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT email FROM user_details WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user:
            # Generate reset token
            reset_token = secrets.token_urlsafe(16)

            # Store token in the database
            cur = mysql.connection.cursor()
            cur.execute("UPDATE user_details SET reset_token = %s WHERE email = %s", (reset_token, email))
            mysql.connection.commit()
            cur.close()

            # Generate reset link
            reset_link = url_for("reset_password_user", token=reset_token, _external=True)

            # Send email with the reset link
            send_email(email, reset_link)

            flash("Password reset link has been sent to your email!", "info")
        else:
            flash("Email not found!", "danger")

    return render_template("forgot_password.html")

# Reset Password Route
def reset_password(mysql, bcrypt, token):
    if request.method == "POST":
        new_password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(new_password).decode("utf-8")

        # Find the user by token
        cur = mysql.connection.cursor()
        cur.execute("SELECT email FROM user_details WHERE reset_token = %s", (token,))
        user = cur.fetchone()

        if user:
            email = user[0]
            cur.execute("UPDATE user_details SET password = %s, reset_token = NULL WHERE email = %s", (hashed_password, email))
            mysql.connection.commit()
            flash("Password updated successfully!", "success")
            return redirect(url_for("login_user"))
        else:
            flash("Invalid or expired reset link!", "danger")

        cur.close()

    return render_template("reset_password.html")
