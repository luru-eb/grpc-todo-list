import string
from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from features.todos.models import Todo


@dataclass(frozen=True)
class CreateTodoCommand:
    description: string


class CreateTodoHandler(Handler[CreateTodoCommand]):
    def __call__(self, command: CreateTodoCommand, *args, **kwargs):
        todo = Todo(description=command.description, )
        todo.save()
        return todo


class CreateTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[CreateTodoCommand]:
        return CreateTodoHandler()
