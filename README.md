# Packages



## reader



Provides file reading and writing utilities.



This package exposes functions for reading and writing text files, including pattern-based search and replacement utilities.



### Modules



- **read**: Functions for searching and extracting content from files or lists.

- **write**: Functions for replacing text in files.



#### write.py



Utilities for modifying text files.



This module provides functions to replace text in files, either single or multiple patterns.



##### Functions



- `replace_text(path, old="# test", new="# test edited")`



    Replace all occurrences of a given text pattern in a file with a new string.



    **Args:**

      - `path` (str): Path to the file to modify.

      - `old` (str): The text pattern to search for. Defaults to '# test'.

      - `new` (str): The replacement text. Defaults to '# test edited'.



    **Returns:**

      - file object: The file object after writing (not typically used).



- `replace_multiple_texts(path, old, new)`



    Replace all occurrences of a given text pattern in a file with each string in a list of new patterns.



    **Args:**

      - `path` (str): Path to the file to modify.

      - `old` (str): The text pattern to search for.

      - `new` (list of str): List of replacement texts. Each pattern in the list will replace all occurrences of 'old'.



    **Returns:**

      - file object: The file object after writing (not typically used).

