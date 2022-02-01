import logging
import os

import django
from injector import Injector

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    django.setup()
    from django.core.management import call_command

    call_command('migrate', 'models')
    logging.basicConfig(level=logging.DEBUG)
    logging.log(logging.INFO, 'Starting todos application...')

    from todos_server import TodosServer
    from foundations.mediator.mediator import Mediator
    from features.todos.create import CreateTodoModule
    from features.todos.delete import DeleteTodoModule
    from features.todos.get_all import GetAllTodosModule
    from features.todos.update import UpdateTodoModule

    container = Injector([
        CreateTodoModule(),
        GetAllTodosModule(),
        UpdateTodoModule(),
        DeleteTodoModule()
    ], auto_bind=False)
    mediator = Mediator(container)
    server = TodosServer(mediator, 50051)
    server.start()
    server.wait()
