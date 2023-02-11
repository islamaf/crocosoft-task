import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    MYSQL_HOST = 'db'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'crocosoft'
    OPTIONS = {
        'auth_plugin': 'mysql_native_password'
    }


config = {
    "dev": DevelopmentConfig
}

key = Config.SECRET_KEY
