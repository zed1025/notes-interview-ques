# A Simple Git-GitHub Workflow
1. Go to this URL: https://github.com/raywenderlich/programmer-jokes
2. Click the Fork button
3. Copy the URL of the Forked repository
4. Clone the repository in your local system, `git clone https://github.com/zed1025/programmer-jokes.git`
5. Create a new branch `git branch my-joke`
6. See the list of all branched `git branch`
7. Switch to the newly created branch `git checkout my-joke`
8. Add the following lines to README.md. _Why couldn’t the confirmed bachelor use Git? Because he was afraid to commit!_
9. Flag the changes made to the file using `git add README.md`. This adds the file to the staging area. (Working Directory -> Staging Area -> Git Repository)
10. Next we want to commit the changes. Committing is the act of saying, “Yes, I have these changes ready, and I want to formally record those changes in my local copy of the repository.”
11. Commit the changes with the following command `git commit -m "Added a new joke"`
12. Git has formally recorded the changes. Now it's time to push these changes to the remote repository. `git push --set-upstream origin my-joke`
	1. **push** tells Git to put your local changes on the server
	2. **–-set-upstream** tells Git to form a tracking link for this branch between your local repository and the remote repository
	3. **origin** is a convention that references the remote repository
	4. **my-joke** is the branch you want to push
13. There’s one thing left to do - Signal to anyone else using this repository that you have something you’d like to integrate, or pull, into the remote repository. You do that with a  mechanism called a **pull request**.
14. Open your forked repository on GitHub
15. You'll see that you now have 2 branches(maybe more, but only the branch you created _my-jokes_ is important to you)
![[Pasted image 20220718221713.png]]
16. Click on the text saying "2 branches"
17. Here you will see the list of all the branches along with _my-jokes_. Click on the **New pull request** button next to _my-jokes_
![[Pasted image 20220718221853.png]]
18. Click that button and you’ll be taken to another page, where you can enter some details about your change. Enter Adds a real knee-slapper to the large text box to give some extra detail about the changes contained in this pull request, then click the Create pull request button
19. END

