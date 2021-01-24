# Go
Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

# Installation
First you can download Golang from [Golang offical website](https://golang.org/doc/install#download)

## Linux
If you have a previous version of Go installed, be sure to [remove it](https://golang.org/doc/manage-install) before installing another.
1. Download the archive and extract it into /usr/local, creating a Go tree in /usr/local/go.

    For example, run the following as root or through sudo:

        tar -C /usr/local -xzf go1.15.7.linux-amd64.tar.gz

2. Add /usr/local/go/bin to the PATH environment variable.

    You can do this by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):

        export PATH=$PATH:/usr/local/go/bin

    Note: Changes made to a profile file may not apply until the next time you log into your computer. To apply the changes immediately, just run the shell commands directly or execute them from the profile using a command such as source $HOME/.profile.

3. Verify that you've installed Go by opening a command prompt and typing the following command:

        $ go version

4. Confirm that the command prints the installed version of Go.


## Windows

## Mac