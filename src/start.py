from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from example.app import app
from example.models import db
import ptvsd
try:
 ptvsd.enable_attach(address=('0.0.0.0', 5678))
except:
 print('still not working')


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
   manager.run()

if __name__ == '__main__':
   manager.run()
