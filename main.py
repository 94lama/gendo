import sys
import ai, git, reader

arguments=sys.argv

if arguments[1] == "git":
    git_diff = git.get_unstaged_diff_subprocess()
    print(git_diff)

elif arguments[1] == "ai":
    client = ai.client
    ai.agent.ask(client, "")

elif arguments[1] == "readme":
    reader.read()