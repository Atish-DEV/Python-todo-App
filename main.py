from enum import Enum
from fileOperations import get_todo,write_todo

class Actions(Enum):
    ADD=1,
    SHOW=2,
    EDIT=3,
    COMPLETE=4,
    EXIT=5


print("Initializing todo App...")
MENU='Todo list options Add,Show,Edit,Complete,Exit :'
while True:
    user_action=input(MENU).upper()
    if user_action==Actions.ADD.name or user_action==Actions.ADD.value:
        new_todo=input("Enter a new todo Item :")+'\n'
        try:
            todo_list=get_todo()
            todo_list.append(new_todo)
            write_todo(todo_list)
        except Exception as err:
            #if File does not exist,create a new file
            with open("todoList.txt",'w') as file:
                file.write(new_todo)
        finally:
            print("New todo item has been added")
    elif user_action==Actions.SHOW.name or user_action==Actions.SHOW.value:
        try:
            todo_list = get_todo()
            for index, item in enumerate(todo_list):
                    print(f"{index + 1}-{item[:-1]}")
        except Exception as err:
            print('No Task to be display')
    elif user_action==Actions.EDIT.name or user_action==Actions.EDIT.value:
        try:
            todo_index=int(input("Enter the index no of the todo Item:"))
            new_todo=input("Enter the new label:")+'\n'
            todo_list = get_todo()
            todo_list[todo_index-1]=new_todo
            write_todo(todo_list)
            print("1 todo modified")
        except FileNotFoundError:
            print("No Task has been added yet !!")
        except IndexError:
            print("No task has been found at this index")
    elif user_action==Actions.COMPLETE.name or user_action==Actions.COMPLETE.value:
        try:
            todo_index = int(input("Enter the index no of the todo Item:"))
            todo_list = get_todo()
            complete_todo=todo_list.pop(todo_index-1)
            write_todo(todo_list)
            print(f"{complete_todo[:-1]} has been completed and removed from todo list...")
        except FileNotFoundError:
            print("No Task has been added yet !!")
        except IndexError:
            print("No task has been found at this index")
    elif user_action==Actions.EXIT.name or user_action==Actions.EXIT.value:
        exit("Closing the application")
    else:
        print("Invalid Entry ,try again")
        continue


