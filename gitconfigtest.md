# GIT GLOBAL CONFIGURATION

Run these two commands:

```
$ git config user.email
$ git config user.name
$
```

If these commands result in an empty return, then your `.gitconfig` file has yet to be set up.

With macOS you can use `$ open ~/` ...to open your home directory file in the Finder. Then use `cmd+shift+.` to toggle displaying invisible files in the Finder.

NOTE: With Windows in PowerShell you can use the `ls ~/` command to see a list of all the files including "invisible" ones which start with a period.

NOTE: With Linux, the `ls -al ~/` command will show the same.

Having forked, cloned, and made the first commit to a project, you may at first see a message like so:

```
$ git commit -m "gitconfig demo" -m "initial commit"
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

...and using `git log` you may see that the commit is associated to something other than what you registered to GitHub with, e.g.

```
commit 9e522d8b1c6675739f10d9c0fffb6da0daabd286 (HEAD -> master)
Author: Guest User <Guest@patricks-mbp.home>
Date:   Tue Oct 16 23:18:37 2018 -0400

    gitconfig demo

    initial commit

```

Pushing this commit to GitHub, you will be prompted for your username and password.

Look at the commit history on GitHub and you will see an anonymous icon.

Now let's globally set the username with the following command:

`$ git config --global user.name "pdktestlambda"`

You will see in the Finder window that there is now a `gitconfig` file in your home directory (or, if you run the `ls` commands on Win/Lin) Open up the ".gitconfig" file, it should look something like:
```
[user]
	name = pdktestlambda
```

(yes, that's a TAB before `name =`)

So let's try another commit:
```
Patricks-MBP:Graphs Guest$ git commit -am "glabal user.name set" -m "only global user.name, not the email yet"
[master a9fbab8] glabal user.name set
 Committer: pdktestlambda <Guest@patricks-mbp.home>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 23 insertions(+), 5 deletions(-)
 ```
(Yes I mis-spelled global ;) )

This time I was not prompted for my password - GitHub recognizes the username! ...but my commit still shows up on GitHub anonymously. So let's set the global e-mail setting:

`$ git config --global user.email "pakelika@mail.com"`

We can verify a couple of ways. In the `.gitconfig` file we should see

```
[user]
	name = pdktestlambda
	email = pakelika@mail.com
```

...or, we can use the `git config` commands (the `--global` flag is optional):
```
Patricks-MBP:Graphs Guest$ git config user.email
pakelika@mail.com
Patricks-MBP:Graphs Guest$ git config --global user.email
pakelika@mail.com
Patricks-MBP:Graphs Guest$ git config --global user.name
pdktestlambda
Patricks-MBP:Graphs Guest$ git config user.name
pdktestlambda
```

Now the Git commits are correctly associated with my username and email. On GitHub, the commits display with my user icon :+1:

***

# CONTRIBUTION GRAPH

So, now we have our commits accurately reflecting our registered account with GitHub, why aren't the commits I push up reflected in my contribution graph?

https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/#commit-was-made-in-a-fork

How can we get this work reflected in the chronological "heat map"?

Easy, de-forking!
