from application.ports.todos_repository import TodosRepositoryInterface
from application.queries.getall_todos_query import GetAllTodosQuery
from infrastructure.mediator.mediator import Handler


class GetAllTodosHandler(Handler[GetAllTodosQuery]):
    def __init__(self, repository: TodosRepositoryInterface):
        self._repository = repository

    def __call__(self, command: GetAllTodosQuery, *args, **kwargs):
        return self._repository.get_all()
