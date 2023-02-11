from ... import DB
from ...core.init_deps import mysql


def find_user_by_id(id):
    db = DB(mysql)
    db.open_connection()
    db.cursor.execute(f"SELECT * FROM customers WHERE id = {id}")

    try:
        user = db.cursor.fetchone()

        fields = ['id', 'name', 'email', 'password', 'phone',
                  'date_of_birth', 'address', 'driving_license_number', 'created_at', 'updated_at', 'deleted_at']
        user_json = {}
        for i in range(len(user)):
            user_json[fields[i]] = user[i]

        return user_json, 200
    except Exception as e:
        print(e)
        return e, 400
    finally:
        db.cursor.close()
