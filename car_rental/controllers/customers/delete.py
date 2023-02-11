from flask import request, jsonify
from ...services.users.delete import delete_customer_from_db


def delete_customer(id):
    res, status = delete_customer_from_db(id)
    return jsonify(res), status
