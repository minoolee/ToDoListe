# To Do Liste

class Task:
    def __init__(self, description):
        self.description = description

        self.completed = False

    def merk_as_completed(self):
        self.completed = True


    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.description}"



class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_new_task(self, task):
        self.tasks.append(task)

    def show_task(self):
        if not self.tasks:
            print("No task in the List")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(index, task)


    def remove_task(self, index):
        self.tasks.remove(index)


    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index-1]
            task.mark_as_completed()
            print(f"Mark the task '{task.description}' as completed")
        else:
            print("Invalid task index.")

    def check_completion(self):
        all_completed = all(task.completed for task in self.tasks)
        if all_completed:
            print("All tasks completed!")


list = ToDoList()

task = Task("Cooding")
task2 = Task("Yoga")
task4 = Task("Sleeping")
list.add_new_task(task)
list.add_new_task(task2)
list.add_new_task(task4)
task4.merk_as_completed()
list.remove_task(task)
list.show_task()
task.merk_as_completed()
print(list)
print(task)