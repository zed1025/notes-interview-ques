## What is a commit?
- You probably think about your files primarily in terms of their content, their position inside the directory hierarchy, and their names. So when you think of a commit, you’re likely to think about the state of the files, their content and names at a particular point in time. And that’s correct, to a point
- Git also adds some more information to that “state of your files” concept in the form of metadata
- Git metadata includes such things like “when was this committed?” and “who committed this?”, but most importantly, it includes the concept of “where did this commit originate from?” — and that piece of information is known as the commit’s parent. 
- Git takes all that metadata, including a reference to this commit’s parent, and wraps that up with the state of your files as the commit. Git then hashes that collection of things using SHA1 to create an ID, or key, that is unique to that commit inside your repository.
## What is a branch?
**It’s simply a reference, or a label, to a commit in your repository. 
- And because you can refer to a commit in Git simply through its hash, you can see how creating branches is a terribly cheap operation. There’s no copying, no extra cloning, just Git saying “OK, your new branch is a label to commit 477e542”. Boom, done.
- As you make commits on your branch, that label for the branch gets moved forward and updated with the hash of each new commit. Again, all Git does is update that label, which is stored as a simple file in that hidden .git repository, as a really cheap operation.
- `git config --global init.defaultBranch main`. This sets the default branch name to main. This only affects new repositories that you create; it doesn’t change the default branch name of any existing repositories.
## How Git tracks branches
- `git branch testBranch` creates a new branch
![[Pasted image 20220719024433.png]]
- _.git/refs/heads/_ directory contains the files that point to all of your branches. 
## Switching to another branch
- `git branch` by itself only shows the local branches in your repository
![[Pasted image 20220719025232.png]]
- the remote only has one branch: `clickbait`
- To get this branch down to your machine, tell Git to start tracking it, and switch to this branch all in one action, execute the following command `git checkout --track origin/clickbait`
## Explaining origin
_origin_ is another one of those convenience conventions that Git uses. Just like master is the default name for the first branch created in your repository, _origin is the default alias for the location of the remote repository from where you cloned your local repository_.
- execute the following command to see where Git thinks origin lives `git remote -v`
- To see Git’s view of all local and remote branches now, execute the following command, `git branch --all -v`
## A shortcut for branch creation
- `git checkout --track origin/clickbait` can be replaced with `git checkout clickbait`. When you specify a branch name to git checkout, Git checks to see if there is a local branch that matches that name to switch to. If not, then it looks to the origin remote, and if it finds a branch on the remote matching that name, it assumes that is the branch you want, checks it out for you, and switches you to that branch.
- There’s also a shortcut command which solves the two-step problem of `git branch <branchname>` and `git checkout <branchname>`: `git checkout -b <branchname>`. 
## Key points
 - A commit in Git includes information about the state of the files in your repository, along with metadata such as the commit time, the commit creator, and the commit’s parent or parents.
- The hash of your commit becomes the unique ID, or key, to identify that particular commit in your repository.
- A branch in Git is simply a reference to a particular commit by way of its hash.
- `master` is simply a convenience convention, but has come to be accepted as the original branch of a repository. `main` is also another common convenience branch name in lieu of master.
- Use `git branch <branchname>` to create a branch.
- Use `git branch` to see all local branches.
- Use `git checkout <branchname> ` to switch to a local branch, or to checkout and track a remote branch.
- Use `git branch -d <branchname>` to delete a local branch.
- Use `git branch --all` to see all local and remote branches.
- `origin`, like master, is simply a convenience convention that is an alias for the URL of the remote repository.
- Use `git checkout -b <branchname>` to create and switch to a local branch in 
one fell swoop.
