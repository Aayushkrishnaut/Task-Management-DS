# Simple To-Do List Manager

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks, 1):
                status = "Completed" if task.completed else "Pending"
                print(f"{index}. [{status}] {task.description} (Priority: {task.priority})")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.completed = True
            print(f"Marked task as completed: {task.description}")
        else:
            print("Invalid task number.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task number.")

    def get_tasks_by_priority(self, priority):
        priority_tasks = [task for task in self.tasks if task.priority == priority]
        return priority_tasks

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. View tasks by priority")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter priority (high/medium/low): ")
            todo_list.add_task(description, priority)
        
        elif choice == '2':
            todo_list.view_tasks()
        
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_index)
        
        elif choice == '4':
            task_index = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_index)
        
        elif choice == '5':
            priority = input("Enter priority to view (high/medium/low): ")
            priority_tasks = todo_list.get_tasks_by_priority(priority)
            if priority_tasks:
                print(f"\nTasks with {priority} priority:")
                for task in priority_tasks:
                    status = "Completed" if task.completed else "Pending"
                    print(f"[{status}] {task.description}")
            else:
                print(f"No tasks found with {priority} priority.")
        
        elif choice == '6':
            print("Thank you for using the To-Do List Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
