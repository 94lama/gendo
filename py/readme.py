import os, re

readme = f"{os.path.curdir}/README.md"
patterns = ['components']

with open(readme) as file:
    for row in file:
        if(re.match(f"^#.*{patterns[0]}$", row)):
            print(f"match: {row}")