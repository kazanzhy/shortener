import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

HOST = '0.0.0.0:5000'
