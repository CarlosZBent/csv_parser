from pytest import raises
from ..csv_parser import CSVParser

empty_file = CSVParser('empty')
test_file = CSVParser('everyone 246')
test_file2 = CSVParser('everyone 248')

# test empty file

def test_opening_empty_file_returns_attributeerror():
    with raises(LookupError):
        empty_file.get_headers()

# test_write_headers()

def test_write_headers():
    new_headers = ["NAME","EMAIL"]
    test_file.write_headers(new_headers)
    assert test_file.get_headers() == new_headers

# test overwrite

def test_overwrite():
    new_body = [
        ['column1','column1'], 
        ['column2','column2']
    ]
    test_file.overwrite(new_body)
    assert test_file.get_all_rows() == new_body

# test append

def test_append_rows():
    rows = [
        ['column1','column1'], 
        ['column2','column2']
    ]
    test_file.append_rows(rows)
    assert test_file.get_all_rows()[:-2] == rows

def test_append_rows_at_top_of_file():
    rows = [
        ['column1','column1'], 
        ['column2','column2']
    ]
    test_file.append_rows(rows, True)
    assert test_file.get_all_rows()[1:3] == [['column2','column2'], ['column1','column1']]