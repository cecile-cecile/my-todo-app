FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# procedural function, nothing to return
def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# if we run functions.py, the value of __name__ is __main__
print(__name__)

# this executes, only if we run functions.py
# will not execute, when running cli.py -> value of __name__ is functions
if __name__ == "__main__":
    print("Hello")
    print(get_todos())