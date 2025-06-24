import sys
import ai, git, readme

arguments=sys.argv

if arguments[1] == "git":
    git_diff = git.get_unstaged_diff_subprocess()

elif arguments[1] == "ai":
    client = ai.client
    ai.agent.ask(client, "")