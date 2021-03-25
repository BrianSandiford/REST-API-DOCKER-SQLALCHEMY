from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from example.app import app
from example.models import db
<<<<<<< HEAD
=======
#from flask.cli import FlaskGroup
>>>>>>> pytest
import ptvsd
try:
 ptvsd.enable_attach(address=('0.0.0.0', 5678))
except:
 print('still not working')


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
<<<<<<< HEAD


if __name__ == '__main__':
   manager.run()
=======
#cli = FlaskGroup(app)

if __name__ == '__main__':
   manager.run()
#    cli()  
>>>>>>> pytest
