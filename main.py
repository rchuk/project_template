from app.io.input import read_console, read_file, read_file_pandas
from app.io.output import write_console, write_file


def write(text: str, path: str) -> None:
    write_console(text)
    write_file(text, path)


def main():
    console_text = read_console()
    file_text = read_file("./data/input.txt")
    pandas_data = read_file_pandas("./data/input.csv")

    write(console_text, "./data/console_output.txt")
    write(file_text, "./data/file_output.txt")
    write(str(pandas_data), "./data/pandas_output.txt")


if __name__ == "__main__":
    main()
