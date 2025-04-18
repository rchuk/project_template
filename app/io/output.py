

def write_console(text: str) -> None:
    """
    Print text to the console.
    Args:
        text (str): text to print to the console.
    """
    print(text)


def write_file(text: str, path: str) -> None:
    """
    Print text to file using built-in functions.
    Args:
        text (str): text to be written to file.
        path(str): path of the file to be written to.
    """
    open(path, "w", encoding="utf-8").write(text)
