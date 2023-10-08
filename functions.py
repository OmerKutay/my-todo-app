def get_todos(filepath="todos.txt"):
    """Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """write todos fonksiyonu ile dosyanın içerisine yapılacak işleri yazabiliriz."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


text = """
principles of productivity
managing your inflow.      
systemizing everything that repeats       
"""
