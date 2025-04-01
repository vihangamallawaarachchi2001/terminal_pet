import git
from datetime import datetime

class GitTracker:
    def __init__(self, repo_path="."):
        try:
            self.repo = git.Repo(repo_path)
        except git.exc.InvalidGitRepositoryError:
            self.repo = None  # No repo found

    def get_commit_count_today(self):
        if not self.repo:
            return 0  # Return 0 if no repo
        today = datetime.today().strftime("%Y-%m-%d")
        commits = list(self.repo.iter_commits(since=today))
        return len(commits)

if __name__ == "__main__":
    tracker = GitTracker()
    print(f"Commits today: {tracker.get_commit_count_today()}")
