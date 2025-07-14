import sys
import ai, git, reader
import doc

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
    patterns = ["reader", "git", "ai"]

    if len(arguments) == 2:
        doc.diff_doc(patterns)
    elif arguments[2] == "help":
        print("Usage: commit <pattern> <message>")
        print("Pattern: ai, reader, git")
        print("Message: The message to commit")
    elif arguments[2] in patterns:
        doc.diff_doc([argument[2]])