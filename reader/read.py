import re

def collect_matching_areas(file, pattern):
    rows=""
    heading=0
    for row in file:
        if(re.match(f"^#{{1,5}}\s{pattern}$", row)):
            heading = len(row.split(pattern)[0]) - 1
            rows += row
        elif(heading > 0):
            if (re.match(f"^#{{{heading}}}", row)):
                heading = 0
                return rows
            else:
                rows += row

def find_match(file, pattern):
    print(f'Opening {file} and searching for "{pattern}"...')
    rows="No match found."
    with open(file) as file:
        rows = collect_matching_areas(file, pattern)
    file.close()
    return rows