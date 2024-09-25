# Import necessary modules
import os
import requests
# from flask import jsonify
from flask import Flask, request, redirect, url_for, render_template, session
# from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import flash_message, login_required, generate_secret_key, validate_class_name, check_required_fields, get_data_from_db, get_class_timing, get_exam_schedules

# Create a Flask web application instance
app = Flask(__name__)

# Configure session settings
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# app.secret_key = generate_secret_key(64)
# Session(app)

# Connect to the SQLite database here
db = SQL("sqlite:///footo.db")

@app.route("/", methods=['GET', 'POST'])
# @login_required
def index():
    # Retrieve assignments for the logged-in student
    # assignment = db.execute("SELECT * FROM assignment WHERE student_id = ?", session["user_id"])
    # Render the homepage template with assignment data
    return {"Default:": "home route"}

# Define route for user signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Clear any existing session data
    # session.clear()

    # Handle POST request for user signup
    if request.method == "POST":
        # Extract user input from the form
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        profession = request.form.get("profession")

        # Check if all required fields are provided
        result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "profession": profession}, current_page="signup")
        if result:
            return result

        # Validate the format of the class name
        # if not validate_class_name(class_name):
        #     flash_message("Class Name must adhere to the specified convention. i.e(CS50, CS or any acronym)", category='info')
        #     return render_template("signup.html")

        # Check if the provided email already exists in the database
        email_exists = db.execute("SELECT * FROM users WHERE email = ?", email)
        if email_exists:
            flash_message("Email is already exist. Please Login Instead.", category='info')
            redirect("/signup")
            return {"error": "Eamil is already exist. Please Login Instead."}

        # Hash the password before storing it in the database
        hash_password = generate_password_hash(password)

        # Insert user data into the database
        db.execute("INSERT INTO users (name, email, password, profession) VALUES (?, ?, ?, ?, ?)", full_name, email, hash_password, profession)

        # Display a success message and redirect to the login page
        flash_message("Signup successful!", category='success')
        return redirect("/login")

    # Render the signup page for GET requests
    return url_for("/signup")

# Define route for user login
@app.route("/login", methods=["GET", "POST"])
def login():
    # Clear any existing session data
    # session.clear()

    # Display a logout message if the request includes a logout parameter
    if request.args.get('logout'):
        flash_message("You're Logout!", category='success')

    # Handle POST request for user login
    if request.method == "POST":
        # Extract user input from the form
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if email and password are provided
        if not email or not password:
            flash_message("Provide required Fields to Log In!", category='error')
            return redirect("/login")

        # Retrieve user data from the database based on the provided email
        user = db.execute("SELECT * FROM users WHERE email = ?", email)

        # Check if the user exists and the password is correct
        if not user or not check_password_hash(user[0]["password"], password):
            flash_message("Invalid email or password!", category='error')
            return ("login.html")

        # Store the user ID in the session for authentication
        session["user_id"] = user[0]["id"]
        # Display a success message and redirect to the homepage
        flash_message("Log In Successful!", category='success')
        return redirect(url_for("index"))

    # Render the login page for GET requests
    return render_template("login.html")

# Define route for user logout
@app.route("/logout")
@login_required
def logout():
    # Clear the session data
    # session.clear()
    # Redirect to the login page with a logout parameter
    return redirect(url_for('login', logout=True))


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)