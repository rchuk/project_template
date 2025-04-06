import os
import tempfile
import contextlib
import pandas as pd
from app.io.input import read_file, read_file_pandas


@contextlib.contextmanager
def temp_file(content: str = "", suffix: str = ".txt") -> str:
    file = tempfile.NamedTemporaryFile(mode="w+", suffix=suffix, encoding="utf-8", delete=False)
    try:
        file.write(content)
        file.flush()
        yield file.name
    finally:
        file.close()
        os.remove(file.name)


def test_read_file_text_content():
    content = "Hello, world!"
    with temp_file(content) as path:
        result = read_file(path)
        assert result == content


def test_read_file_empty():
    with temp_file("") as path:
        result = read_file(path)
        assert result == ""


def test_read_file_with_newlines():
    content = "Line 1\nLine 2\nLine 3"
    with temp_file(content) as path:
        result = read_file(path)
        assert result == content


def test_read_file_pandas_csv():
    csv_content = """id,name,country
1,kyiv,ukraine
2,london,united kingdom
3,paris,france
"""
    with temp_file(csv_content, suffix=".csv") as path:
        df_expected = pd.DataFrame({
            "id": [1, 2, 3],
            "name": ["kyiv", "london", "paris"],
            "country": ["ukraine", "united kingdom", "france"]
        })
        df_actual = read_file_pandas(path)
        pd.testing.assert_frame_equal(df_actual, df_expected)


def test_read_file_pandas_empty_csv():
    df_headers_only = pd.DataFrame(columns=["col1", "col2"])
    csv_buffer = df_headers_only.to_csv(index=False)

    with temp_file(csv_buffer, suffix=".csv") as path:
        df_actual = read_file_pandas(path)
        pd.testing.assert_frame_equal(df_actual, df_headers_only)


def test_read_file_pandas_with_booleans():
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["sss123@", "pineapple228"],
        "registered": [True, False]
    })
    csv_buffer = df.to_csv(index=False)

    with temp_file(csv_buffer, suffix=".csv") as path:
        df_actual = read_file_pandas(path)
        pd.testing.assert_frame_equal(df_actual, df)
