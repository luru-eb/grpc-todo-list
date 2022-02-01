import string
from dataclasses import dataclass


@dataclass(frozen=True)
class UpdateTodoCommand:
    id: int
    description: string
    is_done: bool
