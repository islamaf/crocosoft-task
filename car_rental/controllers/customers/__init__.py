from flask import Blueprint
from .create import add_customer
from .get_customer import get_customer
from .update import update_customer
from .delete import delete_customer

customers = Blueprint("customers", __name__, url_prefix="/customers")
customers.add_url_rule("/add", view_func=add_customer, methods=['POST'])
customers.add_url_rule("/<int:id>", view_func=get_customer, methods=["GET"])
customers.add_url_rule(
    "/update/<int:id>", view_func=update_customer, methods=["PATCH"])
customers.add_url_rule(
    "/delete/<int:id>", view_func=delete_customer, methods=["DELETE"])
