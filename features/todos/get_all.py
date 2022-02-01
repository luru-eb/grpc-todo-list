from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from models.models import Todo


@dataclass(frozen=True)
class GetAllTodosQuery:
    pass


class GetAllTodosHandler(Handler[GetAllTodosQuery]):
    def __call__(self, command: GetAllTodosQuery, *args, **kwargs):
        return Todo.objects.all()


class GetAllTodosModule(Module):
    @provider
    def create_handler(self) -> Handler[GetAllTodosQuery]:
        return GetAllTodosHandler()
