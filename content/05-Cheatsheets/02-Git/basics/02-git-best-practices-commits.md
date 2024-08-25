# Best Practices: Commits

---

## Table of Contents

1. [🚪 Introduction](#-introduction) 
  - [💡 Good commits](#-good-commits)
  - [⏳ Quality equals time saver](#-quality-equals-time-saver)
2. [🫵 Use imperative mood](#-use-imperative-mood)
3. [❌ Avoid periods and ellipses](#-avoid-periods-and-ellipses)
4. [🔍 Limit the length to 50 characters](#-limit-the-length-to-50-characters)
5. [📒 Mention the issue number](#-mention-the-issue-number)
6. [📝 Provide additional context in the body](#-provide-additional-context-in-the-body)
7. [🏷️ Use prefixes for semantic commits](#-use-prefixes-for-semantic-commits)
8. [🛠️ Consider using commit utilities](#-consider-using-commit-utilities)
9. [🧪 Test your work before committing](#-test-your-work-before-committing)
10. [🤝 Be consistent](#-be-consistent)
11. [🏛 License](#-license)

---

## 🚪 Introduction

<details>
<summary> &nbsp; <em>Click to show / hide</em></sup><br /></summary><br />

It is impossible to deny it: writing good commit messages is key in order to maintain a **readable**, **easily scannable**, and **understandable project history**. Traditionally, and just like we've explored in [previous Git and GitHub courses of our pseudo-book](/content/03-Courses/02-Git-GitHub/Introduction/Module-0-git-vs-github.md), a Git workflow will normally involve the following steps:

1. Working directory: **make changes** 🛠️
2. Staging directory: **stage changes** 📦
3. **Commit changes** to apply them to our **Git repository** 📝 

In this short cheatsheet, we'll explore some crucial rules allowing us to write a good commit message, as well as the reasons why doing so is so important.

> ⚠️ Remember that, in Git, a `commit` is a snapshot of your repository at a specific point in time!

### 💡 Good commits

Before we jump into some of the best practices for composing solid Git commit messages, let's insist again on an essential matter: `Git commits` are a way to **record the changes applied to a repository**. On the other hand, a `Git repository` is the **collection of files tracked in the .git folder of a project**.

Given these concepts, it might be helpful to imagine a commit as some sort of **checkpoint or savepoint for our projects**. Remember the times when you reached certain checkpoints while playing video games? What happened then was that our **progress was saved after completing a challenge**, progressing enough in a quest, or making a specific action, a mechanism ensuring that **the progress we achieved wouldn't be lost**. Similarly, a `Git commit` is usually performed _after_ a significant contribution is made to our project - the kind of progress we'd want to save at any cost.

<p align="center">
  <img src="../../images/pixel-checkpoint.png" width="100px" alt="A pixel art 'save' sign, from Dan the Man.">
</p>

The main difference with video games, however, is that **each time a developer performs a commit**, they’re given the option to **write** a **commit message**. `Git commit messages` are used to **explain the function** of the commit, and believe me when I say that, while understanding Git commands is critical, knowing how to write effective commit messages is equally valuable.

A well-constructed commit message will ensure that all collaborators can **understand both the history and the reasoning behind** the changes - and this fact might affect even **the future you**, as working collaboratively, or simply participating in different projects, makes it necessary to keep track of **what has been done and why**.

### ⏳ Quality equals time saver

Just like it happens in every single aspect of life, applying the best practices will help **improve your ability to navigate your project's history**, **understand changes**, and **provide useful direction** for the future of the project. From this perspective, writing comprehensive and intuitive commit messages doesn't have to be tedious or unreasonably time-consuming; far the contrary, it will **help you save time**.

Clear, informative commit messages **reduce the need for extensive code analysis** and **enable efficient collaboration** among team members. Here's a wrap-up:

|                                  | **Reasoning**                                                                                                                                                              |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Navigating history** 🧭                                                | Clear commit messages act as signposts along the project's timeline, facilitating quick navigation and understanding of past changes.                                      |
| **Understanding changes** ✨                                             | Descriptive commit messages provide context for each change, enabling developers to grasp the purpose and scope of modifications without extensive code analysis.        |
| **Providing direction** 🛣️                                               | Commit messages serve as documentation for future contributors, guiding them through past decisions and helping them align their work with the project's goals and vision. |


Always keep in mind the time saved by future developers who can quickly understand and build upon your work without the need for extensive reverse engineering or guesswork, guys! This idea will **definitely make you a better developer**.

Now, let's see some of the rules that will turn our commit messages into top-tier ones!

</details>

---

## 🫵 Use imperative mood

Start the commit message using the `imperative` (this is, verbs that express an **order**, **request**, **instruction**, or **advice**):

```
- Add, 
- Change, 
- Fix, 
- Remove, etc.
```

Don't be scared of sounding way too abrupt or mean when using the imperative mood. Although it might feel tempting to use the past or present tenses instead ( ❌ _Fixes bug_, _Fixed bug_), we should **describe our changes as if we were giving instructions to the versioning system**. If you think of it, this convention **matches up with commit messages
generated by commands**, like `git merge` and `git revert` - and that's for a reason!

In order to give you widely-used examples:

- `Add` indicates adding a new file.
- `Change` signifies modifying an existing file. 
- `Fix` denotes fixing a bug.

In practice, your commits should look like this:

- `Add a new search feature`
- `Change the background color of the header`
- `Fix broken links in the documentation`
- `Refactor the authentication module`

---

## ❌ Avoid periods and ellipses

Avoid using periods or ellipses in your commit messages; if anything, stick with commas only when needed, but that's all. Remember that **each character counts when creating a good commit message**, so don't waste them on unnecessary punctuation!

Example:

- ❌ `git commit -m "Add new search feature."`
- ❌ `git commit -m "Fix a problem with the topbar..."`
- ✅ `git commit -m "Change the default system color"`

Also, keep in mind what follows:

1. Our initial message translates into the commit's title.
2. Linguistically speaking, titles never finish with a period.
3. The commits generated by GitHub never include period (`.`).
3. The commits generated by GitHub never include ellipses (`...`).

---

## 🔍 Limit the length to 50 characters

Keep your commit message **short and concise** - ideally under 50 characters. If you feel there's a lot to explain, it's quite likely that **you are doing quite a lot** - even more than necessary. Question time: **Can you split the task into different commits**? If so, do not hesitate and do it. It's always better to **focus on logical chunks**.

Then, ensure the message is clear, direct, and accurately reflects the changes made.

Example:

- ❌ `git commit -m "Add new search feature and change typography to improve performance"`
- ✅ `git commit -m "Add new search feature"`
- ✅ `git commit -m "Change typography to improve performance"`

---

## 📒 Mention the issue number

If you are using an **issue tracker** like [Jira](https://www.atlassian.com/software/jira) or [GitHub](https://github.com/), please, **remember to reference the issue number in the commit message**, as it creates a clear connection between the commit and the associated task.

As an example, let's check some of the most common scenarios:

- ❌ `Improve UI`
- ✅ `Close issue #232: Update CSS styles for better UI consistency`
- ✅ `Fix page loading bug on mobile devices, closes #233`
- ✅ `#435 Fix SSO front yml file`

In the end, you'll have to **adjust to the rules and conventions followed by your team**. Whatever you do and independently of their specific preferences, always make sure to keep things as clear, accessible, and organized as possible.

---

## 📝 Provide additional context in the body

Sometimes, you need to **provide more context for your commit**. Instead of cluttering the commit summary, add all the necessary information to the commit body.

There are two ways to achieve it:

1. You can use `git commit -m "Add summary of commit" -m "This is a message to add more context."`
2. However, it is better to use `git commit`.

Thanks to the last example, you'll be able to directly open an editor, and then add a commit message.

---

## 🏷️ Use prefixes for semantic commits

As a project grows, maintaining a readable history becomes crucial. Use **prefixes to add more meaning to your commits**, also known as `semantic commits`:

`<tipo-de-commit>[scope]: <descripcion>`

Example:

- `feat: add new search feature`
- `fix: resolve issue with login form validation`

If you are working with multi-package monorepositories, you can also **include information about the package affected by the commit**. This is known as the `scope`, and it would follow this format:

- `feat(backend): add filter for cars`
- `fix(authentication): resolve issue with login form validation`

If you are curious about some other **prefixes**, here you'll find some of them:

| Prefix   | Description                                                            |
|----------|------------------------------------------------------------------------|
| `feat`     | A new feature for the user.                                            |
| `fix`      | Fixes a bug that affects the user.                                     |
| `perf`     | Changes that improve site performance.                                 |
| `build`    | Changes in the build system, deployment tasks, or installation.         |
| `ci`       | Changes in continuous integration.                                     |
| `docs`     | Changes in documentation.                                               |
| `refactor` | Code refactoring, such as variable or function name changes.            |
| `style`    | Changes in formatting, tabs, spaces, or semicolons, etc. They do not affect the user. |
| `test`     | Adds tests or refactors an existing one.                                |

---

## 🛠️ Consider using commit utilities

You can use tools like [Husky](https://typicode.github.io/husky/) to **run scripts or commands before performing different actions** on the repository. For instance, you can run tests before pushing changes to your remote repository.

Example with Husky:

```bash
# Install dependencies
npm install husky --save-dev
npx husky install

# Initiate Husky in your repository
npm set-script prepare "husky install"
npm run prepare

# Create a hook to run tests before commit
npx husky add .husky/pre-push "npm test"
git add .husky/pre-push

git commit -m "Keep calm and commit"
git push -u origin master # tests will run before pushing
```

With `commitlint`, on the other hand, you can ensure that commits are **semantic**, **readable**, and **follow a chosen convention**.

Example with `commitlint` installation:

```bash
# Install commitlint cli and conventional config
npm install --save-dev @commitlint/{config-conventional,cli}

# Add a hook to check the commit message
npx husky add .husky/commit-msg 'npx --no-install commitlint --edit "$1"'
```

> [!TIP]
> Use systems like `conventional-changelog` in order to read the CHANGELOG, **generate new versions**, or **publish packages**. Additionally, `commitizen` allows you to use a command-line interface to choose the commit type, removing the need for manual selection in the commit message.

---

## 🧪 Test your work before committing

Don't commit half-done work, and more importantly, resist the temptation of committing something without making sure it is complete, functional, and error-free.

We are _not machines_. Human errors are more than understandable, and I do not doubt you'll have to retake a task in order to improve its logic or make it better than it was when you first delivered it. However, `don't commit "just because"`. If it might be helpful, make sure to go through these steps before committing your changes:

1. **Split** a feature's implementation into logical chunks.
2. **Work** on them quickly yet efficiently.
3. Ask yourself if **each individual task** is **functional** and has been **completed**.
4. If the problem lies in the urge for a **clean working copy**, **use Git's "Stash" instead**.
5. **Test** everything thoroughly.

> ⚠️ Remember that having your code tested is even more important when it comes to sharing your code with others, guys!

---

## 🤝 Be consistent

In the end, these are pure conventions. Independently of the ones you'll finally adopt (or even discard), remember to `stay consistent` throughout your messages. A consistent commit history will always be **more readable**, **easier to follow**, and, of course, **more professional** than a chaotic mess of desperate messages.

> [!IMPORTANT] 
> Keep messages meaningful. Keep them clear. Keep them consistent. Do it for you, for the future you, for all the upcoming developers, colleagues, and co-workers!

---

**[⬆ Back to Index](#table-of-contents)**

**[🔙 Back to Cheatsheets Index](../../README.md)**

---

## 🏛 License

This crazy woman called `Judit Lázaro Moyano` is, as usual, the one in charge of writing, selecting, and presenting all the previous examples in the form of a... book, at this point? We could definitely say so. However, I consider it essential to highlight, mention, praise, and _love_ other people's work and effort. In this case, the image illustrating the nature of commits belongs to an action-platformer game called [Dan the Man](https://dan-the-man.fandom.com/wiki/Checkpoint), and it serves as a checkpoint saving the player's progress. Amazing style, in my opinion! Do not hesitate to give it a try!

As for the rest, remember that Judit is _very tired_ after writing so much, which means that you can make her (and the Dinosaur!) extremely happy and energetic if you...

---

<h1 align="center">
  <a href="https://karamazfolio.xyz/"><img src="/images/karaMagister.png" width="200" height="200" alt="Original KaraMagister logo asset.">
</h1>
<h2 align="center">
  <a href="https://www.buymeacoffee.com/JuditKaramazov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 207px !important;" ></a>
</h2>
