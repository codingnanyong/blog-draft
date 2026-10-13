---
title: "Codigdex #02 — Linux Paths and Files: Absolute and Relative Paths"
description: "Week 2 of the Codigdex series' Linux chapter. Telling apart absolute paths that start at / from relative paths measured from where you stand, observing how mkdir, cp, mv, rm, and find create, move, find, and delete files, and registering NO.007 Path Forager."
tags: [linux, codigdex, paths, files]
date: 2026-10-12
status: draft
---

# Codigdex #02 — Linux Paths and Files: Absolute and Relative Paths

![Codigdex #02 Linux — the explorer meets the Path Forager with a map at a fork in the Shell Cave](./images/thumbnail.en.v2.png)

Last observation confirmed that the shell is always standing somewhere in the filesystem. We asked where with `pwd`, looked around with `ls`, and moved with `cd`.

But just wandering around doesn't get much done. Sooner or later you have to create files, copy them, move them, find them, and delete them. And to do that, you first need to tell the shell exactly *where* that file is. A little deeper into the Shell Cave, a specimen appeared that was quietly moving files all over the cave.

![A wild Path Forager appears — Codigdex battle screen](./images/01-path-forager-encounter.en.png)

---

## Specimen info

- Dex number: NO.007 Path Forager
- Name: Paths and files — absolute/relative paths, `mkdir`, `cp`, `mv`, `rm`, `find`
- Classification: File explorer type
- Encounter rate: Very high (scripts, config files, CI logs — there's hardly anywhere paths don't show up)
- Danger level: ⚠️⚠️ (`rm` has no trash can, and `cp` and `mv` overwrite a file with the same name without asking)

---

## First impression

Meeting the Path Forager for the first time, these questions came up.

- Apparently `/home/lupi/notes` and `../notes` can be the same place — so when are they the same, and when aren't they?
- In a file explorer you just drag and drop. How do you tell "copy" from "move" in the shell?
- Can a file deleted in the shell be rescued from the trash?

Once again, I decided to sort out the questions before the commands.

---

## Observation 1 — a path is a file's address, and it has two starting points

The first thing I pinned down was what a **path** is. A path is the address of a file or directory in the filesystem tree, written as the route to it joined by `/`. And there are two ways to write that address, depending on where it starts.

![From /home/lupi/project, the absolute path /home/lupi/notes and relative path ../notes reach the same notes folder](./images/02-absolute-relative-paths.en.v2.png)

Say the tree for this observation looks like this.

```text
/
└── home
    └── lupi
        ├── todo.txt
        ├── notes
        └── project
            └── app.log
```

- **Absolute path**: an address written starting from the very top, `/` (the root). It always starts with `/`, like `/home/lupi/notes`, and points to the same place no matter where the shell is standing
- **Relative path**: an address written starting from the **working directory**, where the shell is currently standing. It doesn't start with `/`, and the same characters can point to different places depending on where you are

The `.` and `..` from last week are what relative paths are built from. `.` is where you are, and `..` is one level up. If the shell is standing in `/home/lupi/project`, you can point to the same `notes` directory in two ways.

```bash
pwd                   # /home/lupi/project
ls /home/lupi/notes   # absolute path: start from the root
ls ../notes           # relative path: go up one level from here, then into notes
```

Both commands show the same directory. But go back home with `cd ~` and type `ls ../notes` again, and this time it looks for `/home/notes` — which usually doesn't exist, so you get an error. A relative path comes as a set with "where you're standing right now."

So which kind is the `~/project` from last week? `~` is a marker the shell expands into your home directory's absolute path before running the command. So once it passes through the shell, `~/project` becomes the absolute path `/home/lupi/project`.

Put together, here's how to tell them apart.

- If it starts with `/`, it's an absolute path. It points to the same place wherever you run it, which makes it a good fit for places like scripts, where you can't be sure where they'll run from
- If it starts with `~`, the shell turns it into your home's absolute path
- Every other path (`notes`, `./notes`, `../notes`) is relative. Short and handy, but it calls for the habit of checking where you are with `pwd` before running anything

---

## Observation 2 — mkdir, cp, mv: create, copy, move

Now that I can write addresses, it's time to handle some files. Pretend the `notes` directory in the tree above doesn't exist yet, and build things one at a time starting from home.

![Create notes with mkdir, copy with cp while retaining the original, move to project/today.txt with mv, then remove it with rm](./images/03-file-commands-flow.en.v2.png)

```bash
cd ~                                # start at home
mkdir notes                         # create the notes directory
cp todo.txt notes/                  # copy todo.txt into notes (the original stays)
ls notes                            # → todo.txt
mv notes/todo.txt notes/today.txt   # rename it in place
mv notes/today.txt project/         # move it into project
```

Here's what I observed about each command.

- `mkdir directory`: creates a new directory (**m**a**k**e **dir**ectory). To create intermediate directories in one go, add `-p`, as in `mkdir -p project/logs/2026`. With `-p`, it doesn't complain even if the directory already exists
- `cp source target`: **copies** the source (**c**o**p**y). The original stays where it is
- `mv source target`: **moves** the source (**m**o**v**e). It disappears from where it was

The interesting part was that `cp` and `mv` behave differently depending on **what the target is**.

- If the target is an existing directory, the source goes **into** that directory under the same name (`cp todo.txt notes/`)
- If the target is a name that doesn't exist yet, it becomes a **new file** with that name (`cp todo.txt backup.txt`)
- That's why `mv` has no separate "rename" command. Moving something to a different name in the same directory *is* renaming it

This is also where one reason for the danger rating shows up. If a file with the same name already exists at the target, `cp` and `mv` **overwrite it without asking** by default. If you want to be asked first, add the `-i` (interactive) option.

```bash
cp -i todo.txt notes/      # asks before overwriting if notes/todo.txt already exists
```

Copying a whole directory needs `-r` (recursive). Run plain `cp notes backup`, and GNU `cp` tells you it skipped the directory, with something like `-r not specified; omitting directory 'notes'`. Only `cp -r notes backup` copies everything inside it too. `mv`, on the other hand, moves directories as they are, no `-r` needed.

---

## Observation 3 — find to search, rm to delete

The last thing I observed was finding and deleting. I grouped the two because the order matters: find it and check it with your own eyes before you delete it.

`find` walks the whole tree downward from the starting point you give it and prints every path that matches the condition.

```bash
find . -name "*.log"         # anything under here whose name ends in .log
find ~ -type d -name notes   # only directories named notes, anywhere under home
```

```text
./project/app.log
```

This output is an example. You write it as `find start condition`. If the starting point is a relative path (`.`), the results come out as relative paths starting with `./`; if it's an absolute path (`/home/lupi`, which is what `~` expands to), the results are absolute too. The two kinds of address from Observation 1 carry straight through here.

There's a reason `"*.log"` is wrapped in quotes, too. Last week I noted that the shell expands `~` ahead of time — and `*` works the same way. Type `find . -name *.log` without quotes, and if there are `.log` files in the current directory, the shell replaces `*.log` with those file names first. Then `find` receives some unrelated file names instead of a pattern. The quotes say: "Shell, don't expand this — hand it to `find` as is."

Now for deleting.

```bash
rm project/app.log      # delete a file
rmdir notes             # delete an empty directory (fails if anything is inside)
rm -r backup            # delete a directory and everything in it
rm -i project/*.log     # delete, asking about each file one by one
```

The most important thing I recorded about `rm` (**r**e**m**ove) is that **there's no trash can**. Deleting in a file explorer usually means moving things to the trash, but `rm` deletes them on the spot. There's no undo button either. That's why `rm -rf` — `-r` for directories plus `-f` (force), which skips confirmations and error messages — is so often called out as the combination to be especially careful with.

So I settled on one habit before deleting: print the targets first with `find` or `ls`, check that the list matches what I expect, and only then run `rm` on the same paths. If I'm using relative paths, I type `pwd` once before that, too.

---

## Summary

- A path is a file's address in the filesystem tree. An absolute path, starting with `/`, points to the same place from anywhere; a relative path points to a place measured from the working directory
- The shell expands `~` into your home directory's absolute path
- Create with `mkdir` (`-p`), copy with `cp` (`-r`), and move or rename with `mv`
- When the target is a directory, `cp` and `mv` put things inside it, and if a file with the same name exists, they overwrite it without asking. Use `-i` to be asked
- Search with `find start condition`, and quote patterns so the shell doesn't expand them first
- `rm` has no trash can. Print and check the targets before you delete them

---

## Codigdex notes

Last week I learned how to ask the shell where it's standing; this week I learned how to point it precisely at "that file over there." Once I could tell an address that starts at the root from one that starts where I'm standing, `cp`, `mv`, `rm`, and `find` all read with the same grammar. In the end, every command came down to "which path, to which path."

The next observation meets permissions and users. Finally, I'll read strings like the `drwxr-xr-x` I set aside in last week's `ls -l`, and observe how `chmod`, `chown`, and `sudo` control who can read, write, and run each file.

Before that, the second specimen of the Linux chapter goes into the Codigdex. **NO.007 Path Forager** — follows path maps to gather and move files. The second of the Linux chapter's five slots is filled.

![Path Forager registration card on a blank cream background — NO.007, File explorer type, collects and moves files with path maps, Linux chapter 2/5](./images/04-path-forager-registration.en.v2.png)
