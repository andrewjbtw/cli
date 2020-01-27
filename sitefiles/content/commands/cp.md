---
layout: page
title: cp
date: 2020-01-27
category: commands
tags: copying, writing
status: draft
---

**cp** copies files. With the right options, it will also copy directories.

The simplest **cp** command is:

```bash
$ cp source.txt copy.txt
```

As you would expect, this will create a file in the current directory called *copy.txt* that is a copy of the file called *source.txt*. 

### What is a copy?

As far as the default settings are concerned, a copy of a file is a copy of the content of the file. This does not include attributes, like the date. There are options that will copy attributes, but by default **cp** will use whatever is the default for your system.

```bash
practice@cli: ls -l
total 8
-rw-rw-r-- 1 andrew andrew 11 Jan 27 08:29 copy.txt
-rw-rw-r-- 1 andrew andrew 11 Jan 27 08:17 source.txt
```
In the case above, *source.txt* and *copy.txt* have the same content but *copy.txt* has a later date, the date that I copied it. 

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