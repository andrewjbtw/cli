---
title: cd
date: 2019-05-22
category: commands
---

**cd** changes the directory. Simple, right?

**cd** may come closer to the classical Unix ideal of doing one thing and doing it well than any other command that does more than just output information. 

It's pretty straightforward; let's change a directory!:[^1]

```bash
$ pwd
/home/user/
$ cd destination
$ pwd
/home/user/destination
```

Nevertheless, I've found a few things worth noting.

#### Running cd without specifying a directory ####

If you don't supply a directory, cd will default to changing into the logged in user's home directory:

```bash
$ pwd
/home/user/example
$ cd
$ pwd
/home/user
```

#### Shortcut to previous directory ####

There's a neat shortcut that will let you jump back to the last directory you came from. Just type a '-' after **cd**.

```bash
$ pwd # show current directory
/home/user/example/of/nested/path
$ cd # cd by itself jumps to the home directory
$ pwd # confirm change to home directory
/home/user
$ cd - # jump back to previous directory
/home/user/example/of/nested/path
$ pwd
/home/user/example/of/nested/path
$ cd - # jump back to home directory again
/home/user
$ pwd
/home/user
```
You can see that repeatedly typing 'cd -' will let you toggle between two directories repeatedly, which comes in handy if you're doing things like comparing or copying files between those directories.

Also note that in the example above it wasn't strictly necessary for me to check the current working directory with **pwd** after running 'cd -' because the command itself output the path of the directory it changed into. Normally, **cd** doesn't output anything if it doesn't run into an error. In this case, it must be showing output because the '-' is being expanded like a variable and it's helpful to show the user what it's being expanded to.

It turns out that the value represented by the '-' is stored in a variable named "OLDPWD". I learned this because if you type 'cd -' right after opening a new shell and before changing the directory, bash will tell you that the variable has not yet been set.

```bash
$ cd - # pretend this is the first command you ran in a new shell
bash: cd: OLDPWD not set
```

#### Using cd in a script ####

You can change the directory inside a script, but this can be risky because if the target directory you want to change into doesn't exist or the script does not have the permissions to access it, the script could just continue running. But instead of running the commands on the directory it was supposed to change into, it will run on the current one.

This could result in a disaster if the script was supposed to delete files in the target directory and instead deletes them in the current one.

To guard against this, you can use a conditional in the line where the script changes directory, such as:

```bash
cd target || exit
```
Conditionals and error handling are subjects for another post, but in case it's not clear the above example says basically: "change directory to target, but if that fails, exit the script." This at least can limit the potential damage resulting from a failed **cd**.

[^1]: Here I'm using **pwd** to show the current directory. See the **pwd** [notes]({filename}/commands/pwd.md "notes on using the command line post for pwd"), if you're not familiar with that command.