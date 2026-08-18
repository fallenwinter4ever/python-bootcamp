import random
secret_number= random.randint(1, 5)
def guess_the_number(minimum, maximum, message="guess the number if you can "):
 
 while True:
    try:
        number =int(input(message))
        
        if not minimum<= number<= maximum:
         print("uh oh..try to stay in rules.1 to 5 remember?")
         continue

        
        if number == secret_number:
           return number 
           
           
           
        else:
         print("oops..try again will ya")
        
          
          
         
         
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    

while True:
 number=guess_the_number(1, 5, "guess the number if you can ") 
 
 print(f"your number is {number}")
 break



        
