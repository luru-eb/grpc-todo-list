import string
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateTodoCommand:
    description: string
