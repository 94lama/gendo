import sys
import ai, git, reader

arguments=sys.argv

if arguments[1] == "git":
    git_diff = git.get_unstaged_diff_subprocess()
    print(git_diff)

elif arguments[1] == "ai":
    client = ai.client
    ai.agent.ask(client, "")

elif arguments[1] == "reader":
    reader.read()

elif arguments[1] == "commit":
    import os

    patterns = ["reader"]
    path = f"{os.path.curdir}/README.md"
    git_diff = git.get_unstaged_diff_subprocess()
    git_diff = reader.find_match_on_list(git_diff.split("\n"), patterns[0])
    
    response = "No match found."
    readme = reader.read.find_multiple_matches(path, patterns)

    print(readme)
    if(len(git_diff) > 0):
        import os

        client = ai.client
        response = ai.agent.ask(client, map(lambda x: x["data"], readme), git_diff[0]["data"])
        reader.write.replace_text(path, readme[0]["data"], response)
        #reader.write.replace_multiple_texts(path, readme, response)

    print("Process ended.")