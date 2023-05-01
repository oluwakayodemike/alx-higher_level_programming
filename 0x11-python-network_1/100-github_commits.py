#!/usr/bin/python3
"""
Retrieves the 10 most recent commits from the GitHub repository
specified by the given owner and repo names,
and prints each commit's SHA and author name to the console
in reverse chronological order.
Args:
- repo (str): The name of the repository to retrieve commits from.
- owner (str): The username or organization that owns the repository.
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author))
