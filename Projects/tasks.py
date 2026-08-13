def hello():
    print("Hello from the tasks module!")
import json
tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            loaded_tasks = json.load(file)
            tasks.extend(loaded_tasks)
    except FileNotFoundError:
        pass
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_menu():
    print("==== To_do_Manager ====")
    print("1: Add a task")
    print("2: View tasks")
    print("3: Delete a task")
    print("4: Star a task")
    print("5: Mark a task as completed")
    print("6: Exit")
def add_task():
    print("\n=== Add Task ===")
    task = input("enter the task:")
    save = input("Do you want to save the task? (y/n): ")
    if save.lower() == "y":
         tasks.append(
            {"title": task, "starred": False, "completed": False}
         )
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
        if task["starred"] and task["completed"]:
                     print(f"{i} ⭐ [✔] {task['title']}")
        elif task["starred"]:
            print(f"{i} ⭐ {task['title']}")
        elif task["completed"]:
            print(f"{i}. [✔] {task['title']}")
        else:
            print(f"{i}. {task['title']}")
def delete_task():
        print("\n=== Delete Task ===")
        if not tasks:
           print("No tasks found.")
        else:
           print ("Tasks:")
           for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']}")
           try:
             task_number = int(input("enter the task number to be deleted: "))
           except ValueError:
             print("Invalid number. Enter a valid number.")
             return

           if 1 <= task_number <= len(tasks):
            deleted_task = tasks[task_number - 1]
            tasks.pop(task_number - 1)
            save_tasks()
            print(f"Task successfully deleted: {deleted_task['title']}")
            
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
       print(f"{i}. {task['title']}")
      try:
       task_number = int(input("Enter the task number to star: "))
      except ValueError:
       print("Invalid number. Enter a valid number.")
       return
      if 1 <= task_number <= len(tasks):
        starred_task = tasks[task_number - 1]
        starred_task["starred"] = not starred_task["starred"]
        save_tasks()
        if starred_task["starred"]:
            print(f"Task starred: {starred_task['title']}")
            
        else:
         print(f"Task unstarred: {starred_task['title']}")
        
      else:
       print("Invalid task number.")
def mark_task_completed():
    print("\n=== Mark Task as Completed ===")
    if not tasks:
        print("no tasks found")
    else:
       print ("Tasks:")
       for i, task in enumerate(tasks, start=1):
           print(f"{i}. {task['title']}")
    try:
            task_number = int(input("Enter the task number to mark as completed: "))
    except ValueError:
            print("Invalid number. Enter a valid number.")
            return
    if 1 <= task_number <= len(tasks):
        completed_task = tasks[task_number - 1]
        completed_task["completed"] = not completed_task["completed"]
        
        save_tasks()
        if completed_task["completed"]:
         print(f"Task completed: {completed_task['title']}")
        else:
            print(f"Task marked as not completed: {completed_task['title']}")

    else:
        print("Invalid task number.")
