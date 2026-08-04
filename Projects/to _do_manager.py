tasks = []
starred_tasks = []
while True:
 print("==== To_do_Manager ====")
 print("1: Add a task")
 print("2: View tasks")
 print("3: Delete a task")
 print("4: Star a task")
 print("5: Exit")
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
        if task in starred_tasks:
            print(f"{i} * {task}")
        else:
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
        deleted_task = tasks[task_number - 1]
        tasks.remove(deleted_task)
        print(f"Task successfully deleted: {deleted_task}")
        if deleted_task in starred_tasks:
            starred_tasks.remove(deleted_task)
       else:
        print("Invalid task number.")

 elif choice == 4:
      print("\n=== Star Task ===")
      if not tasks:
         print("No tasks found.")
      else:
         print("Tasks:")
         for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
         task_number = int(input("Enter the task number to star: "))
         if 1 <= task_number <= len(tasks):
            starred_task = tasks[task_number - 1]
            starred_tasks.append(starred_task)
            print(f"Task successfully starred: {starred_task}")
         else:
            print("Invalid task number.")

 elif choice == 5:
           print("\n=== Exit ===")
           print("Exiting the program...")
           print ("successfully exited")
           break
 else:
    print("Invalid choice")

    

 