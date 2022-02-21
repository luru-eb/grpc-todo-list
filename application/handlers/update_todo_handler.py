from application.commands.update_todo_command import UpdateTodoCommand
from application.ports.todos_repository import TodosRepositoryInterface
from infrastructure.mediator.mediator import Handler
from models.models import Todo


class UpdateTodoHandler(Handler[UpdateTodoCommand]):
    def __init__(self, repository: TodosRepositoryInterface):
        self._repository = repository

    def __call__(self, request: UpdateTodoCommand, *args, **kwargs):
        try:
            todo = self._repository.get_by(request.id)
            todo.description = request.description
            if request.is_done:
                todo.done()
            self._repository.save(todo)
            return todo
        except Todo.DoesNotExist:
            return None

