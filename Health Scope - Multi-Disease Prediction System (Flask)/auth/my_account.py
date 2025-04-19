from flask import render_template, session, redirect, url_for, flash, request
from flask_mysqldb import MySQL

def my_account(mysql):
    """Display user account information and handle account deletion"""
    # Check if user is logged in
    if not session.get('logged_in'):
        flash('Please login to access your account', 'warning')
        return redirect(url_for('login_user'))

    # Handle account deletion
    if request.method == 'POST' and 'delete_account' in request.form:
        return delete_account(mysql)

    # Fetch user data from database
    cur = mysql.connection.cursor()
    try:
        cur.execute(
            "SELECT name, email, is_active FROM user_details WHERE id = %s",
            (session['user_id'],)
        )
        user = cur.fetchone()

        if not user:
            flash("User account not found", "danger")
            return redirect(url_for('login_user'))

        name, email, is_active = user

        # Determine account status display
        account_status = "Active" if is_active else "Inactive"
        status_badge = "bg-success" if is_active else "bg-secondary"

        return render_template(
            'my_account.html',
            name=name,
            email=email,
            account_status=account_status,
            status_badge=status_badge
        )

    except Exception as e:
        flash(f"Database error: {str(e)}", "danger")
        return redirect(url_for('dashboard'))
    finally:
        cur.close()

def delete_account(mysql):
    """Handle account deletion"""
    try:
        cur = mysql.connection.cursor()
        cur.execute(
            "DELETE FROM user_details WHERE id = %s",
            (session['user_id'],)
        )
        mysql.connection.commit()
        
        # Clear all session data
        session.clear()
        
        # Return success message and redirect URL
        return {
            'success': True,
            'message': 'Account successfully deleted',
            'redirect': url_for('home')
        }

    except Exception as e:
        mysql.connection.rollback()
        return {
            'success': False,
            'message': f'Delete failed: {str(e)}'
        }
    finally:
        cur.close()