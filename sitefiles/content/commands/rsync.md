---
layout: post
title: rsync
date: 2019-06-05
category: command
status: draft
---

post body text

[link text](link-URL "alt text")
rsync

Basic uses:

Copying files from a source directory to a target directory
Synchronizing files and directories

Simplest form of command:

rsync [source file] [target file or directory]


Example 1: 

Copy source file to target directory for first time:

Starting point

Directory tree:

```bash
.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 16:12]  target
```

Command

$ rsync source/example.txt target/

or 

$ rsync source/example.txt target

Result

Directory tree:

```bash
.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 16:15]  target
    `-- [  24 Aug  8 16:15]  example.txt
```

Discussion

Verbosity

rsync does not print any output by default. A number of options control how much information rsync outputs to the screen. Two useful options are:

-v [for verbose, outputs basic information about what's going on]
--itemize-changes [more detailed output of changes being made -- I generally only use this if '-v' is not detailed enough]

Human readability

When using the '-v' option, rsync prints file sizes in bytes. To print sizes in human readable terms, use this option:

    -h [outputs numbers in human readable format]

File last modified dates

By default, rsync does not copy the last modified date of the source file to the new file created in the target directory. This means that the new file will be given the date that you ran the rsync command. In the example above, the source file has a time of '16:06' but the target file has a time of '16:15' because that's when I ran the command.

This difference in times can become important if you want to synchronize files (or directories). By default, rsync uses file size and last modified date to determine whether two files are the same. If two files have different last modified dates, rsync may try to copy one to the other even if the filenames, file sizes, and file contents are the same.

In most situations, I want to preserve the last modified date when copying a file. Therefore, I use the option:

--times [preserves modification times]

Dry-runs

rsync has a dry-run option, which shows you what will happen if you run your command, without actually running it. This is especially useful when you are learning how to use rsync, or are setting up a complicated command. To use this option, simply include this in your list options:

--dry-run [perform a trial run with no changes made]

I especially recommend using '--dry-run' before running any command that will result in deleting files (this option to be covered later).

Which options are right for you? It depends on your needs. In general, when I'm copying a single file from a source to a target, as in this example, I want to preserve the modification times and I want some feedback from the terminal. So the command I would run is:

$ rsync -vh --times source/example.txt target/

Result

```bash
.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 17:44]  target
    `-- [  24 Aug  8 16:06]  example.txt
```

Note that in this case, the last modified times for 'example.txt' are now identical.


Example 2:

Synchronize source file with existing target file

Starting point

Directory tree:

```bash
.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 16:21]  target
    `-- [  43 Aug  8 16:21]  example.txt
```

File contents

$ cat source/example.txt
this is an example file

$ cat target/example.txt
this doesn't match the source example file

Command

[Note: from now on I'm going to include the 'v', 'h', and '--times' options in all examples.]

$ rsync -vh --times source/example.txt target/example.txt

Result

Directory tree:

```bash
.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 17:48]  target
    `-- [  24 Aug  8 16:06]  example.txt
```

File contents

$ cat target/example.txt # note that this is now the same as source/example.txt
this is an example file

Discussion

Note that the 'example.txt' file in the target directory now has the same size and last modified date as the 'example.txt' in the source directory.

Try running the same command again. Notice how rsync doesn't appear to do anything? This is because rsync only does 'work' when it determines that two files differ. Since the file sizes and modification times are the same, rsync does not consider these file to be different. There are other ways to make rsync compare two files, such as using checksums, but that will be covered later.

What happens if you don't preserve the modification time? Delete the target 'example' file and then run the command again without the '--times' option:

$ rsync -vh source/example.txt target/example.txt

What do you see? Try running the exact same command again. Notice how rsync appears to be copying the file again?

Example 3:

Copy source directory to target directory as a new subdirectory within the target

Starting point

Directory tree:

.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 17:10]  target

Command

$ rsync -r source target/

or 

$ rsync -r source target


Result

.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [8.0K Aug  8 17:16]  target
    `-- [4.0K Aug  8 17:16]  source
        `-- [  24 Aug  8 17:16]  example.txt

Notes:

rsync skips directories by default. To copy directories, you must use the '-r' option.

When working with directories, the trailing slash in the path to the source is extremely important. If you enter the source directory without the trailing slash, as in this example, the whole directory will be copied to the target (if new).

In the next example, we copy only the files from within the source directory to the target directory.

Example 4

Copy files from source directory into target directory

Starting point

Directory tree:

.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 17:10]  target

Command

$ rsync -r source/ target/

or 

$ rsync -r source/ target


Result

.
|-- [4.0K Aug  8 16:06]  source
|   `-- [  24 Aug  8 16:06]  example.txt
`-- [4.0K Aug  8 17:21]  target
    `-- [  24 Aug  8 17:21]  example.txt
