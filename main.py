from art import logo
import os
import time

def add(first_n,second_n):
    return first_n + second_n
def difference(first_n,second_n):
    return first_n - second_n
def multiplication(first_n,second_n):
    return first_n * second_n
def division(first_n,second_n):
    return first_n / second_n
def modulo(first_n,second_n):
    return first_n % second_n


        


def calculator (number):
    operation=input("Pick an operation :  ")
    next_number=float(input("What' s the next number ? "))
    
    
    try :
        calcul_number=operator[operation](number,next_number)
    except KeyError :
        print(f"This operator {operation} doesn' t exist in our app  ")
        calcul_number=number
    else :    

        print(f"{first_number} {operation} {next_number}= {calcul_number} ")
        
        
    return calcul_number


end_exercise=False 
while not end_exercise : 
    print(logo)
    first_number=float(input("What' s the first number ?  "))
    operator={"+":add,
              "-":difference,
              "*":multiplication,
              "/":division,
              "%":modulo,
              }
    for op in operator:
        print(op)
    
    same_exercise=True
    while same_exercise:
        first_number=calculator(first_number)
        yes_or_no =input(f"Type \'y\' to continue calculating with {first_number} ,or type \'n\' to start a new calculation :  ")
        if yes_or_no=="n":
            
            same_exercise=False 
            
            other_exercise=input("Type 0 to stop the app , if not type 1 ")
            if other_exercise=="0":
                print("Good Byee  ")
                end_exercise=True  
            else:
                time.sleep(0.1)
                os.system('cls' if os.name=="nt" else 'clear')
            
    
            
        
    
            


