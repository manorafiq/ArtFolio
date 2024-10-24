# helpers.py
from flask import jsonify, session, redirect, flash, url_for, request
from functools import wraps
from cs50 import SQL
import secrets, re
import random


db = SQL("sqlite:///footo.db")

def flash_message(message, category='default'):
    # flash(message, category=category)
    flash((message, category), category=category)

def check_required_fields(fields):
    missing_fields = [field for field, value in fields.items() if not value]

    # If fields missing then show message
    if missing_fields:
        for field in missing_fields:
            flash_message(f"{field.capitalize()} is required.", category='error')
        # return render_template(f"{current_page}.html")
        return jsonify({})

    # Give us None in return if all good
    return None


def validate_profession_name(profession_name):
    # Validate profession Name using a regular expression
    profession_name_pattern = re.compile(r'^[a-zA-Z0-9\s]+$')

    return profession_name_pattern.match(profession_name)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"error_message": "Token is missing!"}), 401
        
        try:
            user = db.execute("SELECT * FROM users WHERE id = ?", token)
            if not user:
                raise ValueError('Invalid token')
        except:
            return jsonify({ "message": "Token is invalid!"}), 401
        
        return f(user[0], *args, **kwargs)
    
    return decorated


# login required function
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get("user_id") is None:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return decorated_function

# Generating secret key for session
def generate_secret_key(length=32):
    return secrets.token_hex(length // 2)


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
