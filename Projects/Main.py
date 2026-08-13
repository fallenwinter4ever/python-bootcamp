import tasks
tasks.load_tasks()
def show_menu():
    print("==== To_do_Manager ====")
    print("1: Add a task")
    print("2: View tasks")
    print("3: Delete a task")
    print("4: Star a task")
    print("5: Mark a task as completed")
    print("6: Exit")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        tasks.add_task()
    elif choice == "2":
        tasks.view_tasks()
    elif choice == "3":
        tasks.delete_task()
    elif choice == "4":
        tasks.star_task()
    elif choice == "5":
        tasks.mark_task_completed()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")

