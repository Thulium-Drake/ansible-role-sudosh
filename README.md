# Shell logging with sudosh, powered by Ansible
This role will configure a system to log user sessions with sudosh.

This includes:
* Installing the sudosh package
* Configuring available login shells
* Configuring sudoers to allow users to sudo as themselves

It will _NOT_ configure any sudo permissions beyond those required to run sudosh.

## Package
This role depends on a package that may or may not be available in your distribution.
For RHEL-like systems a RPM spec file has been provided. This can be compiled on any RHEL7+ system
that has Go installed on it. Source (in Golang) for sudosh can be found on https://github.com/cloudposse/sudosh/

## Configuration of users
This role will prepare a system for use with sudosh, but it will _not_ configure your useraccounts.
As these can come from a variaty of different sources. However, the main gist for configuring is:

* Ensure that they have ```/usr/bin/sudosh``` as their login shell
* Enforce that your users can not change the shell (local users are already limited to shells in /etc/shells)
* Ensure that any 'service' accounts are excluded from this

This role does configure ```requiretty```, so ```ssh user@host bash``` and the like should not be possible.

## Configuration of root (or other user) prompt
It is advisable to configure the prompt for root to display the output of the ```logname``` command,
as this shows which user originated the sudo session. For example:

```
 PS1="[$(logname)>\u@\h \W]\\$ "
```

Which will show the following prompt:

```
[user>root@host ~]# whoami
root
```

Where 'user' is the login name of the original user.

## Replaying sessions
Replaying sessions can be done using ```sudoreplay``` which is available via the 'sudo-ldap' package.
