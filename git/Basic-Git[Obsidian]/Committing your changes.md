## What is a commit?
It is essentially a snapshot of the particular state of the set of files in the repository at a point in time.
![[Pasted image 20220718224519.png]]
## Working trees and staging areas
The _working copy_ or _working tree_ or _working directory_ (language is great, there’s always more than one name for something) is the collection of project files on your  disk that you work with and modify directly.
Git thinks about the files in your working tree as being in three distinct states
- **unmodified**: Unmodified simply means that you haven’t changed this file since your last commit. 
- **modified**: Modified is simply the opposite of that: Git sees that you’ve modified this file in some fashion since your last commit. 
- **staged**: Essentially, as you work on bits and pieces of your project, you can mark a change, or set of changes, as “staged,” which is how you tell Git, “Hey, I want these changes to go into my next commit… but I might have some more changes for you, so just hold on to these changes for a bit.” You can add and remove changes from this staging area as you go about your work, and only commit that set of carefully curated changes to the repository when you’re good and ready.
_Notice above that I said, “Add and remove changes from the staging area,” not “Add 
and remove files from the staging area.” There’s a distinct difference_
- I added a new line "- [ ] Care and feeding of developers" to the file book_ideas.md
- Run the `git status` command
![[Pasted image 20220718225707.png]]
- Stage the changes using `git add books/book_ideas.md`
- Again run `git status`
![[Pasted image 20220718225907.png]]
- Git recognizes that you’ve now placed this change in the staging area. But you have another modification to make to this file that you forgot about.  Open books/book_ideas.md in your text editor and make the necessary changes. Then run `git status`
![[Pasted image 20220718230120.png]]
- What gives? Git now tells you that books/book_ideas.md is both staged and not staged? How can that be? _Remember that you’re staging changes here, not files_. Git understands this, and tells you that you have one change already staged for commit, and that you have one change that’s not yet been staged.
- To see this in detail, you can tell Git to show you what it sees as changed. Run `git diff`
![[Pasted image 20220718230428.png]]
- That looks pretty obtuse, but a `diff` is simply a compact way of showing you what’s changed between two files. In this case, Git is telling you that you’re comparing two versions of the same file — the version of the file in your working directory, and the  version of the file that you told Git to stage earlier with the `git add` command
- Add all the changes to the staging area with `git add .`That full stop (or period) character tells Git to add all changes to the staging area, both in this directory and all other subdirectories.
- Run `git diff` again. Uh, that’s interesting. `git diff` reports that nothing has changed. But if you think about it for a moment, that makes sense. `git diff` compares your _working tree to the staging area_. With `git add .`, you put everything from your working tree into the staging area, so there should be no differences between your working tree and staging.
- If you want to be really thorough (or if you don’t trust Git quite yet), you can ask Git to show you the differences that it’s staged for commit and the working tree with an extra option on the end of git diff.
![[Pasted image 20220718231044.png]]
- Commit changes `git commit -m ""`
## Adding directories
- create a new directory, `mkdir tutorials`
- check if the directory exists using `ls`
- It does. Now run `git diff`
- Er, that doesn’t seem right. Why can’t Git see your new directory? That’s by design, and it reflects the way that Git thinks about files and directories.
- At its core, Git really only knows about files, and nothing about directories. Git thinks about a file as “a string that points to an entity that Git can track”. If you think about this, it makes some sense: If a file can be uniquely referenced as the full path to the file, then tracking directories separately is quite redundant.
![[Pasted image 20220718232159.png]]
- The solution to making Git recognize a directory is clearly to put a file inside of it. But what if you don’t have anything yet to put here, or you want an empty directory to show up in everyone’s clone of this project?
- **The solution is to use a placeholder file. The usual convention is to create a hidden, zero-byte .keep file inside the directory you want Git to “see.”** Add this file using `touch tutorials/.keep`
- _The touch command was originally designed to set and modify the “modified” and “accessed” times of existing files. But one of the nice features of touch is that, if a specified file doesn’t exist, touch will automatically create the file for you._
- On running `git diff` now, you can see that git now recognizes the directory created.
- Add the changes to the staging area using `git add tutorials/\*`. While you could have just used `git add .` as before to add all files, this form of git add is a nice way to only add the files in a particular directory or subdirectory. In this case, you’re telling Git to stage all files underneath the tutorials directory. Add a commit.
## Looking at git log
- see the entire commit history, `git log`. (Use `Space` to navigate if there are a lot of commits, and `Esc` to exit.)
- To see every detail of your commits use, `git log -p`
- More on this in [[Git log and history]]
## Key Points
- A commit is essentially a snapshot of the particular state of the set of files in the 
repository at a point in time.
- The working tree is the collection of project files that you work with directly.
- `git status` shows you the current state of your working tree.
- Git thinks about the files in your working tree as being in three distinct states: _unmodified_, _modified_ and _staged_.
- `git add <filename>` lets you add changes from your working tree to the staging area.
- `git add .` adds all changes in the current directory and its subdirectories.
- `git add <directoryname>/\*` lets you add all changes in a specified directory.
- `git diff` shows you the difference between your working tree and the staging area.
- `git diff --staged `shows you the difference between your staging area and the last commit to the repository.
- `git commit` commits all changes in the staging area and opens Vim so you can add a commit message.
- `git commit -m "<your message here>"` commits your staged changes and includes a message without having to go through Vim.
- `git log` shows you the basic commit history of your repository.
- `git log -p` shows the commit history of your repository with the corresponding diffs.
- END