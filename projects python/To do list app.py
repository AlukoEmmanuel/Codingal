import sys

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{idx}. {task['title']} - {status}")

def add_task(title):
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added.")

def delete_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['title']}' deleted.")
    except IndexError:
        print("Invalid task number.")

def complete_task(index):
    try:
        tasks[index - 1]['completed'] = True
        print(f"Task '{tasks[index - 1]['title']}' marked as complete.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '3':
            show_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == '4':
            show_tasks()
            index = int(input("Enter task number to mark as complete: "))
            complete_task(index)
        elif choice == '5':
            print("Exiting To-Do List Manager.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()