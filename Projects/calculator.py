
   
def calculator():
 
    x = int(input("your 1st number is: "))
    y = int(input("your 2nd number is: "))
    return x , y
    

 

 


 
def addition ():
    try: 
     x , y = calculator()
     result = x + y
     print(result)
    except ValueError:
       print("invalid number")
def subtraction ():
    try:
      x , y = calculator()
      result = x - y
      print(result)
    except ValueError:
     print("invalid number") 
def multiplication():
    try:
       x , y = calculator()
       result = x*y
       print(result)
    except ValueError:
       print("invalid number")
def division():
    try:
        x, y = calculator()
        result = x / y
    except ValueError:
       print("invalid number")
       
    except ZeroDivisionError:
        print("oops... you cant div by 0")
    else:
       print(result)
def show_menu():
    print("Welcome to Calculator")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
def exit_program():
    
    print("Exiting the program...")
    print ("successfully exited")
    
try:  
 while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
      addition()
    elif choice == "2":
      subtraction()
    elif choice == "3":
      multiplication()
    elif choice == "4":
      division()
    elif choice == "5":
      exit_program()
      break
    else:
      print("invalid number")
        
finally:
     print("program finished")
     
  

  
   




   
  
