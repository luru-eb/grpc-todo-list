from injector import Module, provider

from application.commands.update_todo_command import UpdateTodoCommand
from application.handlers.update_todo_handler import UpdateTodoHandler
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository


class UpdateTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[UpdateTodoCommand]:
        return UpdateTodoHandler(TodosRepository())
