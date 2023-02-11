import re
from ... import DB
from ...core.init_deps import bcrypt, mysql
from .utils.fetch_body import fetch_body
from .utils.check_valid_email import check_valid_email
from .utils.hash_password import hash_password

def add_customer_to_db(body):
    body = fetch_body(body)

    db = DB(mysql)
    db.open_connection()

    check_valid_email(body['email'])
    db.cursor.execute(f"SELECT * FROM customers WHERE email = '{body['email']}'")
    existing_user = db.cursor.fetchone()
    if existing_user:
        return {"success": False, "message": "User by this email already exists."}, 400

    password = hash_password(body['password'])

    db.cursor.execute(
        f'''
            INSERT INTO customers (name, email, password, phone, date_of_birth, address, driving_license_number) 
            VALUES ('{body['name']}', '{body['email']}', '{password}', '{body['phone']}', '{body['date_of_birth']}', '{body['address']}', '{body['driving_license_number']}')
        ''')

    res, status = db.create_commit()

    return res, status
