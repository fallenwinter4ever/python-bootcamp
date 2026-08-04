tasks = []
starred_tasks = []
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                tasks.append(line.strip())

    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    

def show_menu():
    print("==== To_do_Manager ====")
    print("1: Add a task")
    print("2: View tasks")
    print("3: Delete a task")
    print("4: Star a task")
    print("5: Exit")
def add_task():
    print("\n=== Add Task ===")
    task = input("enter the task:")
    save = input("Do you want to save the task? (y/n): ")
    if save.lower() == "y":
         tasks.append(task)
         save_tasks()
         print("Task saved successfully!")
   
    else:
           print("Task not saved.")
def view_tasks():
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
def delete_task():
        print("\n=== Delete Task ===")
        if not tasks:
           print("No tasks found.")
        else:
           print ("Tasks:")
           for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
           try:
             task_number = int(input("enter the task number to be deleted: "))
           except ValueError:
             print("Invalid number. Enter a valid number.")
             return

           if 1 <= task_number <= len(tasks):
            deleted_task = tasks[task_number - 1]
            tasks.pop(task_number - 1)
            save_tasks()
            print(f"Task successfully deleted: {deleted_task}")
            if deleted_task in starred_tasks:
             starred_tasks.remove(deleted_task)
           else:
            print("Invalid task number.")
            return
def star_task():
   print("\n=== Star Task ===")
   if not tasks:
      print("No tasks found.")
   else:
      print("Tasks:")
      for i, task in enumerate(tasks, start=1):
       print(f"{i}. {task}")
      try:
       task_number = int(input("Enter the task number to star: "))
      except ValueError:
       print("Invalid number. Enter a valid number.")
       return
      if 1 <= task_number <= len(tasks):
        starred_task = tasks[task_number - 1]
        starred_tasks.append(starred_task)
        print(f"Task successfully starred: {starred_task}")
      else:
       print("Invalid task number.")
def exit_program():
    print("\n=== Exit ===")
    print("Exiting the program...")
    print ("successfully exited")
load_tasks()
while True:
 show_menu()
 try:
    choice = int(input("Choose an option: "))
 except ValueError:
      print("Invalid input. Please enter a number.")
      continue
 if choice == 1:
     add_task()
 elif choice == 2:
     view_tasks()
 elif choice == 3:
     delete_task()
 elif choice == 4:
     star_task()
 elif choice == 5:
     exit_program()
     break
 else:
    print("Invalid choice")
