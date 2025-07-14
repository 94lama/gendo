import os, ai, git, reader
from config import config

# Validate configuration on startup
if not config.validate():
    exit(1)

path = f"{os.path.curdir}/{config.README_PATH}"

def diff_doc(patterns):
    git_diff = git.get_unstaged_diff_subprocess()
    git_matches = reader.find_match_on_list(git_diff.split("\n"), patterns[0])
    
    response = "No match found."
    mathces = reader.read.find_multiple_matches(path, patterns)

    if(len(git_matches) > 0):
        client = ai.client
        response = ai.agent.ask(client, map(lambda x: x["data"], mathces), git_matches[0]["data"])
        #reader.write.replace_text(path, mathces[0]["data"], response)
        reader.write.replace_multiple_texts(path, mathces, response)

    print("Process ended.")