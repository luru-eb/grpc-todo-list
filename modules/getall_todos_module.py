from injector import Module, provider

from application.ports.todos_repository import TodosRepositoryInterface
from application.queries.getall_todos_query import GetAllTodosQuery
from application.handlers.getall_todos_handler import GetAllTodosHandler
from infrastructure.mediator.mediator import Handler
from infrastructure.repositories.todos_repository import TodosRepository


class GetAllTodosModule(Module):
    @provider
    def repository(self) -> TodosRepositoryInterface:
        return TodosRepository()

    @provider
    def create_handler(self, repository: TodosRepositoryInterface) -> Handler[GetAllTodosQuery]:
        return GetAllTodosHandler(repository=repository)
