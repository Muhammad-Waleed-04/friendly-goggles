def add_task():
    task = input("Enter task: ")
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    print("Task added.")

def view_tasks():
    print("\n--- To-Do List ---")
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    with open("todo.txt", "r") as f:
        tasks = f.readlines()
    if 0 < num <= len(tasks):
        del tasks[num - 1]
        with open("todo.txt", "w") as f:
            f.writelines(tasks)
        print("Task deleted.")
    else:
        print("Invalid number.")

def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

menu()
