
print("Initializing todo App...")
MENU='Todo list options Add,Show,Edit,Complete,Exit :'
todo_list=[]
while True:
    user_action=input(MENU).lower()
    if user_action=="add" or user_action=='1':
        new_todo=input("Enter a new todo Item :")
        todo_list.append(new_todo)
        print("New todo item has been added")
    elif user_action=="show" or user_action=='2':
        for index,item in enumerate(todo_list):
            print(f"{index+1}-{item}")
    elif user_action=="edit" or user_action=='3':
        print("For show operation")
    elif user_action=="complete" or user_action=='4':
        print("For complete operation")
    elif user_action=="exit" or user_action=='5':
        print("For exit operation")
        break
    else:
        print("Invalid Entry ,try again")
        continue
print("Closing the application")


