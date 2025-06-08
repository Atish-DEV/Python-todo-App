FILE_NAME="todoList.txt"
def get_todo(filename=FILE_NAME):
    todo_list=[]
    with open(filename, 'r') as file:
        content = list(file.readlines())
        todo_list = content
    return todo_list


def write_todo(todoList,filename=FILE_NAME):
    with open(filename, 'w') as file:
        file.writelines(todoList)