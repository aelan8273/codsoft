tasks = []

def add_task():
    task = input("Enter the Task: ")
    tasks.append({"task":task,"done":False})
    print("Task added!")

def view_task():
    if not tasks:
        print("NO Thanks available.")
        return
    for idx, t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{idx +1}.{t['task']}[{status}]")

def mark_complete():
    view_task()
    try:
        idx = int(input("Enter task number to mark as complete: ")) -1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid")

while True:
    print("\n---To-Do-Menu-----")
    print("1. View Task")
    print("2. Add Task")
    print("3. Mark Task as complete")
    print("4. Exit Task")

    choice = input("Choose an option(1:4): ")

    if choice == "1":
        view_task()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        print("Exiting........... Goodbye!")
        break
    else:
        print("Invalid choice. Please select from 1 To 4. ")
