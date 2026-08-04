tasks = []
while True:
 print("==== To_do_Manager ====")
 print("1: Add a task")
 print("2: View tasks")
 print("3: Delete a task")
 print("4: Exit")
 choice = int(input("Choose an option: "))
 if choice == 1:
    print("\n=== Add Task ===")
    task = input("enter the task:")
    save = input("Do you want to save the task? (y/n): ")
    if save.lower() == "y":
        tasks.append(task)
        print("Task saved successfully!")

    else:
        print("Task not saved.")
            
 elif choice == 2:
    print("\n=== View Tasks ===")
    if not tasks:
     print("No tasks found.")
    else:
     print("Tasks:")
     for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
   
 elif choice == 3:
    print("\n=== Delete Task ===")
    if not tasks:
       print("No tasks found.")
    else:
       print ("Tasks:")
       for i, task in enumerate(tasks, start=1):
          print(f"{i}. {task}")
       task_number = int(input("enter the task number to be deleted: "))
       if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Task successfully deleted: {deleted_task}")
       else:
        print("Invalid task number.")

 elif choice == 4:
    print("\n=== Exit ===")
    print("Exiting the program...")
    print ("successfully exited")
    break
 else:
    print("Invalid choice")

    

 