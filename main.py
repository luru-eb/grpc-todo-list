import logging
import os

import django
from injector import Injector

from api.todos_server import TodosServer
from foundation.mediator.mediator import Mediator

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    django.setup()
    from django.core.management import call_command

    call_command('migrate', 'models')
    logging.basicConfig(level=logging.DEBUG)
    logging.log(logging.INFO, 'Starting todos application...')

    from modules.create_todo_module import CreateTodoModule
    from modules.getall_todos_module import GetAllTodosModule
    from modules.update_todo_module import UpdateTodoModule
    from modules.delete_todo_module import DeleteTodoModule

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
