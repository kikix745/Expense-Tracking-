from colorama import Fore, Style, init

init()
list1=[]

def main_menu():
    print("========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3.Total spent ")
    print("4.Delete Expense")
    print("5. Exit")
    print("=====================================")
    
def Add_Expense():
    expense=input("enter your expense")
    amount=int(input("enter your amount  "))
    description=input("enter your decription")
    list1.append({"Expense":expense,"Amount":amount,"Description":description})

def  View_Expenses():
    if not list1:
        print("No expences yet")
        return
    for index,ex in enumerate(list1,start=1):

       print(Fore.GREEN + f"{index}. Expense: {ex['Expense']},Amount: {ex['Amount']},Description: {ex['Description']}" + Style.RESET_ALL)
    
def Total_spent():
    total=0
    for expense in list1:
        total=total+expense['Amount']
    print(Fore.GREEN + f"The total spent is :  {total} euro " + Style.RESET_ALL)     

def Delete_Expense():
    main_menu()
    try:
        index=int(input("enter the expense number to delete"))-1
        if 0<=index<len(list1) :
            removed_ex=list1.pop(index)
            print(f"deleted task:{ removed_ex}")
        else:
            print("invalid number")   
    except ValueError:
        print("enter real number")
        
while True:
        main_menu()
        choice=input("enter the index of the choice ")
        
        if (choice=='1'):
             Add_Expense()
             
        elif (choice=='2'):
            View_Expenses()
            
        elif (choice=='3'): 
             Total_spent()  
             
        elif (choice=='4'): 
             Delete_Expense()  
             
        elif (choice=='5'): 
            print("GoodBye Mate")
            break
        else:
            print("invalid choice try again")    
             