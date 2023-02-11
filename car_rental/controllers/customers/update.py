from flask import request, jsonify
from ...services.users.update import update_customer_in_db


def update_customer(id):
    body = request.get_json()

    res, status = update_customer_in_db(id, body)
    return jsonify(res), status
