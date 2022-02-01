from application.commands.update_todo_command import UpdateTodoCommand
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository
from models.models import Todo


class UpdateTodoHandler(Handler[UpdateTodoCommand]):
    def __init__(self, repository: TodosRepository):
        self._repository = repository

    def __call__(self, command: UpdateTodoCommand, *args, **kwargs):
        try:
            todo = self._repository.get_by(command.id)
            todo.description = command.description
            if command.is_done:
                todo.done()
            self._repository.save(todo)
            return todo
        except Todo.DoesNotExist:
            return None

