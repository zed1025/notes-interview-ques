- Git thinks about branches in terms of ours and theirs. “Ours” refers to the branch to which you’re merging back to, and “theirs” refers to the branch that you want to pull into “ours”.
![[Pasted image 20220719032743.png]]
## Three-way merges
- You might think that merging is really just taking two revisions, one on each branch, and mashing them together in a logical manner. This would be a two-way merge. However, a merge in Git actually uses three revisions to perform what is known as a three-way merge.
![[Pasted image 20220719033114.png]]
![[Pasted image 20220719033453.png]]

## Merging a branch
- We will merge changes on the clickbait branch to the master
- `git checkout clickbait`
- Execute the following command to see what’s been committed on this branch that you’ll want to merge back to master, `git log clickbait --not master`
	- This little gem is quite nice to keep on hand, as it tells you “what are the commits that are just in the clickbait branch, but not in master?”
- Recall that merging is the action of pulling in changes that have been done on another branch. In this case, you want to pull the changes from clickbait into the master branch. To do that, you’ll have to be on the master branch first.
- move to master `git checkout master`
- merge using `git merge clickbait`
![[Pasted image 20220719034317.png]]
## Fast-forward merge
![[Pasted image 20220719034539.png]]
If no other person had touched the original file since you picked it up and started working on it, there’s no real point in doing anything fancy, here. And while Git is far from lazy, it is terribly efficient and only does the work it absolutely needs to do to get the job done. This, in effect, is exactly what a fast-forward merge does.
To see this in action, you’ll create a branch off of master, make a commit, and then merge the branch back to master to see how a fast-forward merge works.
![[Screenshot 2022-07-19 034738.png]]
![[Pasted image 20220719034946.png]]
Here, all Git has done is move the HEAD label to your latest commit. And this makes sense; Git isn’t going to create a new commit if it doesn’t have to. It’s easier to just move the HEAD label along, since there’s nothing to merge in this case. And that’s why Git didn’t prompt you to enter a commit message in Vim for this fast-forward merge.
## Forcing merge commits
You can force Git to not treat this as a fast-forward merge, if you don’t want it to behave that way. For instance, you may be following a particular workflow in which you check that certain branches have been merged back to master before you build.
But if those branches resulted in a fast-forward merge, for all intents and purposes, it will look like those changes were done directly on master, which isn’t the case.
To force Git to create a merge commit when it doesn’t really need to, all you need to do is add the `--no-ff` option to the end of your merge command. The challenge for this chapter will let you create a fast-forward situation, and see the difference between a merge commit and a fast-forward merge.
## Key Points
- Merging combines work done on one branch with work done on another branch.
- Git performs three-way merges to combine content.
- Ours refers to the branch to which you want to pull changes into; theirs refers to the branch that has the changes you want to pull into ours.
- `git log <theirs> --not <ours>` shows you what commits are on the branch you want to merge, that aren’t in your branch already.
- `git merge <theirs>` merges the commits on the “theirs” branch into “our” branch.
- Git automatically creates a merge commit message for you, and lets you edit it before continuing with the merge.
- A fast-forward merge happens when there have been no changes to “ours” since you branched off “theirs”, and results in no merge commit being made.
- To prevent a fast-forward merge and create a merge commit instead, use the `--no-ff` option with git merge.