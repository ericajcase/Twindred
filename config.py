import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'w+qNN8anvqWMQkc'

SQLALCHEMY_DATABASE_URI = "postgresql://localhost/Twindred"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

if 'RDS_HOSTNAME'  in os.environ:
    SQLALCHEMY_DATABASE_URI = "postgresql://" + os.environ['RDS_USERNAME'] + ':' + os.environ['RDS_PASSWORD'] + '@' + os.environ['RDS_HOSTNAME'] + "/" + os.environ['RDS_DB_NAME']
else:
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/Twindred"


# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
