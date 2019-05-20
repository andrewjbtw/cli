Title: Introduction
URL:
save_as: index.html

## Plan of this site ##

This is a place for me to gather my notes on how to use the command line, by which I mostly mean tools that run in the bash shell on Linux. Over the years, I've looked up how to do many of the same things over and over again and I've gotten tired of it. So I'm writing them up here, hopefully in a way that will be useful to more than just me.

#### Organization ####

Posts on commands are organized by command name, with URLs formed according to the following pattern:

cli.suppliedtitle.org/commands/[command name]

Commands will also be listed under the category of "[commands](https://cli.suppliedtitle.org/category/commands "commands cateogry")" (see the sidebar for categories). If I'm successful keeping up with this site, new commands will be added regularly until I've covered the ones I use most. 

I haven't decided how I'm going to handle in-line linking between posts. For now, I'm just going to **bold** command names, and then come back and add links later. Most commands do not have posts yet.

Over time, I plan to write also about concepts, such as pipes, tab completion, and process substitution, which will be organized in another category. 

I will also be experimenting with assigning tags to each post, to provide other ways to browse that get outside of categorical hierarchies. 

Dates listed at the bottom of a post are the date it was last updated, not the date when it was first posted. I plan to update posts over time as I learn new functions.

#### Disclaimers ####

I will try to describe what I know as clearly as I can, but I can't promise comprehensive coverage. This is in many ways a record of my own learning, so I'm only going to cover commands and concepts I've actually used. And within that, only specific options and subcommands that I've used. 

Some posts might be not be much more than brief descriptions of what a command does, options that I've used, and syntax I want to remember. Others might have discussions of how to use a command for particular tasks, what other commands might be appropriate to the same task and how they compare with each other, and potential pitfalls that I've come to watch out for.

Finally, I've decided to launch this site without having fully worked out the design. I'm probably going to end up redesigning or reorganizing this site over time to make it look less like a blog and more like a reference resource. I also still need to work on the color scheme and images. But having had writer's block for many years, I've made a conscious decision to not let tweaking the theme get in the way of publishing.

#### A longer description of the site, if you're interested ####

Sometimes I have to remind myself how to double click and drag and drop. Over the past few years I've gotten so used to the command line that it's become my default way to get around the filesystem on a computer. Don't get me wrong, I use a graphical desktop environment 95% of the time, but I almost always have a terminal open alongside all my other applications. I don't see this as good or bad, just a way of working I've become accustomed to.

A lot of people see the command line as an "advanced" environment, something for experts and hackers and expert hackers. It can certainly be used that way: you can do some complex things from the command line that are difficult, sometimes impossible, to do any other way. But the reality for me is that a huge percentage of the time I'm in a terminal, I'm running commands like **cd** or **ls**, which combined are basically the equivalent of double clicking on a folder in a graphical file manager. I also launch graphical applications from the terminal, but again that's basically the equivalent of clicking on something. 

Why do I do this? I'm working on a longer blog post on that, but the short answer is that the command line can offer ways to do the equivalent of a lot of clicking without actually having to click. It offers ways to analyze files, process and manipulate data, and link together multiple tools in ways that can save you a lot of time, especially if what you're trying to do involves a lot of repetition. And in a modern desktop computer environment, you still have the option of opening up a graphical application if that's the best tool for the job. Unless you're on a server, you're probably not going to find yourself just staring at a dollar-sign symbol and a blinking cursor, wondering what you've gotten yourself into.

When you spend as much time on the command line as I've done, you start to build up a memory repository of commands and how to use them. But you also find yourself looking up the same things over and over again if you don't do them enough to memorize them. For a long time I've relied on a combination of my own command history, a few notes files here and there, saved or bookmarked pages on Q&A sites like Stack Overflow, some documentation sites and tech books, and just plain web searching when I need to as my command line "reference" methods.

This site is an attempt to bring some order to my command line usage in a way that I hope also helps others. Somewhere between a cookbook-style reference and a set of manual pages, I'm compiling my accumulated knowledge about the commands I've used at least once, and the options I've used most, into individual posts on each command. More idiosyncratic than comprehensive, I'm only going to cover what I've learned and use myself. In some cases the posts are short, sometimes not much more than pointers to more official documentation. In others, I discuss the affordances of the command's various options, why you might choose that command over a similar one or vice versa, common pitfalls I've run into, and more.

To give an example: the manual page for **rsync** is long, detailed, and some sections are just plain hard to understand. I'm not writing a new manual page in my [not yet published] **rsync** notes. Instead, I'm writing about when I might use **rsync** vs. another copying command like **cp**; what kinds of tasks I do where I prefer to use **rsync** if I can, which options I've found useful, why, and how they work; and common errors I've made that I'm trying to avoid making again by writing them down.

I've thought about whether to enable comments, but this is a static website and I don't feel comfortable hosting my own comments database or outsourcing comments to a third-part plugin that may or may not take good care of people's data. However, I welcome feedback: my goal is to learn and help others learn, so if I have something wrong I want to fix it. 

So what I'm doing for now is putting the code for this site in a [public repository on github](https://github.com/andrewjbtw/cli "notes on the command line github repository"). Please submit an issue if you have a suggestion or correction. I only ask for some patience as I'm fairly new to github and completely new to responding to issues. I can also be reached at the email on my contact page, if you'd prefer not to file a public issue.

*[Introduction last updated: 2019-05-20]*