from github import Github

from github import Auth


def get_github_by_access_token(token):
    auth = Auth.Token(token)
    return Github(auth=auth)
