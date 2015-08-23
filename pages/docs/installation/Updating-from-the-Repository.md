# Updating from the Repository

Once you've installed Crossbar.io, you can **update to the newest release version** at any time by doing

    pip install -U crossbar

If you want to **update to the most current development version** (e.g. for testing), you can do so from the git repository.

## Cloning the repo

> Note: The Amazon EC2 or Microsoft Azure images we provide already have the git repository cloned.*

You need to have [git](http://git-scm.com/) installed.

Then clone the repository into a directory `crossbar` in your current directory. If you're not registered on GitHub you can clone the repository by doing

    git clone https://github.com/crossbario/crossbar.git

else we suggest using SSH

    git clone git@github.com:crossbario/crossbar.git

If you want to name the directory differently, just add that directory name at the end, e.g.

## Pulling changes

Unless you've just cloned the repository, you need to update it before installing. In a shell, in the repository directory, do

    git pull

## Update Crossbar.io

Then you can update your Crossbar.io installation by doing

    cd crossbar
    python setup.py install

To install Crossbar.io with all optional dependencies

    pip install --upgrade -e .[all]

> On Windows, this will most likely  require installing the [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266).
