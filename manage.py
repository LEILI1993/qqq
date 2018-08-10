from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from apps import create_app

app = create_app()

#注册数据库
manager = Manager(app)
manager.add_command('start', Server(host='127.0.0.1',port=9000,use_debugger=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()