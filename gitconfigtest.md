Patricks-MBP:Graphs Guest$ git config user.email
Patricks-MBP:Graphs Guest$ git config user.name
Patricks-MBP:Graphs Guest$

If these two `git config` commands result in an empty return, then your `.gitconfig` file has yet to be set up.

With macOS you can use
Patricks-MBP:Graphs Guest$ open ~/

...to open your home directory file. Then use `cmd+shift+.` to see invisible files in the Finder.

With Windows in PowerShell you can use the `ls ~/` command to see a list of all the files inclduing "invisible" ones which start with a period.

With Linux, the `ls -al ~/` command will show the same.

Having made a commit to a project, you may at first see a message like so:

```
Patricks-MBP:Graphs Guest$ git commit -m "gitconfig demo" -m "initial commit"
[master 9e522d8] gitconfig demo
 Committer: Guest User <Guest@patricks-mbp.home>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 14 insertions(+)
 create mode 100644 gitconfigtest.md
 ```

...and using `git log` you may see that the commit is associated to something other than what you registered to github with, e.g.

```
commit 9e522d8b1c6675739f10d9c0fffb6da0daabd286 (HEAD -> master)
Author: Guest User <Guest@patricks-mbp.home>
Date:   Tue Oct 16 23:18:37 2018 -0400

    gitconfig demo

    initial commit

```
