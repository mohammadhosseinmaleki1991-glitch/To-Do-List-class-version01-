import csv


class Task:

    def __init__(self, tasks, details, priority):
        self.tasks = tasks
        self.details = details
        self.priority = priority

    def get_tasks(self):

        return self.tasks

    def set_task(self, new_task):

        self.tasks = new_task

    def __str__(self):
        return f"Tasks:{self.tasks}, Details:{self.details}, Priority:{self.priority}"


class ToDoList:

    def __init__(self, filename=r"write your path address"):
        self.filename = filename
        self.tasks = []
        self._load_tasks_from_csv()

    def add_task(self, task_input, details=None, priority=None):
        if isinstance(task_input, Task):
            task = task_input
        else:
            task = Task(task_input, details, priority)

        self.tasks.append(task)
        self._save_tasks_to_csv()

    def _load_tasks_from_csv(self):
        try:
            with open(self.filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tasks.append(
                        Task(row["Tasks"], row["Details"], row["Priority"])
                    )
        except FileNotFoundError:
            pass

    def _save_tasks_to_csv(self):
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["Tasks", "Details", "Priority"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(
                    {
                        "Tasks": task.tasks,
                        "Details": task.details,
                        "Priority": task.priority,
                    }
                )

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.tasks != task_name]
        self._save_tasks_to_csv()

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.tasks} | {task.details} | Priority: {task.priority}")


def main_menu():
    execute = ToDoList()

    while True:
        print("\n---To-Do List---")
        print("---------")
        print("1. Add task")
        print("2. Remove task")
        print("3. View all tasks")
        print("4. Quit")

        _entry = input("Enter desired option: ")
        if _entry == "1":
            task_name = input("Enter task name: ")
            details = input("Enter task details: ")
            priority = input("Enter task priority: ")
            new_task = Task(task_name, details, priority)
            execute.add_task(new_task)
        elif _entry == "2":
            task_name = input("Enter the task name to remove: ")
            execute.remove_task(task_name)
        elif _entry == "3":
            execute.view_all_tasks()
        elif _entry == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()
