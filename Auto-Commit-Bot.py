import os
import random
import string
import time
from datetime import datetime
from git import Repo
import argparse

def get_config():
    parser = argparse.ArgumentParser(description="Automate GitHub PR creation with random commits.")
    parser.add_argument('--github-username', required=True, help='GitHub username')
    parser.add_argument('--repo-name', required=True, help='Repository name')
    parser.add_argument('--local-path', required=True, help='Local repository path')
    parser.add_argument('--branch', default='main', help='Target branch (default: main)')
    parser.add_argument('--target-file', default='auto_file.txt', help='File to append sentences to')
    parser.add_argument('--min-prs', type=int, default=10, help='Minimum number of PRs per run')
    parser.add_argument('--max-prs', type=int, default=15, help='Maximum number of PRs per run')

    args = parser.parse_args()

    config = {
        "GITHUB_USERNAME": args.github_username,
        "GITHUB_TOKEN": os.environ.get("GITHUB_TOKEN"),
        "REPO_NAME": args.repo_name,
        "LOCAL_REPO_PATH": args.local_path,
        "DEFAULT_BRANCH": args.branch,
        "TARGET_FILE": args.target_file,
        "NUM_PRS_PER_DAY": random.randint(args.min_prs, args.max_prs),
    }

    if not config["GITHUB_TOKEN"]:
        raise ValueError("GITHUB_TOKEN must be set as an environment variable.")
    
    return config


WORDS = [
    "autonomous", "bot", "generates", "commits", "repository", "pull",
    "request", "GitHub", "automated", "system", "daily", "random",
    "sentence", "python", "script", "workflow", "branch", "feature",
    "test", "integration", "automation", "commit", "push", "version",
    "control", "branching", "merge", "collaboration", "cloud", "ci/cd",
    "deployment", "algorithm", "performance", "debugging", "code", "quality",
    "container", "docker", "dockerfile", "kubernetes", "pipeline", "monitoring",
    "data", "processing", "ai", "machine", "learning", "deep", "neural",
    "network", "training", "model", "optimization", "analytics", "metrics",
    "refactor", "repository", "pull-request", "issue", "feature-branch", "git",
    "merge-conflict", "collaborate", "deploy", "cloud", "api", "endpoint", 
    "server", "networking", "containerization", "orchestration", "load-balancer", 
    "scalability", "database", "sql", "nosql", "storage", "backend", "frontend", 
    "ui", "ux", "react", "angular", "vue", "typescript", "html", "css", "javascript", 
    "responsive", "mobile", "cross-platform", "versioning", "testing", "unit", 
    "integration", "functional", "acceptance", "test-driven", "devops", "agile", 
    "scrum", "project", "management", "documentation", "sprint", "iteration", "backlog", 
    "feature-request", "bug-fix", "release", "hotfix", "patch", "upgrade", "rollback",
    "monitoring", "logging", "error-handling", "validation", "security", "authentication",
    "authorization", "access", "control", "permissions", "encryption", "data-protection"
]


def generate_random_sentence():
    length = random.randint(5, 10)
    words = random.choices(WORDS, k=length)
    return ' '.join(words).capitalize() + '.\n'


def append_sentence_to_file(file_path):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(generate_random_sentence())


def run_commit_loop(config):
    repo = Repo(config["LOCAL_REPO_PATH"])
    origin = repo.remote(name='origin')
    file_path = os.path.join(config["LOCAL_REPO_PATH"], config["TARGET_FILE"])

    for i in range(config["NUM_PRS_PER_DAY"]):
        print(f"\nCommitting {i + 1}/{config['NUM_PRS_PER_DAY']}...")

        repo.git.checkout(config["DEFAULT_BRANCH"])
        repo.git.pull()

        append_sentence_to_file(file_path)

        repo.git.add(A=True)
        commit_message = f"Add random sentence {i + 1} - {datetime.now().strftime('%H:%M:%S')}"
        repo.index.commit(commit_message)
        origin.push()

        sleep_time = random.randint(0, 2)
        print(f"Sleeping {sleep_time}s before next commit...")
        time.sleep(sleep_time)


def main():
    config = get_config()
    run_commit_loop(config)


if __name__ == "__main__":
    main()
