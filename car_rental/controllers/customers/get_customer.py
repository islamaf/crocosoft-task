from flask import request, jsonify
from ...services.users.find_user import find_user_by_id


def get_customer(id):
    res, status = find_user_by_id(id)
    return jsonify(res), status
