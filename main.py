import sys, os
import ai, git, reader
import document_generator

arguments=sys.argv

def get_principal_subdirectories(directory):
    """Return a list of principal subdirectories in the given directory."""
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

# Set the patterns variable to the principal subdirectories of the current directory
patterns = get_principal_subdirectories(os.path.curdir)


if len(arguments) == 1:
    print("Welcome to Gendo!")
    print("This tool is meant to help you generate documentation for your project.")
    print("It is a work in progress and will be updated soon.")
    print("For now, you can use it to generate documentation for your project.")
    print("To see the patterns, use the command 'patterns'.")
    print("To see the help, use the command 'help'.")
    print("To see the git diff, use the command 'git'.")
    print("To see the ai response, use the command 'ai'.")
    exit(0)

elif arguments[1] == "help":
    print("Usage: commit <pattern> <message>")
    print("patterns: list of patterns")
    print("commit: verifies the diff and generates the documentation")
    print("git: shows the git diff")
    print("ai: shows the ai response")
    print("reader: shows the reader response")
    exit(0)

elif arguments[1] == "patterns":
    print(f"Patterns: ${patterns}")
    exit(0)

elif arguments[1] == "git":
    git_diff = git.get_unstaged_diff_subprocess()
    print(git_diff)

elif arguments[1] == "ai":
    client = ai.client
    ai.agent.ask(client, "")

elif arguments[1] == "reader":
    reader.read()

elif arguments[1] == "commit":
    if len(arguments) == 2:
        document_generator.diff_doc(patterns)
    elif arguments[2] == "help":
        print("Usage: commit <pattern> <message>")
        print("Pattern: ai, reader, git")
        print("Message: The message to commit")
    elif arguments[2] in patterns:
        document_generator  .diff_doc([argument[2]])