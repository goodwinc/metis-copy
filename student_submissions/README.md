# Student Submissions Folder

## The following will be submitted in this folder:  
* Challenges
* Investigations
* Pair Programming (optional)
* Projects

## How PRs work

The way these work is that you pick a branch on your personal repo. My personal repo name is  `sophiaray/nyc17_ds13`. I can choose the master branch on this repo or create a specific one for the merge, like `proj-2-branch`. The merge happens between the head of my branch and the head of our class repo's master branch (`thisismetis/nyc17_ds13: master`).  

When you go to "new pull request" and select the branch you want to merge, github shows you a summary of your changes, including which files you are changing:

![](.images/compare.png)

This page tells me that in this PR I'm making changes to the class lecture and adding a data file.

## The rules

The comparing changes page is what instructors will be looking at when they choose to reject or accept your PRs. We have the following rules for student PRs:
- Only change files in student_submissions
- Do not include data files (or other big files), e.g. `.pkl`, `.csv`, `.json`, etc.
- Do not change many files, roughly keep it under <20.

Hopefully these rules make sense. The course repo is for everyone, so we can't allow students to make changes to the lectures or resources that other students might need. And big files are a problem because then everyone has to store that on their personal hard drive. The rule about the number of files is just for us—we have to review your changes so asking us to look at dozens or more files is not a good use of our time.

You will see which files your PR affects every time you go to submit a new PR, so you will know in advance if your PR is going to break a rule.

## Fixing mistakes :no_good:
Okay, what if you broke a rule and need to fix it so that you can get your submission in? The document [git oops](/class_lectures/week01-benson/04-more_pandas/git-oops.md) covers how to do this from the command line. I'll go over a few other methods here.

All of these work by adding new commits to the branch you submitted the original PR on. When you update that branch, the PR is updated automatically, so the process to fixing these mistakes is just to add commits that fix them.

### Delete a few files :x:
Deleting files by hand is very easy through the github web interface. Navigate to the file you want to delete and github gives you a nice garbage can to throw it into:

![](.images/delete.png)

### Reverting changes to a few files :pencil:
If you changed something you shouldn't have, you can revert those changes in the web interface relatively easily. The short version: you'll need to copy the text from the previous version of the file and then paste it into the current version. From the PR webpage, you can go to the file you changed by clicking on the view button:
![](.images/view.png)
From there, you can navigate the file's history by clicking "history":
![](.images/history.png)
From there, you'll see a list of commits that affected the file. You can find the last commit  before you made changes:
![](.images/hash.png)
Click on that, then click on "view", and go to the "raw" view mode. Copy the raw text from the previous file.

Switch back to the branch you are using for your PR (in my case, it's proj-2-branch) by using the tree selector:
![](.images/branch.png)

Then you can edit the file (click on the pencil) and paste in the text from the previous version.

### Last resort :cold_sweat:
Those methods work if your problem is a small number of files but what if you have a whole lot of files that you want to take off your PR? If the command line methods in git oops aren't working for you, you can always just start over.

First, copy the contents of your repo somewhere safe (maybe in a folder synced to google drive or dropbox so you won't lose things). Then create a brand new fork from the `thisismetis/nyc_ds13` repo. Then you can make the changes you want to commit and submit a new PR.
