### Module 1: Introduction to Version Control

---

Table of Contents
-----------------
* [📚 1. Understanding Version Control](#-1-understanding-version-control)
  * [🔄 What is version control?](#-what-is-version-control)
  * [🤔 Why do we need version control?](#-how-are-git-and-github-related)
  * [🌟 Benefits of version control systems (VCS)](#-benefits-of-version-control-systems-vcs)

---

## 📚 1. Understanding Version Control

### 🔄 What is version control?

`Version control` is a system that tracks changes to files over time; in other words, the term refers to the **process of saving various files or "versions" throughout the different stages of a project**. Since it maintains a **historical record** of modifications, it allows users to revert to previous versions if necessary. Essentially, this enables developers to keep track of what has been made and return to a previous phase if they decide they want to revert some changes, and it also provides a way to manage and collaborate on projects effectively.

Although it might sound slightly alien by now, it's way more simple than it seems: it is **a way for software developers to never lose any state of their code**. No one can accidentally delete someone else's work, no one can permanently overwrite code, and this way, progress is never lost.

One of our biggest fears when we initially get immersed into the programming universe is ruining or destroying what was previously there. "What if I touch something and the entire thing stops working?" Version control, however, **allows you to be more confident in making changes to the code**. Worst case scenario: Did you apply a change that messed something up? No worries, you can just **undo** it and **revert back to a working version** of your code!

<p align="center">
  <img src="../../images/version-control-explanation.png" width="450px" alt="Representation of the Git plus GitHub workflow.">
  <br>
    Diagram by <a href="https://www.simplilearn.com/tutorials/devops-tutorial/version-control">Ishan Gaba</a>
</p>

Given the previous diagram, let's see how version control makes these options available:

1. The `three workstations` represent **three different developers at three other locations**.
2. There is a `repository` (remember that we went through a brief introduction to them in [the previous module](Module-0-git-vs-github.md)) that acts as a `server`, as they are somehow the `home for our projects`. 
3. The three stations are using that repository either for the process of committing, either for updating their given tasks. 
4. All these **workstations will have their** `own, working copy`. At the same time, **all these workstations will save their source codes into a particular server repository**.
5. As we can see above, there may be a **large number of working stations using the same server/repository**.
6. This way, if any system breaks down, **the work won't stop**. Why? Because there will be a `copy of the code in the central repository`.

> [!NOTE]
> Version Control Systems (VCS) are also the ones in charge of telling you who made a change and when they did it - and keeping all of the members on the same page. A VCS keeps everything clearly organized and then backs up all versions of the program, averting the crisis of destroying weeks of progress, as we mentioned before.

---

### 🤔 Why do we need version control?

Version control is essential for multiple reasons. For example, it makes it **easier to resolve errors** and **fix other mistakes that might occur** during development. We can also **note changes in each version** to help any team members **stay up-to-date** on what's completed and what still needs to be accomplished.

Let's not forget that version control is defined as a `system that tracks the progress of code across the software development lifecycle and its multiple iterations`. Considering that this fact ensures the existence and proper record of every change complete with authorship, timestamp, and other details, such aid in managing changes should be reason enough to define version control as an indispensable tool.

Despite this perspective only, we could safely say that we need version control due to several other factors:

  - **Collaboration:** 
    - It enables **multiple people to work** on the same project simultaneously without conflicting changes.
  - **History tracking:** 
    - Users can see who made specific changes, when they were made, and why, providing **transparency and accountability**.*
  - **Experimentation:** 
    - Version control allows users to **experiment** with new features or ideas in a **controlled environment**, facilitating innovation.
  - **Backup and recovery:** 
    - By maintaining a comprehensive history of changes, version control serves as a **backup mechanism**, ensuring that data can be recovered in case of errors or data loss.*

> [!NOTE]
> Whenever a change is applied to the project, the version control system creates a `snapshot` of the **state of the project**. This `snapshot` contains the history of current changes, and it also includes the author, date, and written notes for the purpose of maintaining a record of each change. Thanks to this complete history, we can go back to previous versions!
---

### 🌟 Benefits of version control systems (VCS)

Although version control systems offer numerous advantages, let's highlight some of the most relevant ones in order to close this brief introduction in an organized and concise way:

|                           | Description                                                                                                            |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 🤝 **Improved collaboration**           | Teams work efficiently, sharing and reviewing code changes seamlessly.                                                 |
| 💬 **Communication through open channels** | Facilitates transparent communication within the team, leveraging version control features.                            |
| 💡 **Flexibility**                      | Developers can experiment and revert changes without compromising project integrity.                                    |
| 🔍 **Traceability**                     | Every change is documented, aiding understanding of the project's evolution and issue identification.                   |
| 🔄 **Streamline merging and branching** | Optimizes merging and branching processes for smoother collaboration and development.                                 |
| 💾 **Creation of regular, automated backups** | Automated backups ensure data integrity and protect against potential loss or corruption.                           |
| 🛡️ **Disaster recovery**                | Version control systems provide a safety net in case of data loss or system failures.                                    |


---

<h1 align="center">
  <a href="https://karamazfolio.xyz/"><img src="/images/karaMagister.png" width="200" height="200" alt="Original KaraMagister logo asset.">
</h1>
<h2 align="center">
  <a href="https://www.buymeacoffee.com/JuditKaramazov" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 207px !important;" ></a>
</h2> 
