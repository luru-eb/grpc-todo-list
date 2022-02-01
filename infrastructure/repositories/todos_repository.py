from application.ports.todos_repository import TodosRepositoryInterface
from models.models import Todo


class TodosRepository(TodosRepositoryInterface):
    def get_by(self, id: int):
        return Todo.objects.get(pk=id)

    def get_all(self):
        return Todo.objects.all()

    def save(self, todo: Todo):
        todo.save()

    def remove(self, id: int):
        todo = Todo.objects.get(pk=id)
        todo.delete()
