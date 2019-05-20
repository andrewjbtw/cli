---
layout: post
title: ls
date: 2019-05-20
category: commands
tags: getting file info
status: published
---

**ls** lists files (and folders, symlinks, etc) 

#### Basic usage ####

Run with no options, **ls** will list the files in the current directory, laid out in columns. The exact number of columns displayed depends on the width of the terminal window and the length of the filenames being listed. 

```bash
$ ls
01.txt  03.txt  05.txt
02.txt  04.txt  06.txt
```

To list files in a single column with no other detail, use the '-1' option:

```bash
$ ls -1
01.txt
02.txt
03.txt
04.txt
05.txt
06.txt
```

Note that when sending the output of **ls** (with no options) to a pipe, it outputs as if the '-1' option has been invoked, so it's not necessary to supply it in that situation. However, if you're thinking of parsing the output of **ls** in a pipe or a script, please see the warning section at the end of this post.

By default, **ls** does not list hidden files. Use the '-a' or '-A' options to list hidden files.

```bash
$ ls -a
.  ..  01.txt  02.txt  03.txt  04.txt  05.txt  06.txt  .this-is-a-hidden-file
```
The '-a' option includes '.' (current directory) and '..' (parent directory) in the list. Since these are a part of every directory listing, I don't find this particularly useful. It can also cause problems if you accidentally have a command process '..' when you don't want it to run on the parent directory. 

So I generally use the '-A' option to list files when I want to list hidden files, as it leaves '.' and '..' out.

```bash
$ ls -A
01.txt  02.txt  03.txt  04.txt  05.txt  06.txt  .this-is-a-hidden-file
```

#### Getting more details ####

Use the '-l' option to get a useful set of details, such as permissions, date modified, and size.

```bash
$ ls -l
total 20
-rw-r--r-- 1 user user 3 May 20 00:08 01.txt
-rw-r--r-- 1 user user 3 May 20 00:08 02.txt
-rw-r--r-- 1 user user 3 May 20 00:08 03.txt
-rw-r--r-- 1 user user 3 May 20 00:08 04.txt
-rw-r--r-- 1 user user 3 May 20 00:08 05.txt
-rw-r--r-- 1 user user 0 May 20 00:25 06.txt
```

One feature I've found useful in my digital preservation work has been the ability to list inodes with the '-i' option. This isn't the place for a detailed discussion of inodes, so I'll just say that inodes can help determine whether more than one filename actually refers to the same file, or if a file has been moved or renamed without having been changed.

```bash
$ ls -i1
total 20
8388743 01.txt
8388744 02.txt
8388745 03.txt
8388752 04.txt
8388755 05.txt
8388757 06.txt
```

The above example also shows you can combine options to **ls**, in this case using the '-i' and '-1' options, which I chose because I think it's easier to read this way. The numbers at the start of each line (except "total" obviously) are the inodes.

#### Shaping output ####

**ls** offers a few ways to format its output for easier reading, depending on what you're looking for.

For human-readable file sizes (i.e. 10K, 20M, 30G, etc.), use '-h'

```bash
$ ls -h # TODO: add example
```

To sort by modification time (newest first), combine '-l' and '-t':

```bash
$ ls -lt # TODO: add example
```

To sort by file size (largest first) combine '-l' and '-S':

```bash
$ ls -lS # TODO: add example
```

To list all directories below a particular directory, use '-R' (for "recursive"):

```bash
$ ls -R # TODO: add example
```

Note that if you type 'ls *[directory name]*', **ls** will output information about files in that directory. To get **ls** to output information about the directory itself, use the '-d' option:

```bash
$ ls directory # shows information about files in "directory"
$ ls -d directory # shows information about the directory "directory"
```

#### A way into the filesystem ###

Some of the power of **ls** comes not from what it can show you about a particular directory or group of files, but in how you can use it to get a picture of what's on your computer (or removable drive, or network share -- really, almost anything you can reach through the shell). Unlike many graphical file managers, which typically show you details only from the currently opened folder, you can use **ls** to get a picture of potentially any directory or file on your system by supplying a path on the command line.

Doing this requires understanding relative and absolute paths, which is a topic for another post. But the key is that you can supply any path to **ls**, which means you aren't restricted to listing files in or below the current directory you happen to be looking at.

Below are some examples of how you could use **ls** from any directory to view information about specific files in various locations. These commands could be typed from any directory you happen to be in at the time.

List files in the current directory whose names end with ".jpg":

```bash
$ ls *.jpg 
```

List files in your user's Pictures directory whose names end in ".jpg":

```bash
$ ls ~/Pictures/*.jpg 
```

Recursively output information about files and folders in your user's Documents folder:

```bash
$ ls -R -Alh ~/Documents # added options to list hidden files, show more details, and human readable sizes
```

This might not seem like a big deal, but it means that you can do things like list the files in another directory before deciding whether to change to that directory, without having to open another window to do it. Or you could use it to see whether you want to copy anything from your current directory to another directory, or vice versa. 

For me, typing **ls** and a path is like clicking on a folder in a file manager, but without having to actually click a bunch of times. And if what I see from **ls** leads me to think opening a file manager window and dragging and dropping files is my best course of action, I can still do that. The command line is not a trap; it's just another tool.

To be clear, **ls** is not at all unique in being able to process paths to other files and directories: being able to supply specific paths to commands is one of the main advantages of working from the command line. Not all commands support this, but many do. And since **ls** is fairly low-key in what it does - it does not edit files, for example - it's a good command to use to familiarize yourself with getting around a filesystem via path names.

#### Warning: think carefully about parsing the output of **ls** ####

**ls** is a deceptively simple command. It doesn't look like it's doing much at first, but work has gone into making its output human readable. For example, if you use the '-l' option a lot to get detailed information, you'll notice that it modifies how it displays the date depending on how long ago a file was last modified.

The trade-off is that what's human-readable isn't necessarily what's best for machine readability. A computer is going to be able to handle data better if it's consistently formatted, and an output that is slightly different depending on whether a file has been updated in the last few months, or uses spaces in its name, or whatever, is going to be difficult to parse in a script.

There are many descriptions of this problem online. Just search for "parsing ls" and you'll see this warning a lot. In fact, those warnings are why I've included this section in my notes. I didn't lose any data, but let's just say that I lost some hours to trying to parse **ls** before searching around and learning that there are other ways to do what I needed.

You might still be able to get what you need via parsing **ls** if you run it with no options, but if you're going to process a list of file names, most recommendations are to use a command like **find** or a feature like shell "globbing" to form the list of names. These strategies are more resilient against the problems caused by file names that include spaces or characters that have special meaning to the shell (a filename with a '\*' in it, for example). More detail on these methods will have to wait until I've written more notes for comparison.

#### to-dos: further posts or notes that will make this post more useful ####

1. overview of how to form paths, including shortcuts like typing "~" to refer to user's home directory
2. tab completion, which can make it easier to type long paths
2. **cd**
3. **find**
4. "globbing"
5. add link[s] to references on inodes, or write post about them