FILEPATH = "todos.txt"


def get_todos(FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(FILEPATH, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(FILEPATH, 'w') as file_local:
        file_local.writelines(todos_arg)

