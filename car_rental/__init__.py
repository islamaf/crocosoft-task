from flask import Flask, jsonify

from .core.config import config
from .models import DB
from .controllers.customers import customers
from .core.init_deps import bcrypt, mysql


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config[env])
    mysql.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(customers)

    db = DB(mysql)
    with app.app_context():
        db.init_db()

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "message": 'Bad request sent to server.'
        }), 400

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            "success": False,
            "message": 'Page not found.'
        }), 404

    @app.errorhandler(405)
    def unallowed_method(error):
        return jsonify({
            "success": False,
            "message": 'Method Not Allowed,'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "message": 'Unprocessable method.'
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": 'Internal Server Error.'
        }), 500

    app.app_context().push()

    return app
