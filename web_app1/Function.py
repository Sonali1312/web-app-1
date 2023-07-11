def get_todos(filepath='todos.txt'):
    """ To open the file in read mode and read the content of todo"""
    with open(filepath, 'r') as file_1:
        todos1 = file_1.readlines()
    return todos1


def write_todos(todos_w, filepath='todos.txt'):
    """ To open the file in write mode and read the content of todo"""
    # filepath = "todos_1.txt"
    with open(filepath, 'w') as file:
        file.writelines(todos_w)


if __name__ == "__main__":
    print("hello")
