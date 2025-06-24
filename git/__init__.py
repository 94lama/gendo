import sys, re
from .git import *


""" if __name__ == "__main__":
    argument = sys.argv[1]
    if (argument == "-h"):
        print("Add a path in which to verify unstaged filed on git.")
    
    else:
        argument = argument if(not re.match("^\.", argument)) else "."

        print(f"Searching on {argument} directory...")

        repo_path = argument
        get_unstaged_diff_subprocess(repo_path) """