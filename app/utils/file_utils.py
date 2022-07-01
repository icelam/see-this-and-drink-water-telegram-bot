"""File utilities"""

def convert_file_to_list(path, default_value):
    """Read lines from file and put them into a list"""
    try:
        with open(path, encoding='utf8') as file:
            lines = file.readlines()
            result = [line.rstrip() for line in lines]
    except FileNotFoundError:
        result = [default_value]

    return result
