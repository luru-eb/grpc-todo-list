from typing import TypeVar, Generic, Type

from injector import Injector

TCommand = TypeVar("TCommand")
TResponse = TypeVar("TResponse")


class Handler(Generic[TCommand]):
    def __call__(self, command: TCommand) -> TResponse:
        raise NotImplementedError


class Mediator:
    def __init__(self, container: Injector) -> None:
        self._container = container

    def send(self, command: TCommand) -> TResponse:
        command_cls: Type[TCommand] = type(command)
        handler = self._container.get(Handler[command_cls])
        return handler(command)
