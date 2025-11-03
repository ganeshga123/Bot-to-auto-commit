# 🔁 Auto Commit Bot

A Python script to automate daily commits to a GitHub repository by appending randomly generated sentences to a file.  
Ideal for testing GitHub workflows, CI/CD pipelines, or simulating activity in repositories.

---

## 🚀 Features

- Configurable number of commits per run
- Uses a random word bank to generate sentences
- Pushes changes directly to the default branch
- Secure token handling via environment variables
- Fully customizable via command-line arguments

---

## 📦 Requirements

- Python 3.7+
- GitPython

Install dependencies:

```bash
pip install gitpython
```

---

## 🔐 Setup

### 1. Clone Your Repository Locally

Make sure you have a local clone of the target GitHub repository.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### 2. Set Up Your GitHub Token

Export your GitHub Personal Access Token (classic or fine-grained with `repo` scope):

```bash
export GITHUB_TOKEN=your_github_token
```

> ⚠️ **Never hardcode your token inside scripts.**

---

## ⚙️ Usage

Run the script from the terminal with required arguments:

```bash
python auto_committer.py \
  --github-username GaneshGA \
  --repo-name Private-Experiment \
  --local-path "E:/auto-pr-bot/Private-Experiment" \
  --branch main \
  --target-file your_file.txt \
  --min-prs 10 \
  --max-prs 15
```

---

### 🧾 Arguments

| Argument           | Description                          | Required | Example                            |
|--------------------|--------------------------------------|----------|------------------------------------|
| `--github-username`| Your GitHub username                 | ✅        | `BhargavBJ`                        |
| `--repo-name`      | Repository name                      | ✅        | `Private-Experiment`               |
| `--local-path`     | Local path to your cloned repo       | ✅        | `E:/auto-pr-bot/Private-Experiment`|
| `--branch`         | Target branch (default: `main`)      | ❌        | `dev`                              |
| `--target-file`    | File to append random sentences      | ❌        | `sentences.txt`                    |
| `--min-prs`        | Minimum commits per run              | ❌        | `5`                                |
| `--max-prs`        | Maximum commits per run              | ❌        | `10`                               |

---

## 🧠 Example Output

Each commit will look like this:

```text
Add random sentence 3 - 14:52:08
```

Appended text in file:

```text
Container dockerfile deployment ai integration test.
```

---

## 📌 Notes

- This script **does not open pull requests** — it commits and pushes directly to the specified branch.
- Ideal for:
  - Testing bots and GitHub Actions
  - CI/CD pipeline simulations
  - GitHub activity heatmap boosting
- You can customize the `WORDS` list inside the script to fit any domain (e.g., tech, medical, finance, etc.)

---

## 📄 License

MIT License.  
Feel free to use, modify, and distribute.

---

## 🙋‍♂️ Author

**BhargavBJ**  
