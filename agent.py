from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

if not token:
    print("❌ GITHUB_TOKEN پیدا نشد.")
    exit()

g = Github(token)
user = g.get_user()

print(f"سلام {user.login}")
print("مخزن‌های شما:")

for repo in user.get_repos():
    print("-", repo.full_name)
