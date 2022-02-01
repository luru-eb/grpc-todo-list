from injector import Module, provider

from application.commands.create_todo_command import CreateTodoCommand
from application.handlers.create_todo_handler import CreateTodoHandler
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository


class CreateTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[CreateTodoCommand]:
        return CreateTodoHandler(TodosRepository())
