import sys
from automated_clean_code import HistLib

file_name = "src/automated_clean_code/data/exercise_20_data.txt"
counter = HistLib().fill_histogram(file_name)


def test_get_args():
    result = HistLib().get_filename_from_args(
        ["src/automated_clean_code/exercise_20_histlib.py", "src/automated_clean_code/data/exercise_20_data.txt"]
    )
    assert result == file_name


def test_fill_histogram():
    assert counter == {"apple": 2, "banana": 1}
    return counter


def test_get_histlib():
    min_key, min_counter, max_key, max_counter = HistLib().get_results(counter)
    assert min_key == "banana"
    assert min_counter == 1
    assert max_key == "apple"
    assert max_counter == 2
