import grpc
from injector import inject

from features.todos.create.create import CreateTodoCommand
from features.todos.delete.delete import DeleteTodoCommand
from features.todos.getall.get_all import GetAllTodosQuery
from features.todos.update.update import UpdateTodoCommand
from features.todos.todos_pb2 import Todo, TodoList, Empty
from features.todos import todos_pb2_grpc
from foundations.mediator.mediator import Mediator


class TodosService(todos_pb2_grpc.TodosServicer):
    @inject
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def GetAll(self, request, context):
        response = self.mediator.send(GetAllTodosQuery())
        todos = [
            Todo(id=todo.id, description=todo.description, is_done=todo.is_done)
            for todo in response
        ]
        return TodoList(todos=todos)

    def Create(self, request, context):
        response = self.mediator.send(CreateTodoCommand(description=request.description))
        return Todo(
            id=response.id,
            description=response.description
        )

    def Update(self, request, context):
        response = self.mediator.send(
            UpdateTodoCommand(
                id=request.id,
                description=request.description,
                is_done=request.is_done
            )
        )
        if response is None:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Todo not found')
        return Todo(
            id=response.id,
            description=response.description,
            is_done=response.is_done
        )

    def Remove(self, request, context):
        response = self.mediator.send(
            DeleteTodoCommand(
                id=request.id,
            )
        )
        if response is None:
            context.abort(grpc.StatusCode.NOT_FOUND, 'Todo not found')
        return Empty()
