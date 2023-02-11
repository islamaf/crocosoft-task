from ....core.init_deps import bcrypt

def hash_password(password):
    return bcrypt.generate_password_hash(password, 8).decode('utf-8')