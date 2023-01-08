---
layout: post
title: for
date: 2022-12-17
category: commands
tags: looping
status: draft
---

```bash
limit=10
for ((i=1; i <= "$limit" ; i++)) ; do
	echo "$i"
done
```