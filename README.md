# commit-check

This project is inspired by http://chris.beams.io/posts/git-commit/.
It aims to enforce the guidlines mentioned in the blog post.

The blog post mentions 7 goals for a good commit message, 6 of them are enforced by these git-hooks.
 1. Separate subject from body with a blank line ✓
 2. Limit the subject line to 50 characters ✓
 3. Capitalize the subject line ✓
 4. Do not end the subject line with a period ✓
 5. Use the imperative mood in the subject line ✓
 6. Wrap the body at 72 characters ✓
 7. Use the body to explain what and why vs. how

In addition it also spell checks the message.

## Behaviour

Line length violations will cause the commit to abort.
* The subject line must be shorter than 60 characters, warns at 50.
* All the lines in the body must be shorter than 80 characters, warns at 72.

If any of the following guidelines aren't followed, they will be introduced to the message.
* The first line should not be empty (the line is used, if none abort commit)
* Capitalize the subject line
* Do not punctuation the subject line
* Seperate the subject line and the body with an empty line

The message will be run through a spell checker, if any wrongly spelled words are found the full message will be prompted with those underlined. The user decides if to coninue or not.

The sentence will also be parsed for its mood. The subject line have to be in a imperative mood, and subjunctive mood is discuraged in the body of the message. The message with the moods outlined will be show to the user if any bad moods are found. The user decides if to coninue or not.

## Installing the spell checker

The spell checker used is GNU aspell. It is available in `brew install aspell` for mac users, `sudo apt-get install aspell-en` for those who have apt-get available, and somewhere else for those who don't.

## Installing the mood checker

`pattern.en` is used for checking the sentences mood, it is a full web mining tool, but we will only be using one module of Natural Language Processing part. It is available [here](https://github.com/clips/pattern) and is installed with `pip install pattern`.

## Recommended setup

If you do not already use any git hooks this setup will work nicely.

1. `mkdir -p ~/.git_template`
2. `cd ~/.git_template`
3. `git clone git@github.com:simonlindberg/commit-check.git hooks`
4. `git config --global init.templatedir '~/.git_template'`

This creates a templete to be used when a new git repository is initiated with `git init`.
If you want to enable it into a already existing repository you can do `git init` there aswell. This will introduce the hooks to the repo, but it won't overwrite any existing hooks. Meaning it will not work if you already use commit related git hooks.
