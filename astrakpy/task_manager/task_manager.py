from astrakpy.task_manager.task import Task
import typing


class TaskManager:
    def __init__(self, app):
        self.loop = app.loop
        self.tasks: typing.List[Task] = []

    def add_task(self, name: str, func: typing.Coroutine):
        self.tasks.append(Task(name, func))

    def _run_tasks(self):
        for task in self.tasks:
            task.run(self.loop)

    def run(self):
        if self.tasks.__len__() <= 0:
            raise ValueError("You have no tasks created.")
        self._run_tasks()
        self.loop.run_forever()

    def get_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return name
        raise LookupError(f"No task found with name {name}.")
