import subprocess

def run_git_command(command, repo_path='.'):
    try:
        result = subprocess.run(
            command,
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True,
            shell=True # Be cautious with shell=True, but often needed for git commands
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(f"Stderr: {e.stderr}")
        return None

def get_unstaged_diff_subprocess(repo_path='.'):
    print(f"Unstaged changes (via subprocess) in {repo_path}:\n")
    diff_output = run_git_command("git diff", repo_path)
    if diff_output:
        print(diff_output)

def get_commit_diff_subprocess(commit_hash_1, commit_hash_2, repo_path='.'):
    print(f"\nChanges between {commit_hash_1[:7]} and {commit_hash_2[:7]} (via subprocess) in {repo_path}:\n")
    diff_output = run_git_command(f"git diff {commit_hash_1} {commit_hash_2}", repo_path)
    if diff_output:
        print(diff_output)

if __name__ == "__main__":
    repo_path = '.' # Or specify your repo path
    # get_unstaged_diff_subprocess(repo_path)
    # get_commit_diff_subprocess("HEAD~1", "HEAD", repo_path)