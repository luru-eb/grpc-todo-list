from application.commands.delete_todo_command import DeleteTodoCommand
from application.ports.todos_repository import TodosRepositoryInterface
from infrastructure.mediator.mediator import Handler
from models.models import Todo


class DeleteTodoHandler(Handler[DeleteTodoCommand]):
    def __init__(self, repository: TodosRepositoryInterface):
        self._repository = repository

    def __call__(self, request: DeleteTodoCommand, *args, **kwargs):
        try:
            todo = self._repository.get_by(request.id)
            self._repository.remove(todo)
            return todo
        except Todo.DoesNotExist:
            return None