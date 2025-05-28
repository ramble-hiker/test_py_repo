# test_py_repo
Testing py repository

Share what you learned:
I have learned there are 2 main ways to use git.  From command line and from the GUI.  With both methods you use the online website to view repositories and affected changes (refresh if needed).

To use the GUI you download git desktop and use that to create and select repositories.  You can create or choose branches and you can open repositories into an editor (such as vscode).

Using command line (I recommend getting bash for windows) you first use "git init" to initialize a repository. Then use "git add" to stage files to be committed to the local repository.  Then you use "git commit" to commit changes to the local repository.  Then you use "git push" to push to the server for online storage.  

To maintain the integrity of the main file it is good to make a branch and work on that branch.  Then when it is correct you can push it to the online repository and then push the branch to the main repository for review by the main repository manager.

Any time you want a current copy of the main or branch repository it is important to fetch it from the server.

You can revert (undo changes while keeping a history) or if you are not working with a group you can reset (delete changes and history and return to a previous repo state).  

After a revert if you want to again affect the same changes it may be best to start with a different branch because I found issues in using the same rejected revert to push previously rejected changes back onto main.

I'm still learning but this is what I learned so far.