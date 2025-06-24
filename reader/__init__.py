import os, re
from .read import *

readme = f"{os.path.curdir}/README.md"
default_patterns = ['components']

def read(patterns=default_patterns):
    data = [""] * len(patterns)
    for i, pattern in enumerate(patterns):
        print(f'Collecting rows which matches for the pattern "{pattern}"...')
        data[i] = find_match(readme, pattern)

    print("Collected all matches.")
    return data