from flask import Flask, request, jsonify
# from helpers import check_required_fields, validate_profession_name
from cs50 import SQL
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask("__name__")

db = SQL("sqlite:///footo.db")
CORS(app) # Enable CORS for all routes

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.json

        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")
        profession = data.get("profession")

        # full_name = request.form.get("full_name")
        # email = request.form.get("email")
        # password = request.form.get("password")
        # profession = request.form.get("profession")

        # result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "Profession": profession})

        # if result:
        #     return jsonify(result), 400
        
        # if not validate_profession_name(profession):
        #     return jsonify({"error": "Invalid profession name"}), 400
        
        email_exists = db.execute("SELECT * FROM users WHERE email = ?", email)

        if email_exists:
            return jsonify({"error": "Email already exists"}), 400
        
        # hash_password = generate_password_hash(password)
        
        db.execute("INSERT INTO users (full_name, email, password_hash, profession) VALUES(?, ?, ?, ?)", full_name, email, password, profession)

        return jsonify({"message": "Signup successfully"}), 201
    
    # If GET requests return error
    return jsonify({"error": "Invalid request"}), 400


@app.route("/login", methods=["GET", "POST"])
def login():
    
    # Handle POST request for user login
    if request.method == "POST":
        data = request.json
        email = data.get("email")
        password = data.get("password")

        # email = request.form.get("email")
        # password = request.form.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        
        user = db.execute("SELECT * FROM users WHERE email = ?", email)

        # if not user or not check_password_hash(user[0]["password"], password):
        pas = password == user[0]["password_hash"]
        if not user or not pas:
            return jsonify({"error": "Invalid email or password"}), 401
        
        return jsonify({"message": "Login successful", "user_id": user[0]["id"]}), 200
    
    # Get request send error message
    return jsonify({"error": "Invalid request"}), 400


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

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from werkzeug.security import check_password_hash, generate_password_hash
# from cs50 import SQL
# from helpers import validate_profession_name, check_required_fields, get_data_from_db, token_required, generate_secret_key
# #generate_secret_key,
# from werkzeug.utils import secure_filename
# import os

# UPLOAD_FOLDER = 'uplaods'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# app = Flask(__name__) *****
# CORS(app) # Enable CORS for all routes

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['SECRET_KEY'] = generate_secret_key(64)
# db = SQL("sqlite:///footo.db") *****

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# /***************
# @app.route("/api/upload", methods=["POST"])
# @token_required
# def upload_image():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400
#     if not allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return jsonify({"message": "File uploaded successfully", 'filename': filename}), 200
#     return jsonify({"error": "File type not allowed"}), 400


# @app.route("/signup", methods=["GET", "POST"])
# # @token_required
# def singup():
#     if request.method == "POST":
#         data = request.json
#         full_name = data.get("full_name")
#         email = data.get("email")
#         password = data.get("password")
#         profession = data.get("profession")

#         result = check_required_fields({"Full Name": full_name, "Email": email, "Paswwrod": password, "Profession": profession})

#         if result: 
#             return jsonify(result), 400
        
#         if not validate_profession_name(profession):
#             return jsonify({"error": "Invalid profession name"}), 400
        
#         email_exists = db.execute("SELECT * FROM users WHERE email = ?", email)
#         if email_exists:
#             return jsonify({"error": "Email already exists"}), 400
        
#         hash_password = generate_password_hash(password)
#         db.execute("INSERT INTO users (full_name, email, password_hash, profession) VALUES(?, ?, ?, ?)", full_name, email, hash_password, profession)

#         return jsonify({"message": "Singup successfully"}), 201
#     return jsonify({"error": "Invalid request"}), 400


# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     email = data.get("email")
#     password = data.get("password")

#     if not email or not password:
#         return jsonify({"error": "Email and password are required"}), 400
    
#     user = db.execute("SELECT * FROM users WHERE email = ?", email)

#     if not user or not check_password_hash(user[0]["password"], password):
#         return jsonify({"error": "Invalid email or password"}), 401
    
#     return jsonify({"message": "Login successful", "user_id": user[0]["id"]}), 200


