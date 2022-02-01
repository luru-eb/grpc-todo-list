from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteTodoCommand:
    id: int
