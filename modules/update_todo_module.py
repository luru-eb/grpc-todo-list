from injector import Module, provider

from application.commands.update_todo_command import UpdateTodoCommand
from application.handlers.update_todo_handler import UpdateTodoHandler
from application.ports.todos_repository import TodosRepositoryInterface
from infrastructure.mediator.mediator import Handler
from infrastructure.repositories.todos_repository import TodosRepository


class UpdateTodoModule(Module):
    @provider
    def repository(self) -> TodosRepositoryInterface:
        return TodosRepository()

    @provider
    def create_handler(self, repository: TodosRepositoryInterface) -> Handler[UpdateTodoCommand]:
        return UpdateTodoHandler(repository=repository)
