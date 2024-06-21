from typing import Callable


def on_each_line(file_path: str, callback: Callable[[str], str]):
    """
    Replace all occurrences of a string in a file with a new string.

    :param file_path: The path to the file.
    :param callback: A callback function that takes a string and returns a new string.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            file.write(callback(line))
