import os
from github import Github

token = os.environ["AGENT_TOKEN"]

g = Github(token)
user = g.get_user()

print(f"GitHub User: {user.login}")

print("\nRepositories:")
for repo in user.get_repos():
    print(f"- {repo.full_name}")
