import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import reader

path = "tests/README.md"

def test_read_file():
    res = reader.find_match(path, "# test")
    assert len(res) > 0

def test_write_file():
    res = reader.replace_text(path)
    assert res

    with open(path, 'w') as file:
        file.write("# test")

def test_replace_multiple_texts():
    res = reader.write.replace_multiple_texts(path, "#test", ["new test"])
    assert res