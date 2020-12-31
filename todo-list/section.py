from demo.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        tasks_names = [t.name for t in self.tasks]
        if new_task.name in tasks_names:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        tasks_names = [t.name for t in self.tasks]
        if task_name not in tasks_names:
            return f'Could not find task with the name {task_name}'
        index = tasks_names.index(task_name)
        self.tasks[index].completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        all_tasks_count = len(self.tasks)
        uncompleted_tasks = [t for t in self.tasks if not t.completed]
        removed_tasks_count = all_tasks_count - len(uncompleted_tasks)
        return f'Cleared {removed_tasks_count} tasks.'

    def view_section(self):
        section_name = f'Section {self.name}:\n'
        tasks_info = '\n'.join([t.details() for t in self.tasks])
        return section_name + tasks_info



