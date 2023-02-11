from flask import current_app
from .customers import customers
from .employees import employees
from .vehicles import vehicles
from .bookings import bookings
from .invoices import invoices


class DB:
    mysql = None
    cursor = None
    tables = [customers(), employees(), vehicles(), bookings(), invoices()]

    def __init__(self, mysql):
        self.mysql = mysql

    def open_connection(self):
        cursor = self.mysql.connection.cursor()
        self.cursor = cursor

    def on_success(self, message):
        return {
            "success": True,
            "message": message
        }, 200

    def on_failure(self, message):
        return {
            "success": False,
            "message": message
        }, 400

    def create_tables(self):
        self.open_connection()

        for table in self.tables:
            self.cursor.execute(table)

        try:
            self.mysql.connection.commit()

            return self.on_success("Database tables created!")
        except Exception as e:
            return self.on_failure(e)
        finally:
            self.cursor.close()

    def create_commit(self):
        self.open_connection()

        try:
            self.mysql.connection.commit()

            return self.on_success("Commit successful!")
        except Exception as e:
            return self.on_failure(e)
        finally:
            self.cursor.close()

    def init_db(self):
        self.create_tables()
