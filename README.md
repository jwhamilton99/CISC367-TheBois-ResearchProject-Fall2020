# CISC367-TheBois-ResearchProject-Fall2020

[using git on windows](https://www.computerhope.com/issues/ch001927.htm)

## cloning the repo

in terminal (or command prompt for paul), make sure your working directory is where you want the repo: `cd <path/to/repo/parent/folder>`

then clone the repo: `git clone https://github.com/jwhamilton99/CISC367-TheBois-ResearchProject-Fall2020.git`

## doing work with git

when working, use your own branch. please. **do not work on the master branch**

to make a new branch: `git branch <branch name>`

to change to a branch: `git checkout <branch name>`
## committing

you need to stage files before you push them.

staging files: `git add .`

committing: `git commit -a -m "<commit message>"`

pushing: `git push`

## fetching

when someone else does work, pull the repo. you have to pull on a branch-by-branch basis, so you'll mostly be pulling the master branch when someone else is done their section

make sure you're in your branch: `git checkout <your-branch>`
to fetch: `git fetch`
merge into your branch: `git merge master`

## about the master branch

i will do everything with the master branch. **do not mess with the master branch please for the love of god**

*NOTE: all the commands above are done through terminal/command prompt with the working directory in the git repo. use `cd <path/to/repo>` to get there*

that should be it. come to me with any questions
