students = [
    {
        "name": "Alex",
        "score": 85,
        "subjects": {"Python", "Math"}
    },
    {
        "name": "Maya",
        "score": 92,
        "subjects": {"Python", "Physics"}
    }
]

def show_menu():
    print("===== STUDENT MANAGER =====")
    print("1. Show_all_students")
    print("2. Show_students_scoring_80+")
    print("3. Find_a_student")
    print("4. Add_a_student")
    print("5. Exit")

def show_student():
   print("\n=== View Existing Students ===")
   if not students:
     print("No students found.")
   else:
     print(students) 

def student_above_80(students):
    return [student["name"] for student in students if student["score"] >= 80]

def find_student():
  
    x = input("Search name: ")
    
    for student in students:
        if student["name"]== x:
            print(student)
            break
    else:
        
        print("no name found")

def add_student():
    print("\n=== Add Student ===")
    nam = input("enter the name:")
    try:
        scor = int(input("enter student score: "))
        
    except ValueError:
        print("enter a valid score")
        return
    try:
       if not (0 <= scor <= 100):
                   raise ValueError("Score out of range")
    except ValueError as error:
        print("Error:" , error)
        return   
         
     
    sub = {s.strip() for s in input("Enter the subjects: ").split(",")}
    save = input("Do you want to save the student? (y/n): ")
    
    if save.lower() == "y":
        students.append({"name": nam, "score": scor, "subjects": sub})
        print("Student saved successfully!")
    else:
        print("Student not saved.")


def exit_program():
    print("Exiting the program...")
    print ("successfully exited")
try:
 while True:
   show_menu()
   choice = input("Enter your choice: ")
   if choice == "1":
      show_student()
   elif choice == "2":
      names = student_above_80(students)
       
      print(names)

   elif choice == "3":
      find_student()
   elif choice == "4":
      add_student()
   elif choice == "5":
      exit_program()
      break
   else:
      print("invalid number")
finally:
   print("program finished")
       
   
