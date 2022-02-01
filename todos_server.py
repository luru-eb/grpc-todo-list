from concurrent import futures

import grpc

from grpc_reflection.v1alpha import reflection

from features.todos.api import TodosService
from foundations.grpc import todos_pb2, todos_pb2_grpc
from foundations.mediator.mediator import Mediator


class TodosServer:
    def __init__(self, mediator: Mediator, port=50051):
        self._server = None
        self._mediator = mediator
        self._port = port

    def start(self):
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        todos_pb2_grpc.add_TodosServicer_to_server(
            TodosService(self._mediator),
            self._server
        )
        service_names = (
            todos_pb2.DESCRIPTOR.services_by_name['Todos'].full_name,
            reflection.SERVICE_NAME
        )
        reflection.enable_server_reflection(service_names, self._server)
        self._server.add_insecure_port(f'[::]:{self._port}')
        self._server.start()

    def wait(self):
        self._server.wait_for_termination()

    def stop(self):
        self._server.stop(None)
