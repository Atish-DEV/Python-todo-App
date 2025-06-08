
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
        try:
            todo_index=int(input("Enter the index no of the todo Item:"))
            new_todo=input("Enter the new label:")
            todo_list[todo_index-1]=new_todo
            print("1 todo modified")
        except Exception as err:
            print("Exception",err)


    elif user_action=="complete" or user_action=='4':
        try:
            todo_index = int(input("Enter the index no of the todo Item:"))
            complete_todo=todo_list.pop(todo_index-1)
            print(f"{complete_todo} has been completed and removed from todo list...")
        except Exception as err:
            print("Exception", err)


    elif user_action=="exit" or user_action=='5':
        print("For exit operation")
        break


    else:
        print("Invalid Entry ,try again")
        continue


print("Closing the application")


