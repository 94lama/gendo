import re

def read(file, pattern):
    with open(file) as file:
        for row in file:
            if(re.match(f"^#.*{pattern}$", row)):
                print(f"match: {row}")