# helpers.py
from flask import session, redirect, flash, url_for
from functools import wraps
import secrets, re

def flash_message(message, category='info'):
    # flash(message, category=category)
    flash((message, category), category=category)

def check_required_fields(fields):
    missing_fields = [field for field, value in fields.items() if not value]
    
    # If fields missing then show message
    if missing_fields:
        for field in missing_fields:
            flash_message(f"{field.capitalize()} is required.", category='error')
        return redirect(url_for('show_flash'))
    
    # Give us None in return if all good
    return None


def validate_class_name(class_name):
    # Validate Class Name using a regular expression
    class_name_pattern = re.compile(r'^[A-Za-z0-9_\-]+$')
    
    return class_name_pattern.match(class_name)

# i want to show sign up page for those who are not at our data base as student/teacher/admin whiAch can do using login-required i guess lets see

# login required function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/signup")
        return f(*args, **kwargs)
    return decorated_function

# Generating secret key for session
def generate_secret_key(length=32):
    return secrets.token_hex(length // 2)
