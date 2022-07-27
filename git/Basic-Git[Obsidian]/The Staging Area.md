## Why staging exists
It’s noble to think that that you’ll work on just one feature or bug at a time; that your working tree will only ever be populated with clean, fully documented code; that you’ll never have unnecessary files cluttering up your working tree; that the configuration of your development environment will always be in perfect sync with the rest of your team; and that you won’t follow any rabbit trails (or create a few of your own) while you’re investigating a bug.
Development is a messy process. What, in theory, should be a linear, cumulative construction of functionality in code, is more often than not a series of intertwining, non-linear threads of dead-end code, partly finished features, stubbed-out tests, collections of // TODO: comments in the code, and other things that are inherent to a human-driven and largely hand-crafted process.
Git was built to compensate for this messy, non-linear approach to development.
It’s possible to work on lots of things at once, and selectively choose what you want to stage and commit to the repository. The general philosophy is that a commit should be a logical collection of changes that make sense as a unit — not just “the latest collection of things I updated that may or may not be related.”
## Undoing staged changes
It’s quite common that you’ll change your mind about a particular set of staged changes, or you might even use something like git add . and then realize that there was something in there you didn’t quite want to stage.
- Make the following additions
	- create a new file in the books directory, named management_book_ideas.md, `touch books/management_book_ideas.md`
	- wait — the video production team pings you and urgently requests that you update the video content ideas file, since they’ve just found someone to create the “Getting started with Symbian” course, and, oh, could you also add, “Advanced MOS 6510 Programming” to the list? Open `notepad videos/content_ideas.md` and make the necessary changes
	- `git add .` to add all changes to staging area
	- Run `git status`
	![[Pasted image 20220718235952.png]]
	- Oh, crud. You accidentally added that empty books/management_book_ideas.md. You likely didn’t want to commit that file just yet, did you? Well, now you’re in a pickle. Now that something is in the staging area, how do you get rid of it?
	- The easiest way to do this is through `git reset`.
## git reset
- Execute the following command to remove the change to books/management_book_ideas.md from the staging area, `git reset HEAD books/management_book_ideas.md`
	- **HEAD** is simply a label that references the most recent commit.
- So, `git reset HEAD books/management_book_ideas.md`, in this context means “use HEAD as a reference point, restore the staging area to that point, but only restore any changes related to the books/management_book_ideas.md file.”
- Run the `git status` command
![[Pasted image 20220719000545.png]]
- Git is no longer tracking books/management_book_ideas.md, but it’s still tracking your changes to videos/content_ideas.md
- Commit the changes `git commit -m "Updates book ideas for Symbian and MOS 6510"`
![[Pasted image 20220719000706.png]]
## Moving ﬁles in Git
- create a new directory in the /ideas directory, `mkdir website`
- Move the file platform_ideas.md to this folder, do it manually using the mv command `mv videos/platform_ideas.md website`
- Execute `git status`
![[Pasted image 20220719001603.png]]
- Well, that’s a bit of a mess. Git thinks you’ve deleted a file that is being tracked, and it also thinks that you’ve added this website bit of nonsense. Why doesn’t it just see that you’ve moved the file?
	- Remember, Git knows nothing about directories: It only knows about full paths to files. Comparing the two snippets of your working tree below shows you exactly why git status reports what it does.
	![[Pasted image 20220719001750.png]]
- Seems like the brute force approach of `mv` isn’t what you want. _Git has a built-in mv command to move things “properly” for you_.
- Move the file back to where it was, `mv website/platform_ideas.md videos/`. Git will go back to the state it was previously(before the move)
- Execute `git mv videos/platform_ideas.md website/` and then `git status`
![[Pasted image 20220719002056.png]]
- Git sees the file as “renamed,” which makes sense, since Git thinks about files in terms of their full path. And Git has also staged that change for you. 
- Commit the changes `git commit -m "Moves platform ideas to website directory"`
- Your ideas project is now looking pretty ship-shape. But, to be honest, those live streaming(articles/live_streaming_ideas.md) ideas are pretty bad. Perhaps you should just get rid of them now before too many people see them.
## Deleting ﬁles in Git
- The impulse to just delete/move/rename files as you’d normally do on your filesystem is usually what puts Git into a tizzy, and it causes people to say they don’t “get” Git. But if you take the time to instruct Git on what to do, it usually takes care of things quite nicely for you.
- So — that live streaming ideas file has to go.
- Brute force way
	- Execute `rm articles/live_streaming_ideas.md` and then `git status`
	![[Pasted image 20220719002557.png]]
	- That’s not so bad. Git recognizes that you’ve deleted the file and is prompting you to stage it. `git add articles/live_streaming_ideas.md`
	![[Pasted image 20220719002715.png]]
	- Well, that was a bit of a roundabout way to do things. But just like `git mv`, you can use the `git rm` command to do this in one fell swoop.
- But to use `git rm` we have to go back to where we were
## Restoring deleted ﬁles
- Unstage the change to the live streaming ideas file `git reset HEAD articles/live_streaming_ideas.md`
![[Pasted image 20220719002955.png]]
- That removes that change from the staging area — but it doesn’t restore the file itself in your working tree. To do that, you’ll need to tell Git to retrieve the latest committed version of that file from the repository.
- Run `git checkout HEAD articles/live_streaming_ideas.md`
![[Pasted image 20220719004717.png]]
- Get rid of that file with the following command `git rm articles/live_streaming_ideas.md`
![[Pasted image 20220719004812.png]]
- commit changes `git commit -m "Removes terrible live streaming ideas"`
- add and commit the management_book_ideas.md file, `git add books/management_book_ideas.md`, `git commit -m "Adds all the good ideas about management"`
## If you delete a file by mistake
- say the file is books/management_book_ideas.md
- To restore it 
	- `git reset HEAD books/management_book_ideas.md`
	- `git checkout HEAD books/management_book_ideas.md`
## Key points
- The staging area lets you construct your next commit in a logical, structure fashion.
- `git reset HEAD <filename>` lets you restore your staging environment to the last commit state.
- Moving files around and deleting them from the filesystem, without notifying Git, will cause you grief.
- `git mv` moves files around and stages the change, all in one action.
- `git rm` removes files from your repository and stages the change, again, in one action.
- Restore deleted and staged files with `git reset HEAD <filename>` followed by `git checkout HEAD <filename>`
- END
