import logging
import os

import django
from injector import Injector

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    django.setup()
    from django.core.management import call_command

    call_command('migrate', 'todos')
    logging.basicConfig(level=logging.DEBUG)
    logging.log(logging.INFO, 'Starting todos application...')

    from features.todos.todos_server import TodosServer
    from foundations.mediator.mediator import Mediator
    from features.todos.create.create import CreateTodoModule
    from features.todos.delete.delete import DeleteTodoModule
    from features.todos.getall.get_all import GetAllTodosModule
    from features.todos.update.update import UpdateTodoModule

    container = Injector([
        CreateTodoModule(),
        GetAllTodosModule(),
        UpdateTodoModule(),
        DeleteTodoModule()
    ], auto_bind=False)
    mediator = Mediator(container)
    server = TodosServer(mediator, os.getenv('APP_PORT', '50051'))
    server.start()
    server.wait()
