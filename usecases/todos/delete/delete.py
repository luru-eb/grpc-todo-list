from dataclasses import dataclass

from injector import Module, provider

from foundations.mediator.mediator import Handler
from usecases.todos.models import Todo


@dataclass(frozen=True)
class DeleteTodoCommand:
    id: int


class DeleteTodoHandler(Handler[DeleteTodoCommand]):
    def __call__(self, request: DeleteTodoCommand, *args, **kwargs):
        try:
            todo = Todo.objects.get(pk=request.id)
            todo.delete()
            return todo
        except Todo.DoesNotExist:
            return None


class DeleteTodoModule(Module):
    @provider
    def create_handler(self) -> Handler[DeleteTodoCommand]:
        return DeleteTodoHandler()
