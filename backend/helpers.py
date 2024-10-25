# helpers.py
from flask import jsonify, session, redirect, flash, url_for, request
from functools import wraps
# from cs50 import SQL
import secrets, re
import random
import os
from werkzeug.utils import secure_filename
from flask import current_app
from datetime import datetime
import uuid


# db = SQL("sqlite:///footo.db")

# Configure upload settings
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_unique_filename(filename):
    """Generate a unique filename using UUID and timestamp"""
    ext = filename.rsplit('.', 1)[1].lower()
    return f"{uuid.uuid4().hex}_{int(datetime.now().timestamp())}.{ext}"

def save_image(file):
    """
    Save an image file and return its details
    Returns: dict with file details or None if failed
    """
    try:
        if not file:
            raise ValueError("No file provided")
            
        if not allowed_file(file.filename):
            raise ValueError("File type not allowed")
            
        if file.content_length and file.content_length > MAX_FILE_SIZE:
            raise ValueError("File size exceeds maximum limit")
            
        filename = secure_filename(file.filename)
        unique_filename = get_unique_filename(filename)
        
        # Create upload directory if it doesn't exist
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
            
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(file_path)
        
        return {
            'file_name': unique_filename,
            'file_path': file_path,
            'file_size': os.path.getsize(file_path),
            'file_type': file.content_type
        }
    except Exception as e:
        current_app.logger.error(f"Error saving image: {str(e)}")
        return None

def delete_image(file_path):
    """Delete an image file from the filesystem"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
    except Exception as e:
        current_app.logger.error(f"Error deleting image: {str(e)}")
    return False

def flash_message(message, category='default'):
    # flash(message, category=category)
    flash((message, category), category=category)

def check_required_fields(fields):
    missing_fields = [field for field, value in fields.items() if not value]

    # If fields missing then show message
    if missing_fields:
        for field in missing_fields:
            # flash_message(f"{field.capitalize()} is required.", category='error')
            return jsonify({"flash_message": [f"{field.capitalize()}"]})
        
        # return render_template(f"{current_page}.html")
        # return jsonify({"flash_message": "fields are correct"})

    # Give us None in return if all good
    return None


def validate_profession_name(profession_name):
    # Validate profession Name using a regular expression
    profession_name_pattern = re.compile(r'^[a-zA-Z0-9\s]')

    return profession_name_pattern.match(profession_name)


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')

#         if not token:
#             return jsonify({"error_message": "Token is missing!"}), 401
        
#         try:
#             user = db.execute("SELECT * FROM users WHERE id = ?", token)
#             if not user:
#                 raise ValueError('Invalid token')
#         except:
#             return jsonify({ "message": "Token is invalid!"}), 401
        
#         return f(user[0], *args, **kwargs)
    
#     return decorated


# login required function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# Generating secret key for session
def generate_secret_key(length=32):
    return secrets.token_hex(length // 2)

# Getting unique data everytime without compromising the speed of the web app and minmising the loading time with this technique
def get_data_from_db(db, session, query, shown_key):
    """Fetch data from the database."""
    # Fetch all data from the database
    all_data = db.execute(query)

    # Get the list of data already shown
    shown_data = session.get(shown_key, [])

    # Find unique data that hasn't been shown
    unique_data = [item for item in all_data if item['id'] not in shown_data]

    # If all data have been shown, reset the list
    if not unique_data:
        shown_data.clear()

    # Choose a random set of data
    random.shuffle(unique_data)
    selected_data = unique_data[:6]

    # Update the list of shown data in the session
    shown_data.extend(item['id'] for item in selected_data)
    session[shown_key] = shown_data

    return selected_data
