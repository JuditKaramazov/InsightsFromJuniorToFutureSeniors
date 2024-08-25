# Git Cheatsheets, vol.1: Essential Commands

Undoubtedly, mastering Git is _almost a requirement_ for all developers, especially once you start collaborating and having to share code with others. However, its functionality, purpose, and the main commands surrounding the previous two concepts may be perceived as blurry due to the many different possibilities it offers.

Are you scared of not _gitting gud_ enough? Fear not, fellow traveler; here, we will cover some of those relevant commands in the form of a beautiful, practical, and clear cheatsheet. Considering this, here are some of the key elements we'll try to define:

1. **Initial setup**.
2. **Configuration options**.
3. **Widely used commands**. 

Let's have a look at it!

<p align="center">
  <img src="../../images/git-very-gud.png" width="350px" alt="The git logo followed by the word 'gud'.">
</p>

> [!TIP]
> No matter if you are an **advanced git user** or someone **struggling with understanding this tool**, it's crucial to `understand why we are using certain commands instead of memorizing them`. For that purpose, you might find these resources helpful:
> 1. 👉 [shell.how](https://www.shell.how/) explains your Terminal's commands - **git ones included**!
> 2. 👉 [gitexplorer](https://gitexplorer.com/) will provide you with a **simple and interactive guide** to master git. **Write what you'd want to do or achieve**, and the site will **display the proper command** - ready to be copied and used!

---

## Table of Contents

1. [⚙️ Setup](#-setup)
2. [🏗️ Setup and init](#-setup-and-init)
3. [🌿 Branch and merge](#-branch-and-merge)
4. [📸 Stage and snapshot](#-stage-and-snapshot)
5. [🔍 Inspect and compare](#-inspect-and-compare)
6. [🛤️ Tracking path changes](#-tracking-path-changes)
7. [🙈 Ignoring patterns](#-ignoring-patterns)
8. [🔄 Share and update](#-share-and-update)
9. [📝 Rewrite history](#-rewrite-history)
10. [📦 Temporary commits](#-temporary-commits)
11. [🏛 License](#-license)

---

## ⚙️ Setup

Configure user information and global settings for Git:

| Command                                    | Description                                                                                                        |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| `git config --global user.name “[firstname lastname]”` | Sets an identifiable name for credit in version history reviews.                                       |
| `git config --global user.email “[valid-email]”`        | Associates an email address with each history marker.                                            |
| `git config --global color.ui auto`                    | Enables automatic command line coloring for Git, aiding in review.                                                   |

---

## 🏗️ Setup and init

Configure user information, initialize, and clone repositories:

| Command   | Description                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| `git init` | Initializes an existing directory as a Git repository.                                               |
| `git clone [url]` | Retrieves an entire repository from a hosted location via URL.                                        |

---

## 🌿 Branch and merge

Isolate work in branches, change context, and integrate changes:

| Command             | Description                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------|
| `git branch`        | Lists all branches, with an asterisk (*) indicating the currently active branch.                              |
| `git branch [branch-name]` | Creates a new branch at the current commit.                                                        |
| `git checkout`      | Switches to another branch and updates the working directory.                                |
| `git merge [branch]` | Merges the specified branch’s history into the current one.                                           |
| `git log`           | Displays all commits in the current branch’s history.                                                      |

---

## 📸 Stage and snapshot

Work with snapshots and the Git staging area, managing changes and commits:

| Command                | Description                                                                                          |
|------------------------|------------------------------------------------------------------------------------------------------|
| `git status`           | Displays modified files in the working directory, staged for the next commit.                           |
| `git add [file]`       | Adds a file to the staging area for the next commit.                                              |
| `git reset [file]`     | Unstages a file while retaining its changes in the working directory.                                  |
| `git diff`             | Shows the differences between the working directory and the staging area.                               |
| `git diff --staged`    | Shows the differences between the staging area and the last commit.                                     |
| `git commit -m “[descriptive message]”` | Commits the staged changes with a descriptive message.                                             |

---

## 🔍 Inspect and compare

Examine logs, diffs, and object information to understand changes:

| Command                     | Description                                                                                             |
|-----------------------------|---------------------------------------------------------------------------------------------------------|
| `git log`                   | Shows the commit history for the currently active branch.                                                  |
| `git log branchB..branchA`  | Shows the commits on branchA that are not on branchB.                                                       |
| `git log --follow [file]`   | Shows the commits that changed a file, even across renames.                                                   |
| `git diff branchB...branchA`| Shows the differences between branchA and branchB.                                               |
| `git show [SHA]`            | Displays the details of a specific commit.                                                           |

---

## 🛤️ Tracking path changes

Version files, remove, or move paths while tracking changes:

| Command                    | Description                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| `git rm [file]`            | Deletes the file from the project and stages its removal for commit.                                        |
| `git mv [existing-path] [new-path]` | Moves or renames a file and stages the change.                                                     |
| `git log --stat -M`        | Shows all commit logs with an indication of any paths that have moved.                                          |

---

## 🙈 Ignoring patterns

Prevent unintentional staging or committing of files with ignore patterns:

`logs/`
`.notes`
`pattern/`

Define patterns to ignore files when staging or committing changes.

| Command                                      | Description                                                                                     |
|----------------------------------------------|-------------------------------------------------------------------------------------------------|
| `git config --global core.excludesfile [file]` | Sets a system-wide ignore pattern for all local repositories.                                        |

---

## 🔄 Share and update

Retrieve updates, merge branches, and push or pull changes:

| Command                                    | Description                                                                                         |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `git remote add [alias] [url]`            | Adds a git URL as an alias.                                                                       |
| `git fetch [alias]`                       | Fetches down all branches from the specified Git remote.                                                 |
| `git merge [alias]/[branch]`              | Merges a remote branch into your current branch to bring it up to date.                             |
| `git push [alias] [branch]`               | Transmits local branch commits to the remote repository branch.                                     |
| `git pull`                                | Fetches and merges any commits from the tracking remote branch.                                       |

---

## 📝 Rewrite history

Rewrite branches, update commits, and manage commit history:

| Command                                  | Description                                                                                         |
|------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `git rebase [branch]`                    | Applies any commits of the current branch ahead of the specified one.                                 |
| `git reset --hard [commit]`              | Clears the staging area and rewrites the working tree from the specified commit.                      |

---

## 📦 Temporary commits

Temporarily store changes to switch branches or work on other tasks:

| Command                                  | Description                                                                                         |
|------------------------------------------|-----------------------------------------------------------------------------------------------------|
| `git stash`                     | Temporarily saves modified and staged changes.                                                            |
| `git stash list`                | Lists the stack-order of stashed file changes.                                                   |
| `git stash pop`                 | Applies and deletes the topmost stash.                                               |
| `git stash drop`                | Discards the topmost stash without applying changes.                                          |


**[⬆ Back to Index](#table-of-contents)**

**[🔙 Back to Cheatsheets Index](../../README.md)**

---

## 🏛 License

Although I was the one in charge of selecting and presenting all the previous examples, it is essential to highlight, mention, and praise other people's work, efforts, and time. The image introducing this brief chapter belongs to the user [binaryben](https://github.com/binaryben/gud), serving as an introduction to a project that, sadly, seems to be currently inactive. Nonetheless, thanks for the amazing logo! Keep on keeping on!

As for the rest, remember that you can make the Dinosaur extremely happy if you...

---

<h1 align="center">
  <a href="https://karamazfolio.xyz/"><img src="/images/karaMagister.png" width="200" height="200" alt="Original KaraMagister logo asset.">
</h1>
<h2 align="center">
  <a href="https://www.buymeacoffee.com/JuditKaramazov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 207px !important;" ></a>
</h2>
