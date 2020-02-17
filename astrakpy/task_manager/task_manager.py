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
        self._run_tasks()
        self.loop.run_forever()
