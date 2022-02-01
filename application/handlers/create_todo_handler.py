from application.commands.create_todo_command import CreateTodoCommand
from foundation.mediator.mediator import Handler
from foundation.repositories.todos_repository import TodosRepository
from models.models import Todo


class CreateTodoHandler(Handler[CreateTodoCommand]):
    def __init__(self, repository: TodosRepository):
        self._repository = repository

    def __call__(self, command: CreateTodoCommand, *args, **kwargs):
        todo = Todo(description=command.description,)
        self._repository.save(todo)
        return todo
