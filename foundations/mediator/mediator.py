from typing import TypeVar, Generic, Type

from injector import Injector

TRequest = TypeVar("TRequest")
TResponse = TypeVar("TResponse")


class Handler(Generic[TRequest]):
    def __call__(self, command: TRequest) -> TResponse:
        raise NotImplementedError


class Mediator:
    def __init__(self, container: Injector) -> None:
        self._container = container

    def send(self, request: TRequest) -> TResponse:
        request_cls: Type[TRequest] = type(request)
        handler = self._container.get(Handler[request_cls])
        return handler(request)
