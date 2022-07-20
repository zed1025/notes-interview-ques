There are quite a few situations in which you might not want Git to track everything.
A good example would be any files that contain API keys, tokens, passwords or other secrets that you definitely need for testing, but you don’t want them sitting in a repository — especially a public repository — for all to see.
`.gitignore` file, is a set of rules held in a file that tell Git to not track files or sets of files
But the real power of `.gitignore` is in its ability to pattern-match a wide range of files so that you don’t have to spell out every single file you want Git to ignore.
You can have a global .gitignore that applies to all of your repositories, and then put project-specific .gitignore files within directories or subdirectories under the projects that need a particularly pedantic level of control.
## Key points
- .gitignore lets you configure Git so that it ignores specific files or files that match a certain pattern.
- `*.html` in your .gitignore matches on all files with an .html extension, in any directory or subdirectory of your project.
-  `*/*.html` matches all files with an .html extension, but only in subdirectories of your project.
- `!` negates a matching rule.
- You can have multiple .gitignore files inside various directories of your project to override higher-level matches in your project.
- You can find where your global .gitignore lives with the command `git config --global core.excludesfile`.
- GitHub hosts some excellent started .gitignore files at https://github.com/github/gitignore.
