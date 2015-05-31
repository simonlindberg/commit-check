# commit-check

This project is inspired by http://chris.beams.io/posts/git-commit/.
It aims to enforce the guidlines mentioned in the blog post.

Line length violations will cause the commit to abort.
* The subject line must be shorter than 50 characters
* All the lines in the body must be shorter than 72 characters

If any of the following guidelines aren't followed, they will be introduced to the message.
* Capitalize the subject line
* Do not punctuation the subject line
* Seperate the subject line and the body with an empty line


## Recommended setup

If you do not already use any git hooks this setup will work nicely.

1. `mkdir -p ~/.git_template`
2. `cd ~/.git_template`
3. `git clone git@github.com:simonlindberg/commit-check.git hooks`
4. `git config --global init.templatedir '~/.git_template'`

This creates a templete to be used when a new git repository is initiated with `git init`.
If you want to enable it into a already existing repository you can do `git init` there aswell. This will introduce the hooks to the repo, but it won't overwrite any existing hooks. Meaning it will not work if you already use commit related git hooks.
