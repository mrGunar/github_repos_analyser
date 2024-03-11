import typing as tp

from github import GithubException

import dto


def is_file_empty(commit_file):
    return (
        commit_file["additions"] == 0
        and commit_file["deletions"] == 0
        and commit_file["changes"] == 0
    )


def analyse_file(file):
    file_name = file["filename"]

    if is_file_empty(file) or not file_name.endswith(".py"):
        return dto.CommitStat()

    return dto.CommitStat(file["additions"], file["deletions"])


def analyse_files_from_commit(files: tp.Iterable) -> dto.CommitStat:
    stats = dto.CommitStat()
    for file in files:
        stats += analyse_file(file)
    return stats


def get_all_commits(user_login, user_repos):
    for repo in user_repos:
        repo_name = repo.full_name

        if not repo_name.startswith(user_login):
            continue

        print(f"Start processing {repo.full_name}")

        try:
            commits = list(repo.get_commits())
        except GithubException:
            print(f"Repo `{repo_name}` is empty. Skip it.")
            continue

        for commit in commits:
            try:
                if commit.author.login != user_login:
                    continue
            except AttributeError:
                # In some cases there is not an author in the commit.committer property.
                commit_author = commit.raw_data["commit"]["author"]["name"]
                if commit_author != user_login:
                    continue

            yield commit