# @app.route("/api/porjects", methods=["GET"])
# @token_required
# def projects():
#     user_projects = get_data_from_db(db, None, "SELECT * FROM projects", "shown_projects")
#     return jsonify(user_projects)
# *****/
# # Import necessary modules
# import os
# import requests
# from flask import Flask, request, redirect, url_for, render_template, session, jsonify
# import json
# # from flask_session import Session
# from cs50 import SQL
# from werkzeug.security import check_password_hash, generate_password_hash
# from helpers import flash_message, login_required, generate_secret_key, validate_profession_name, check_required_fields, get_data_from_db

# # Create a Flask web application instance
# app = Flask(__name__)

# # Configure session settings
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# app.secret_key = generate_secret_key(64)
# Session(app)

# # Connect to the SQLite database here
# db = SQL("sqlite:///footo.db")

# @app.route("/", methods=['GET', 'POST'])
# # @login_required
# def index():
#     # Retrieve assignments for the logged-in student
#     # assignment = db.execute("SELECT * FROM assignment WHERE student_id = ?", session["user_id"])
#     # Render the homepage template with assignment data
#     return jsonify([{"Default:": "home route"}])

# # Define route for user signup
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     # Clear any existing session data
#     # session.clear()

#     # Handle POST request for user signup
#     if request.method == "POST":
#         # Extract user input from the form
#         full_name = request.form.get("full_name")
#         email = request.form.get("email")
#         password = request.form.get("password")
#         profession = request.form.get("profession")

#         # Check if all required fields are provided
#         result = check_required_fields({"Full Name": full_name, "Email": email, "Password": password, "profession": profession}, current_page="signup")
#         if result:
#             return result

#         # Validate the format of the profession name
#         if not validate_profession_name(profession):
#             return {"validate_proffesion_name": "Profession Name must adhere to the specified convention. i.e(designer, Artist or Engineer)", "category": 'info'}

#         # Check if the provided email already exists in the database
#         email_exists = db.execute("SELECT * FROM users WHERE email = ?", email)
#         if email_exists:
#             flash_message("Email is already exist. Please Login Instead.", category='info')
#             redirect("/signup")
#             return {"error": "Eamil is already exist. Please Login Instead."}

#         # Hash the password before storing it in the database
#         hash_password = generate_password_hash(password)

#         # Insert user data into the database
#         db.execute("INSERT INTO users (name, email, password, profession) VALUES (?, ?, ?, ?, ?)", full_name, email, hash_password, profession)

#         # Display a success message and redirect to the login page
#         flash_message("Signup successful!", category='success')
#         return redirect("/login")

#     # Render the signup page for GET requests
#     return url_for("/signup")

# # Define route for user login
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     # Clear any existing session data
#     # session.clear()

#     # Display a logout message if the request includes a logout parameter
#     if request.args.get('logout'):
#         flash_message("You're Logout!", category='success')

#     # Handle POST request for user login
#     if request.method == "POST":
#         # Extract user input from the form
#         email = request.form.get("email")
#         password = request.form.get("password")

#         # Check if email and password are provided
#         if not email or not password:
#             flash_message("Provide required Fields to Log In!", category='error')
#             return redirect("/login")

#         # Retrieve user data from the database based on the provided email
#         user = db.execute("SELECT * FROM users WHERE email = ?", email)

#         # Check if the user exists and the password is correct
#         if not user or not check_password_hash(user[0]["password"], password):
#             flash_message("Invalid email or password!", category='error')
#             return ("login.html")

#         # Store the user ID in the session for authentication
#         session["user_id"] = user[0]["id"]
#         # Display a success message and redirect to the homepage
#         flash_message("Log In Successful!", category='success')
#         return redirect(url_for("index"))

#     # Render the login page for GET requests
#     return render_template("login.html")

# # Define route for user logout
# @app.route("/logout")
# @login_required
# def logout():
#     # Clear the session data
#     # session.clear()
#     # Redirect to the login page with a logout parameter
#     return redirect(url_for('login', logout=True))


# @app.route('/projects', methods=['GET'])
# def projects():
#     user_projects = get_data_from_db(db, session, 'SELECT * FROM projects', 'shown_projects')
#     return jsonify(user_projects)


# # Run the Flask application in debug mode
# if __name__ == '__main__':
#     app.run(debug=True)