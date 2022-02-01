from models.models import Todo


class TodosRepositoryInterface:
    def get_by(self, id: int):
        pass

    def get_all(self):
        pass

    def save(self, todo: Todo):
        pass

    def remove(self, id: int):
        pass