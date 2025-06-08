
print("Initializing todo App...")
MENU='Todo list options Add,Show,Edit,Complete,Exit :'
todo_list=[]
while True:
    user_action=input(MENU).lower()
    if user_action=="add" or user_action=='1':
        new_todo=input("Enter a new todo Item :")+'\n'
        todo_list_2=[]
        try:
            with open("todoList.txt",'r') as file:
                content=list(file.readlines())
                todo_list_2=content
            todo_list_2.append(new_todo)
            with open("todoList.txt",'w') as file:
                file.writelines(todo_list_2)
        except Exception as err:
            #if File does not exist,create a new file
            with open("todoList.txt",'w') as file:
                file.write(new_todo)
        finally:
            print("New todo item has been added")
    elif user_action=="show" or user_action=='2':
        todo_list_2 = []
        try:
            with open("todoList.txt", 'r') as file:
                content = list(file.readlines())
                todo_list_2=content
            for index, item in enumerate(todo_list_2):
                    print(f"{index + 1}-{item[:-1]}")
        except Exception as err:
            print('No Task has been added')
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


