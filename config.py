import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'w+qNN8anvqWMQkc'
SQLALCHEMY_DATABASE_URI = "postgresql://localhost/Twindred"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
