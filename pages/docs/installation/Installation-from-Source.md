[Documentation](.) > [Installation](Installation) > [Local Installation](Local Installation) > Installation from Source

# Installation from Source

Here is how to build Python or PyPy and Crossbar.io from sources.

This is a reliable, quick way of installation that does not require superuser rights, can install to any location (such as your home directory) and does not depend on system Python packages.

> Note: This recipe was tested on a completely fresh install of [Ubuntu](http://www.ubuntu.com/) [14.04 LTS 64-bit Server](http://www.ubuntu.com/download/server) running as a [Oracle VirtualBox](https://www.virtualbox.org/) virtual machine.

## Prepare

After a fresh install of Linux (we use Ubuntu 14.04 LTS 64-bit Server), first update your system (recommended):

    sudo apt-get update
    sudo apt-get -y dist-upgrade

and reboot. Then install the prerequisites:

    sudo apt-get -y install build-essential libssl-dev libffi-dev \
       libreadline-dev libbz2-dev libsqlite3-dev libncurses5-dev

> Note: These packages really should be installed system-wide, whereas the Python and Crossbar.io we build and install in an arbitrary (non-system) location.

Now continue to build for:

 1. [CPython](#cpython) or
 2. [PyPy](#pypy)


## CPython

After the [prepare-step](#prepare), build Python from vanilla sources and install it to your home directory:

    cd $HOME
    wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz
    tar xvf Python-2.7.8.tar.xz
    cd Python-2.7.8
    ./configure --prefix=$HOME/python278
    make
    make install

Install [Pip](https://pypi.python.org/pypi/pip):

    wget https://bootstrap.pypa.io/get-pip.py
    ~/python278/bin/python get-pip.py

Now, to install Crossbar from [PyPi](https://pypi.python.org/pypi/crossbar):

    ~/python278/bin/pip install crossbar[all]

**or** install Crossbar directly from [GitHub](https://github.com/crossbario/crossbar):

    cd $HOME
    git clone git@github.com:crossbario/crossbar.git
    cd crossbar/crossbar
    git tag -l
    git checkout v0.9.4
    ~/python278/bin/pip install -e .[all]

> Generally, you should only use *tagged* versions from the source tree. The *head* of *master* and/or other branches than *master* might be broken or incomplete.

Check the Crossbar installation:

```console
$v~/python278/bin/crossbar version
Crossbar.io software versions:

Crossbar.io     : 0.9.6-2
Autobahn        : 0.8.10
Twisted         : 13.2.0-IOCPReactor
Python          : 2.7.5
UTF8 Validator  : autobahn
XOR Masker      : autobahn
```

If everything went fine, add the following to your `$HOME/.profile`:

```shell
export PATH=${HOME}/python278/bin:${PATH}
```

## PyPy

After the [prepare-step](#prepare), install PyPy to your home directory:

    cd $HOME
    wget https://bitbucket.org/pypy/pypy/downloads/pypy-2.3-linux64.tar.bz2
    tar xvjf pypy-2.3-linux64.tar.bz2

Install [Pip](https://pypi.python.org/pypi/pip):

    wget https://bootstrap.pypa.io/get-pip.py
    ~/pypy-2.3-linux64/bin/pypy get-pip.py

Now, to install Crossbar from [PyPi](https://pypi.python.org/pypi/crossbar):

    ~/pypy-2.3-linux64/bin/pip install crossbar[all]

**or** install Crossbar directly from [GitHub](https://github.com/crossbario/crossbar):

    cd $HOME
    git clone git@github.com:crossbario/crossbar.git
    cd crossbar/crossbar
    git tag -l
    git checkout v0.9.4
    ~/pypy-2.3-linux64/bin/pip install -e .[all]

> Generally, you should only use *tagged* versions from the source tree. The *head* of *master* and/or other branches than *master* might be broken or incomplete.

Check the Crossbar installation:

```console
$ ~/pypy-2.3-linux64/bin/crossbar version
Crossbar.io software versions:

Crossbar.io     : 0.9.6-2
Autobahn        : 0.8.10
Twisted         : 13.2.0-IOCPReactor
Python          : 2.7.5
UTF8 Validator  : autobahn
XOR Masker      : autobahn
```

If everything went fine, add the following to your `$HOME/.profile`:

```shell
export PATH=${HOME}/pypy-2.3-linux64/bin:${PATH}
```

## Updating from the Repository

Once you've installed Crossbar.io, you can **update to the newest release version** at any time by doing

    pip install -U crossbar

If you want to **update to the most current development version** (e.g. for testing), you can do so from the git repository.

### Cloning the repo

> Note: The Amazon EC2 or Microsoft Azure images we provide already have the git repository cloned.*

You need to have [git](http://git-scm.com/) installed.

Then clone the repository into a directory `crossbar` in your current directory. If you're not registered on GitHub you can clone the repository by doing

    git clone https://github.com/crossbario/crossbar.git

else we suggest using SSH

    git clone git@github.com:crossbario/crossbar.git

If you want to name the directory differently, just add that directory name at the end, e.g.

### Pulling changes

Unless you've just cloned the repository, you need to update it before installing. In a shell, in the repository directory, do

    git pull

## Update Crossbar.io

Then you can update your Crossbar.io installation by doing

    cd crossbar
    python setup.py install

To install Crossbar.io with all optional dependencies

    pip install --upgrade -e .[all]

> On Windows, this will most likely  require installing the [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266).


## Next

Ready to go? Then [choose your language or device of choice](Choose your Weapon).
