 # To-Do List Application

tasks = []

def add_task():
    task = input("Enter the task: ").strip()
    tasks.append({'task': task, 'done': False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
        return
    print("\n--- To-Do List ---")
    for i, item in enumerate(tasks, 1):
        status = "✅ Done" if item['done'] else "❌ Not done"
        print(f"{i}. {item['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['done'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()