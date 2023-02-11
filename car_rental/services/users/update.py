from ... import DB
from ...core.init_deps import bcrypt, mysql
from .find_user import find_user_by_id
from .utils.fetch_body import fetch_body


def update_customer_in_db(id, body):
    body = fetch_body(body)

    user, status = find_user_by_id(id)

    if status == 400:
        return user, status

    update_query = '''UPDATE customers SET '''
    for k, v in user.items():
        if k in body.keys():
            if body[k] is not None:
                if v == "password":
                    password = bcrypt.generate_password_hash(body[k], 8)
                    update_query += f'''{k} = {str(password)},'''
                else:
                    update_query += f'''{k} = '{str(body[k])}','''

    if update_query.endswith(','):
        update_query = update_query.rstrip(',')

    update_query += f''' WHERE id = {id}'''

    db = DB(mysql)
    db.open_connection()
    db.cursor.execute(update_query)
    res, status = db.create_commit()

    return res, status
