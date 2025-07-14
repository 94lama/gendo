import os, ai, git, reader

path = f"{os.path.curdir}/README.md"

def diff_doc(patterns):
    git_diff = git.get_unstaged_diff_subprocess()
    git_diff = reader.find_match_on_list(git_diff.split("\n"), patterns[0])
    
    response = "No match found."
    mathces = reader.read.find_multiple_matches(path, patterns)

    print(mathces)
    if(len(git_diff) > 0):
        import os

        client = ai.client
        response = ai.agent.ask(client, map(lambda x: x["data"], mathces), git_diff[0]["data"])
        #reader.write.replace_text(path, mathces[0]["data"], response)
        reader.write.replace_multiple_texts(path, mathces, response)

    print("Process ended.")