from github import Github
import os

token = os.environ["AGENT_TOKEN"]

g = Github(token)
user = g.get_user()

print("=" * 40)
print("GitHub Agent")
print("=" * 40)
print("User:", user.login)
print()

print("Repositories:")
for repo in user.get_repos():
    print(f"- {repo.full_name}")
