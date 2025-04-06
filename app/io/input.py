import pandas as pd


def read_console() -> str:
    """
    Reads input from console.
    Return:
        str. text, entered by the user.
    """
    pass


def read_file(path: str) -> str:
    """
    Reads contents of the file using builtin functions.
    Args:
        path(str): path of the file to be read.
    Return:
        str: contents of the file.
    """
    pass


def read_file_pandas(path: str) -> pd.DataFrame:
    """
    Reads contents of the file using pandas library.
    Args:
        path(str): path to the file to be read.

    Returns:
        df(pandas.DataFrame): contents of the file parsed by pandas.
    """
    pass
