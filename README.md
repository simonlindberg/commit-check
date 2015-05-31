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
