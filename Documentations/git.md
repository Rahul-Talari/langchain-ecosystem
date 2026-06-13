# GIT WORKFLOW - QUICK REFERENCE

---

## 1. SETUP *(Fresh Local Project)*

| Command | Description |
|---|---|
| `git init` | Initialize a new local Git repository |

---

## 2. REMOTE ORIGIN & BRANCH SETUP

| Command | Description |
|---|---|
| `git remote add origin <URL>` | Link local repo to remote repository |
| `git remote -v` | Verify remote origin URL is set correctly |
| `git branch -a` | List all branches (local + remote) `*` = current branch |
| `git switch -c <branch-name>` | Create and switch to a new branch |
| `git switch <branch-name>` | Switch to mentioned branch (recommended) |

---

## 3. WORKING WITH FILES

| Command | Description |
|---|---|
| `git status` | Show current changes and file states |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes ready for commit |

---

## 4. STAGING & COMMIT 🔁 *(Repeat for every change)*

| Command | Description |
|---|---|
| `git add .` | Stage all modified/new files |
| `git commit -m "your commit message"` | Commit staged changes with a message |
| `git log` | Verify commit history after each commit |

---

## 5. SYNC WITH REMOTE & PR FLOW

| Command | Description |
|---|---|
| `git pull origin <branch-name>` | Fetch + merge latest changes (before push in teams) |
| `git push -u origin <branch-name>` | Push branch and set upstream tracking |

> GitHub → New Pull Request → Assign Approver → Review → Approve → Merge into main

---

## 6. UNDO / FIX MISTAKES

| Command | Description |
|---|---|
| `git restore <file>` | Discard local (unstaged) changes in a file |
| `git restore --staged <file>` | Unstage a file (keep changes in working directory) |
| `git reset --soft HEAD~1` | Undo last commit but keep changes staged |
| `git reset --hard HEAD~1` | Undo last commit and discard all changes |

---

## SCENARIO 2: REPO ALREADY EXISTS *(Clone/Pull)*

| Command | Description |
|---|---|
| `git clone <URL>` | Clone full remote repository (first time) |
| `git pull origin <branch-name>` | Pull latest changes (already cloned) |