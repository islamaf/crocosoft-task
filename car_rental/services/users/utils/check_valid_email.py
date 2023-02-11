import re


def check_valid_email(email):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return {"success": False, "message": "Invalid email."}, 400
