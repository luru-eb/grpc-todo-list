from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from features.todos.models import Todo


@dataclass(frozen=True)
class GetAllTodosQuery:
    pass


class GetAllTodosHandler(Handler[GetAllTodosQuery]):
    def __call__(self, request: GetAllTodosQuery, *args, **kwargs):
        return Todo.objects.all()


class GetAllTodosModule(Module):
    @provider
    def create_handler(self) -> Handler[GetAllTodosQuery]:
        return GetAllTodosHandler()
