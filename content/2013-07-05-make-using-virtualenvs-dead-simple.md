Layout: post
Title: Make using virtualenvs dead-simple
Date: 2013-07-05 18:00
Comments: true
Category: Python
Tags: tooling,Python,virtualenv,zsh

__tl;dr__ - grab files from [this gist][thisgist] and follow the instructions in
`README.md`

`virtualenv` (and, particularly, `virtualenvwrapper`), are really great when
you want to use specific versions of libraries or make changes to an existing
library without borking other versions of the files. That said, it adds a level
of indirection. I set up my dotfiles to allow me to switch virtualenvs without
a lot of typing. Ultimately, this will let you type just `p <projectname>` to
change to the directory and workon the appropriate virtualenv.

First, I grabbed [Harry Marr's `workon_cwd` command](http://hmarr.com/2010/jan/19/making-virtualenv-play-nice-with-git/)
which detects which `virtualenv` to use with a combination of `git` or a file
called `.venv` in your base directory. I didn't want to overwrite `cd`, so
instead, I aliased a command to handle the workon script (assuming you've
already created an alias like `export PYTHONPROJECTS=$HOME/projects/python`:

```sh
venv_cd $PYTHONPROJECTS/$1;
```

Plus add a completion script (`_files` is a preexisting completion function
that just tells `zsh` to search for files in that directory):

```zsh
#compdef p
_files -W $PYTHONPROJECTS -/
```

Now you can use `p` to change to a python project (potentially including
subdirectories as well) with tab completion and other exciting properties.

I have the full list of files with instructions in [this gist][thisgist]

[thisgist]: https://gist.github.com/jtratner/5934189
