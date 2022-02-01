from injector import Module, provider

from application.queries.getall_todos_query import GetAllTodosQuery
from application.handlers.getall_todos_handler import GetAllTodosHandler
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository


class GetAllTodosModule(Module):
    @provider
    def create_handler(self) -> Handler[GetAllTodosQuery]:
        return GetAllTodosHandler(TodosRepository())
