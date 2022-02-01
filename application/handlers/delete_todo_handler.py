from application.commands.delete_todo_command import DeleteTodoCommand
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository
from models.models import Todo


class DeleteTodoHandler(Handler[DeleteTodoCommand]):
    def __init__(self, repository: TodosRepository):
        self._repository = repository

    def __call__(self, command: DeleteTodoCommand, *args, **kwargs):
        try:
            todo = self._repository.get_by(command.id)
            self._repository.remove(todo)
            return todo
        except Todo.DoesNotExist:
            return None
