import grpc
import pytest
from injector import Injector

from features.todos.create import CreateTodoModule
from features.todos.delete import DeleteTodoModule
from features.todos.get_all import GetAllTodosModule
from features.todos.grpc.todos_pb2 import Empty
from features.todos.update import UpdateTodoModule
from todos_server import TodosServer
from features.todos.grpc import todos_pb2_grpc
from foundations.mediator.mediator import Mediator
from models.models import Todo

server = None
port = 50052


def setup_module(module):
    print('*****SETUP*****')
    global server
    container = Injector([
        CreateTodoModule(),
        GetAllTodosModule(),
        UpdateTodoModule(),
        DeleteTodoModule()
    ], auto_bind=False)
    mediator = Mediator(container)
    server = TodosServer(mediator, port)
    server.start()


def teardown_module(module):
    print('*****TEARDOWN*****')
    server.stop()


@pytest.mark.django_db(transaction=True)
def test_should_return_all_todos():
    todos = given_a_list_of_todos()
    with grpc.insecure_channel(f'localhost:{port}') as channel:
        sut = todos_pb2_grpc.TodosStub(channel)
        response = sut.GetAll(Empty())
    assert len(response.todos) == len(todos)


def given_a_list_of_todos():
    todos = [
        Todo(description="What is the meaning of Lorem ipsum?"),
        Todo(description="Why is Lorem Ipsum Dolor used?"),
        Todo(description="What is the most used version?"),
        Todo(description="What are the origins of Lorem Ipsum Dolor Sit?"),
        Todo(description="What is the original text of Lorem Ipsum Dolor Sit Amet?"),
    ]
    Todo.objects.bulk_create(todos)
    return todos
