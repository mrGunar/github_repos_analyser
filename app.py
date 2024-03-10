import os

from github import GithubException
from dotenv import load_dotenv

import auth

load_dotenv()


def is_file_empty(commit_file):
    return (
        commit_file["additions"] == 0
        and commit_file["deletions"] == 0
        and commit_file["changes"] == 0
    )


def main():
    g = auth.get_github_by_access_token(os.getenv("ACCESS_TOKEN_GITHUB"))

    user = g.get_user()
    total_add = 0
    total_del = 0

    for repo in user.get_repos():
        repo_name = repo.full_name

        if not repo_name.startswith(user.login):
            continue

        print(f"Start processing {repo.full_name}")

        try:
            commits = list(repo.get_commits())
        except GithubException:
            print(f"Repo `{repo_name}` is empty. Skip it.")
            continue

        for commit in commits:
            try:
                if commit.author.login != user.login:
                    continue
            except AttributeError:
                # In some cases there is not an author in the commit.committer property.
                commit_author = commit.raw_data["commit"]["author"]["name"]
                if commit_author != user.login:
                    continue

            for file in commit.raw_data["files"]:
                file_name = file["filename"]
                if is_file_empty(file) or not file_name.endswith(".py"):
                    continue

                total_add += file["additions"]
                total_del += file["deletions"]

    g.close()

    print(f"Total number of additional rows in all projects is: {total_add}")
    print(f"Total number of deletional rows in all projects is:{total_del=}")


if __name__ == "__main__":
    main()
