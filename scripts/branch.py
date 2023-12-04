from git import Repo

repo = Repo('.')
current_branch = repo.active_branch


def checkout(branch_name: str):
    # detect if branch exists, if not, create it
    if branch_name not in repo.branches:
        repo.create_head(branch_name)
    # checkout branch
    repo.git.checkout(branch_name)
