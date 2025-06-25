import re

def collect_matching_areas(file, pattern):
    rows=""
    heading=0
    for row in file:
        if(re.match(f"^#{{1,5}} {pattern}$", row)):
            heading = len(row.split(pattern)[0]) - 1
            rows += row
        elif(heading > 0):
            if (re.match(f"^#{{{1,heading}}}", row)):
                heading = 0
                return rows
            else:
                rows += row
    return rows

def find_match(file, pattern):
    print(f'Opening {file} and searching for "{pattern}"...')
    rows={
        "data": "No match found."
        }
    with open(file) as file:
        rows["data"] = collect_matching_areas(file, pattern)
    file.close()
    return rows

def find_multiple_matches(file, patterns):
    data = [""] * len(patterns)
    for i, pattern in enumerate(patterns):
        print(f'Collecting rows which matches for the pattern "{pattern}"...')
        data[i] = find_match(file, pattern)

    print(f"Matches found on {file}: {data}")
    return data


def find_match_on_list(list, pattern):
    print(f'Opening the list and searching for "{pattern}"...')
    rows=[]
    for i, row in enumerate(list):
        if(re.match(f"diff --git a/{pattern}*", row)):
            print(f"Match found: {row}")
            rows.append({
                "file": re.sub(r'diff --git a/.*?b/', "", row),
                "index": i,
                "data": [],
                })
        elif (len(rows) > 0):
            rows[len(rows) - 1]["data"].append(row)
    print(f"{len(rows)} matches found")
    return rows