import string
from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from usecases.todos.models import Todo


@dataclass(frozen=True)
class CreateTodoCommand:
    description: string


class CreateTodoHandler(Handler[CreateTodoCommand]):
    def __call__(self, request: CreateTodoCommand, *args, **kwargs):
        todo = Todo(description=request.description, )
        todo.save()
        return todo


class CreateTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[CreateTodoCommand]:
        return CreateTodoHandler()
