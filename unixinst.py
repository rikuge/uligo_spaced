#!/usr/bin/python
# File: unixinst.py

## This file is part of uliGo, a program for exercising go problems.
## It serves to install uliGo systemwide under Unix.

##   Copyright (C) 2001-12 Ulrich Goertz (uligo@g0ertz.de)

##   This program is free software; you can redistribute it and/or modify
##   it under the terms of the GNU General Public License as published by
##   the Free Software Foundation; either version 2 of the License, or
##   (at your option) any later version.

##   This program is distributed in the hope that it will be useful,
##   but WITHOUT ANY WARRANTY; without even the implied warranty of
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##   GNU General Public License for more details.

##   You should have received a copy of the GNU General Public License
##   along with this program (gpl.txt); if not, write to the Free Software
##   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##   The GNU GPL is also currently available at
##   http://www.gnu.org/copyleft/gpl.html

##   ---------------------------------------------

# Please read the comments below carefully and edit the file where necessary.
# Probably you will not have to make many changes.
# If on your system, the Python interpreter is not in /usr/bin (but in
# /usr/local/bin for example), you will have to change the first line
# of the file uligo.py accordingly.

import os
import sys

# this should be used only on UNIXoid systems:

if os.name != 'posix':
    print('This should be used only on Unix systems. On other systems,')
    print('it is not necessary to execute an installation script.')
    sys.exit()

# write global uligo.def

f = open('uligo.def','w')
f.write('uligo03\n')    # Do NOT change this!

f.write('i /tmp\n')     # 'i'ndividual .def files:
                        # Look for .opt, .def files in $HOME/.uligo,
                        # or -if $HOME is not set- for /tmp/.uligo .
                        # You can replace /tmp with another directory that should
                        # be used as an alternative if $HOME is not set.
                        # It is very unlikely that you have to change this.

# f.write('d \n')       # Uncomment this if .dat files should be stored in the
                        # same directory as the corresp. sgf file.
                        # If you leave it as it is (recommended), the .dat
                        # files are saved in subdirectories of $HOME/.uligo
                        # (or of /tmp/.uligo ...)

# f.write('s /usr/local/share/sgf\n')
                        # Uncomment (and change) this to set a new
                        # default path for sgf files
                        # (the directory you use must exist).
                        # This might make sense if you don't want to put the
                        # .sgf files in your bin directory.
                        # Leave it to make the sgf subdirectory of uligo's
                        # directory the default.

# create link to uligo.py

os.symlink('/home/stefan/Desktop/uligo(py3)/src/uligo.py', '/usr/local/bin/uligo.py')
                        # This creates a link in /usr/local/bin pointing
                        # to uligo.py .
                        # If you put the uligo03 directory not in
                        # /usr/local/share, but somewhere else,
                        # you must change the first entry.
                        # You can change the second entry to put the link
                        # somewhere else, but the link should be in a
                        # directory which is in the PATH of the users.
                        # The file uligo.py itself must stay in
                        # the uligo03 subdirectory where you unpacked it,
                        # because it needs to find the other files in
                        # that subdirectory.

# make uligo.py executable for everybody

os.chmod('uligo.py', 0o755)

# check if the python interpreter is in the 'right' place

if not os.path.exists('/usr/bin/python3'):
    print('Your python interpreter is not installed in /usr/bin .')
    print('Please change the first line of uligo.py accordingly.')
    print('(You can find the location of the Python interpreter with')
    print('\'which python\' .)')
