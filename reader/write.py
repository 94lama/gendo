"""
write.py: Utilities for modifying text files.

This module provides functions to replace text in files, either single or multiple patterns.
"""
import re, os

def replace_text(path, old="# test", new= "# test edited"):
    """
    Replace all occurrences of a given text pattern in a file with a new string.

    Args:
        path (str): Path to the file to modify.
        old (str): The text pattern to search for. Defaults to '# test'.
        new (str): The replacement text. Defaults to '# test edited'.

    Returns:
        file object: The file object after writing (not typically used).
    """
    print(path, old, new)
    prev = ""
    res = ""

    with open(path) as file:
        for row in file:
            prev += f"{row}\n"
        file.close()

    with open(path, 'w') as file:
        updated = prev.replace(old, new)
        print(updated)
        if (updated): 
            file.write(updated)
        else:
            print("No match found in file.")
        res = file
        file.close()

    return res

def replace_multiple_texts(path, old, new):
    """
    Replace all occurrences of a given text pattern in a file with each string in a list of new patterns.

    Args:
        path (str): Path to the file to modify.
        old (str): The text pattern to search for.
        new (list of str): List of replacement texts. Each pattern in the list will replace all occurrences of 'old'.

    Returns:
        file object: The file object after writing (not typically used).
    """
    text = ""
    res = ""
    print("Updating the documentation...")
    print(old, new)
    with open(path) as file:
        for row in file:
            text += f"{row}\n"
        file.close()

    with open(path, 'w') as file:
        for i, pattern in enumerate(new):
            text = text.replace(old[i]["data"], pattern)

        if (text): 
            file.write(text)
        else:
            print("No match found in file.")
        res = file
        file.close()

    return res
