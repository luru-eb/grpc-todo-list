from injector import Module, provider

from application.commands.delete_todo_command import DeleteTodoCommand
from application.handlers.delete_todo_handler import DeleteTodoHandler
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository


class DeleteTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[DeleteTodoCommand]:
        return DeleteTodoHandler(TodosRepository())