import os, re
from .read import *

readme = f"{os.path.curdir}/README.md"
patterns = ['components']

if __name__ == "__main__":
    for pattern in patterns:
        data = read(readme, pattern)
        print(data)