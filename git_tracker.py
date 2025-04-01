import git
from datetime import datetime

class GitTracker:
    def __init__(self, repo_path="."):
        self.repo = git.Repo(repo_path)

    def get_commit_count_today(self):
        today = datetime.today().strftime("%Y-%m-%d")
        commits = list(self.repo.iter_commits(since=today))
        return len(commits)

if __name__ == "__main__":
    tracker = GitTracker()
    print(f"Commits today: {tracker.get_commit_count_today()}")
