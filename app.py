import os

from dotenv import load_dotenv

import auth
import utils
import dto

load_dotenv()


def main():
    g = auth.get_github_by_access_token(os.getenv("ACCESS_TOKEN_GITHUB"))

    user = g.get_user()
    total_stats = dto.CommitStat()

    for commit in utils.get_all_commits(
        user_login=user.login, user_repos=user.get_repos()
    ):
        total_stats += utils.analyse_files_from_commit(commit.raw_data["files"])

    g.close()

    print(total_stats)


if __name__ == "__main__":
    main()
