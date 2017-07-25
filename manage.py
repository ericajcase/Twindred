import os
from flask_script  import Manager
from flask_migrate import Migrate, MigrateCommand

from application import application, db

application.config.from_object('config')

migrate = Migrate(application, db)

manager = Manager(application)

manager.add_command('db', MigrateCommand)

# allows to use as a library or script
if __name__ == '__main__':
    manager.run()
