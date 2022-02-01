from application.queries.getall_todos_query import GetAllTodosQuery
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository
from models.models import Todo


class GetAllTodosHandler(Handler[GetAllTodosQuery]):
    def __init__(self, repository: TodosRepository):
        self._repository = repository

    def __call__(self, command: GetAllTodosQuery, *args, **kwargs):
        return self._repository.get_all()
