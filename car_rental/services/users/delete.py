from ... import DB
from ...core.init_deps import mysql


def delete_customer_from_db(id):
    delete_query = f'''DELETE FROM customers WHERE id = {id}'''

    db = DB(mysql)
    db.open_connection()
    db.cursor.execute(delete_query)
    res, status = db.create_commit()

    return res, status
