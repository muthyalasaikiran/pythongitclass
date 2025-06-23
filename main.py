# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("✅ No tasks! You're all caught up.")
        return
    print("\nYour Tasks
