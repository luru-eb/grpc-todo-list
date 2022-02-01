# From layered/onion/clean layered architecture to vertical slices architecture

Before digging into the source code, please read this [blog post](https://jimmybogard.com/vertical-slice-architecture/) about vertical slices architecture.

## Layered/onion/clean architectures pain points

In the main branch, we are using a clean architecture approach, which uses abstractions in their use case handlers, such us TodosRepositoryInterface:

```python
class CreateTodoHandler(Handler[CreateTodoCommand]):
    def __init__(self, repository: TodosRepository):
        self._repository = repository

    def __call__(self, command: CreateTodoCommand, *args, **kwargs):
        todo = Todo(description=command.description,)
        self._repository.save(todo)
        return todo
```

The problem with this approach/architecture is you start to get many [abstractions](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/) around concepts that are really abstracted. For example, using a repository pattern to abstract Django ORM. Django ORM is already a repository pattern, it has already given you a persistence ignorance since you can change the underlying database implementation.

If we're using directly Django ORM in our use case handlers we won't be able to have unit test for them, but we can have integration test, which allows us to avoid mock-heavy dependencies and also to test E2E our systems. With the arrival of the containers, we can run anything in them, which makes them very ideal for faster integration testing, so one difference between vertical slices architecture and clean architecture is that the last one does not use indirections.

Another problem is when you are adding or changing a feature in your application, because you are typically changing many layers, which means an increase of the cognitive load for the developer.

In this case the complexity is also caused by a lack of code organisation (Vertical slices forces us to have a clean code organisation), focusing in technical details (handlers, commands, queries, repositories, etc.) rather than features and capabilities.

## The goal os using Vertical slices

> Instead of coupling across a layer, we couple vertical along a slice, minimizing coupling between slices and maximizing coupling in a slice.

In this case, when someone new to a project and does not yet familiar with the codebase, he or she has to add a new feature or modify ab existing one, he/she is not worrying about side effects, because he/she is nor modifying shared code,

## The solution

In the vertical branch you can show how I refactor the current approach to a vertical slices architecture



