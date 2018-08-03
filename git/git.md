# Summary of Git

## Overview
- Distributed rather than centralized (svn).

## A General process
- Create
```
git init [proj]
git clone
```
- setup in file .gitconfig
```
git config --list
git config -e [--global]
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"

git config --global push.default simple
```
- Add/remove files
```
git add file1 [file2] [folder] [.]
git rm ...
git mv src dst
```
- Check in codes
```
git commit -m [message]
git commit -a
git commit -v # show all difference
git commit --amend [file1] [file2]
```
- Branch
```
git branch # all branches
git branch -r # all remote branches
git branch -a # all local and remote

git branch [name] # create a branch, still stay in current branch
git checkout -b [branch]
git checkout [branch]
git branch --set-upstream [branch] [remote-branch]

git merge [branch] # merge a specific branch to current

git cherry-pick [commit]
# delete locally
git branch -d [branch-name]
# delete remote
git push origin --delete [branch-name]
git branch -dr [remote/branch]
```
- tag
```
git tag
git tag [tag]
git tag [tag] [commit]
git push origin :refs/tags/[tagName]
```
- check info
```
git status
git log [--stat]
git log -S [keyword]
git log --follow [file]
git blame [file] # difference between workspace and temporary
git diff HEAD
git diff [branch1] [branch2]
git show [commit]
```
- Remote synchronyze
```
git fetch [remote]
git remote [-v]
git remote show
git remote add [branch]
git pull [remote] [branch]
git push [remote] [branch]
git push [remote] --all
```
- Recall a change
```
git checkout [file]
git checkout [commit] [file]
git checkout .
git reset [file]
git reset --soft # work dir only
git reset --hard # both work and temp dir
git reset [commit]
git reset --hard [commit]
git stash
git stash pop
```