from flask import request, jsonify
from ...services.users.create import add_customer_to_db


def add_customer():
    body = request.get_json()

    res, status = add_customer_to_db(body)
    return jsonify(res), status
