---
layout: page
title: cp
date: 2020-01-27
category: commands
tags: copying, writing
status: draft
---

**cp** copies files by default, and has options that will make it copy directories.

The simplest **cp** command is:

```bash
$ cp source.txt copy.txt
```

As you would expect, this will create a file in the current directory called *copy.txt* that is a copy of the file called *source.txt*.

If you try to copy a directory without using any options, you will get an error message:

```bash
$ cp dir1 dir2
cp: -r not specified; omitting directory 'dir1'
```

### What is a copy?

As far as the default settings are concerned, a copy of a file is a copy of the content of the file. This does not necessarily include the source file's attributes, such as its dates or permissions.

```bash
practice@cli: ls -l
total 8
-rw-rw-r-- 1 andrew andrew 11 Jan 27 08:29 copy.txt
-rw-rw-r-- 1 andrew andrew 11 Jan 27 08:17 source.txt
```
In the case above, *source.txt* and *copy.txt* have the same content but *copy.txt* was given the date of when the copy was created. 

In practice, there may be some attributes that cp does copy by default, but I've never looked into it in much detail. If there are attributes that you know you want to copy, it's best to select these options specifically.

### Copying all attributes

If you want to copy all of the attributes that `cp` can copy, use the `-a` or `--archive` option.

```bash
$ ls -l
total 8
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 copy.txt
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 source.txt
```

Note that this option is recursive, so it will copy entire directories too.

```bash
$ cp -a dir1 dir2
$ ls -l dir*

dir1:
total 8
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 copy.txt
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 source.txt

dir2:
total 8
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 copy.txt
-rw-rw-r-- 1 andrew andrew 2 Jun  4 12:47 source.txt

```


### Permissions issues

Be careful to make sure you have the requisite permissions to do the things you want to do with `cp`. You obviously can't copy files into locations where you don't have write permissions, but there are also situations to watch out for where `cp` will partially fail. In those situations you'll get an error message that usually describes what attributes couldn't be copied.

The most common problem I've run into is where I've wanted to preserve some attributes, but my permissions don't allow it. This happens to me most often when copying from one type of filesystem to another because the permissions schemes are often not compatible (i.e. copying from Linux/ext4 to Windows/NTFS hard drives). It also can come up when copying to or from shared or networked folders.

Note that a partial failure like this will generally still copy the content of the source file even if it fails to copy some attributes. If you get an error message after cp, it's best to read the message carefully and then check what happened to the files.

So if you want to copy a folder but don't care about the attributes, then I would use `cp -r` instead of `cp -a` if `cp -a` generates errors for some of the attributes it tries to copy.

### By default, **cp** will overwrite any file with the same name. There are options that will either warn you about overwriting or prevent you from overwriting, but it's a good idea to take care not to overwrite when you don't ean to.
2. 



You can give the copied file whatever name you want, and you can supply any path you want as long as those directories already exist and you have the permissions to write to them:

```bash
$ cp source.txt path/to/copy.txt
```

You can also take your source file from any path you can access. You're not limited to copying files in your current working directory. So the most generic 

```bash
$

[link text](link-URL "alt text")