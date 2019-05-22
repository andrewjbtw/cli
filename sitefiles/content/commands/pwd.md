---
title: pwd
date: 2019-05-22
category: commands
tags: getting oriented
---

**pwd** **p**rints the **w**orking **d**irectory.

It's a pretty simple command, but very useful because it's not always easy to tell where you are in the shell. I usually put directory information in my shell prompt, like so:

```bash
user@example:~/example$ 
```

The current directory in this example is shown in the text between the ':' and the "$". This shows that I'm in the "example" directory, which is a subdirectory inside the home directory for the logged in user.[^1] 

Not all shells will be set to show the path like that, however. My setting for the prompt is pretty close to the default on Ubuntu, but there are other distributions that use a different setting. You can customize your prompt, but sometimes it's not worth it, and you can just use **pwd** if you lose track of where you are.

The other feature of **pwd** is that it prints the working directory without any shorthands like the tilde, which can make it easier to process if you're redirecting the output.

```bash
user@example:~/example$ pwd
/home/user/example
```

One more note: there is a shell variable called "PWD" whose value is the current directory. 

```bash
user@example:~/example$ echo "$PWD"
/home/user/example
```
I don't really have an opinion at this point on when to use the **pwd** command or the PWD variable.

[^1]: Remember that in bash the tilde by itself is a kind of shorthand referring to the logged in user's home directory. Technically, this is called "[tilde expansion](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html "bash manual section on tilde expansion")" and covers more than just the tilde by itself.