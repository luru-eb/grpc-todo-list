import string
from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from models.models import Todo


@dataclass(frozen=True)
class UpdateTodoCommand:
    id: int
    description: string
    is_done: bool


class UpdateTodoHandler(Handler[UpdateTodoCommand]):
    def __call__(self, command: UpdateTodoCommand, *args, **kwargs):
        try:
            todo = Todo.objects.get(pk=command.id)
            todo.description = command.description
            if command.is_done:
                todo.done()
            todo.save()
            return todo
        except Todo.DoesNotExist:
            return None


class UpdateTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[UpdateTodoCommand]:
        return UpdateTodoHandler()
