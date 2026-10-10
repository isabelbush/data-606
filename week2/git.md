# Version Control Software

Software that track changes which allows you to:
- Revert changes to earlier versions
- Compare versions over time
- Branch off for safe experimentation

## Key concepts

- Repository = central hub which stores files, commits and history
- Directory = folder
- Working directory = current file or folder where changes are being made
- Staging = changes ready to be committed
- Commit = version or snapshot of changes at a specific point in time

# Shell

- OS/Kernal = brains of computer
- GUI = graphical user interface
- Shell = way to communicate with OS/Kernal without GUI

# Commands

- pwd = present working directory
- cd [folder_name]= change directory
- cd .. = return to previous directory
- cd ~ = return to home directory
- ls = list files in current directory
- ls -a = list files in current directory, including hidden ones
- clear = clear the terminal
- git status = show changed, staged and untracked files
- git init = initialise git repository in current folder
- git add [file_name.ext] = stage a specific file for commit
- git add . = stage all changes in current directory
- git commit -m "[message]" = commit staged changes to repository

# GitHub

Cloud platform accessed remotely via the internet that hosts repositories
- Collaboration
- Backup
- Visibility
- Extra functionality

## Commands

- git remote add origin [github link] = connect git to github
- git branch -M main = change name of core local branch from master to main
- git push -u origin main = send commits to github
- README = cover file