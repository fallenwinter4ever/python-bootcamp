tasks = []
while True:
 print("==== To_do_Manager ====")
 print("1: Add a task")
 print("2: View tasks")
 print("3: Exit")
 choice = int(input("Choose an option: "))
 if choice == 1:
    print("you chose option 1")
    task = input("enter the task:")
    save = input("Do you want to save the task? (y/n): ")
    if save.lower() == "y":
        tasks.append(task)
        print("Task saved successfully!")

    else:
        print("Task not saved.")
            
 elif choice == 2:
    print("you chose option 2")
    if not tasks:
     print("No tasks found.")
    else:
     print("Tasks:")
     for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
   
 elif choice == 3:
    print("you chose option 3")
    print("Exiting the program...")
    print ("successfully exited")
    break
 else:
    print("Invalid choice")

 