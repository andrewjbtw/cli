---
title: md5sum
date: 2019-05-24
category: commands
tags: getting file info, checksums
---

**md5sum** is a tool that creates md5 checksums (or hashes, if that's your preferred term). 

#### Obligatory discliamer on the brokenness of md5 ####

Before saying anything else, I should note that the md5 algorithm is widely considered to be so broken at this point that you probably shouldn't use it if you have a choice of algorithms. "Broken" in this context means that it's possible to generate so-called hash collisions, where two files have the same md5 checksum. Since one of the principle uses of a checksum algorithm is to provide a way to uniquely identify files using unique hashes for each file, an algorithm that can't guarantee uniqueness isn't a particularly useful algorithm.

At the same time, if you're just checking against unintentional file corruption, or trying to identify potential duplicate files, md5 still has some usefulness. You might still run into a random hash collision in the wild, but for the most part md5 will function as intended. 

I'd still recommend finding an alternative, but I know there's software out there that offers only md5, and there's a reasonable chance that if you're picking up a list of checksums in an organization that's been using them a long time, you're going to see md5 and then have to decide whether to swap it out for something stronger or keep using it for compatibility.

In the fields that I've been working in, digital preservation in libraries, archives, and museums, many people are adopting algorithms like sha256 or sha512 for longer term storage. Fortunately, there are tools just like **md5sum** that use these stronger algorithms:

**sha256sum**<br>
**sha512sum**

And by "just like", I mean that the command line options are almost literally the same for those tools as they are for **md5sum**. So everything I write below applies to them too. For the moment, I'm not going to write separate notes for those commands, and instead just refer to this post for examples.

#### md5sum basics ####

It can take input from a number of sources, but most commonly

[link text](link-URL "alt text")