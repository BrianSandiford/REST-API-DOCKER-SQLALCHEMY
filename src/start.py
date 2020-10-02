from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from example.app import app
from example.models import db
#app.run(host= "0.0.0.0")

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
