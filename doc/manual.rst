======
Manual
======

This is the documentation for uliGo 0.4 - a program to practice Go problems. 
It was written by Ulrich Goertz (u@g0ertz.de).
uliGo is published under the `GNU General Public License <http://www.gnu.org/copyleft/gpl.html>`_.
This program comes WITHOUT ANY WARRANTY.


Getting started
===============

From now on I assume that you installed the program, and that 
the main window pops up when you start it. (Otherwise, read the 
section about :ref:`installing uliGo <installation>` first.)

The first thing you have to do is to load a problem collection.  Some
example collections come with uliGo; see below how you can create your own
ones. So, go to the 'File' menu, and select 'Open problem collection'.
Then choose one of the sgf files that you are shown (they are in the 'sgf'
subdirectory which should automatically be selected).  Later, the program
automatically loads the collection you used last.  Of course you can always
load another collection with the 'Open problem collection' command in the
File menu.

I think that the user interface is pretty self-explanatory,
so I suggest that you just play around a bit with it:
press the right arrow to see the first problem. The problem (randomly
chosen from the database) will be displayed, the stop clock 
will be started (by default you have 2 min 30 sec to find the
complete answer), and you can play your move. The indicator above the
clock (and the 'cursor') shows whose turn it is. After you
enter your move, the program automatically replies (unless
your suggested move was wrong and no refutation is contained
in the database). Then enter the next move ... when the correct
solution is reached, the program shows a 'solved' indicator on the left.
After entering a wrong move, you can still try to solve the
problem, but you cannot get credit for it anymore, of course;
instead of the green "solved" you will see a blue
one when you get to a correct solution (similarly after
using undo, the 'show solution' mode or the 'try variation' mode).

With the right arrow you can go to the next problem (this works at
any stage). Note that the arrow buttons do not serve to navigate within the SGF file 
(use UNDO and HINT, respectively, to do that), but to go to the next problem, or 
back to the previous one.

Alternatively, if you choose 'Replay game', you can load any SGF file, and
replay it by :ref:`guessing the next move <guess-next-move>`.


Solving problems
================


Next Problem
------------


.. image:: images/right.gif
  :align: right

This button discards the current problem, and shows the next one.
This works at any stage, no matter if you solved the current problem
correctly or not, or if you tried some variation etc.
Of course, some problem collection must be open; otherwise nothing
happens.

Previous problem
----------------

.. image:: images/left.gif
  :align: right

With this button, you can go back to the previous problem. Clicking it more than once goes back further,
like with the 'back' button in a web browser.
Note though that you can't go back and forth: the 'next' button will not go back to the problem you came 
from, but will give you a new problem.

Restart problem
---------------

.. image:: images/reload.gif
  :align: right
  
Go back to the beginning of the problem, and start over. 
If you are at the beginning of the problem already,
this sets up the problem again at a (possibly) different position and with different colors.

Hint
----

.. image:: images/hint.gif
  :align: right

Give a hint, i.e. show the next move (and the answer). Using the Hint button results in 
this problem not being counted in the statistics, i.e. it is neither a wrong nor a correct answer.

Show Solution
-------------

.. image:: images/showsol.gif
  :align: right

This shows a solution of the current problem. (The button is
disabled if you already solved the problem correctly yourself.)
You can choose between two modes for displaying the solution
(in the Options menu: :ref:`Show solution mode <show-solution-mode>`):

* animate solution: the moves of the solution are played out.
  Choose the speed in the Options menu. If there are several correct 
  solutions, one is chosen randomly.
* navigate solution: You can 'navigate' the underlying SGF file
  with the correct and wrong variations yourself. The possible
  variations at a given move are marked by green (correct),
  red (wrong) or blue (moves of the opponent) markers. Just click
  on one of them to choose that variation. With the Undo button
  you can undo the last move. If only red markers are displayed,
  you cannot reach the correct resolution from this point anymore - 
  you went wrong earlier. Use the Undo button to go back until
  a green marker appears.


Using the Show Solution button results in this problem not being counted in
the statistics, i.e. it is neither a wrong nor a correct answer.


Try variation
-------------

.. image:: images/tryvar.gif
  :align: right

At any point, you can press this button, and then play out some
variation of your own, e.g. to convince yourself that/why something
does not work. Use the Undo button to undo a move. As long as
you are in the 'Try variation' mode, the 'Show solution' mode
is disabled - it wouldn't make sense to display the solution with
your additional stones on the board. Press 'Try variation' again
to leave this mode and remove all the stones of your variation.
Once you enter this mode, you cannot get any credit for the current
problem anymore.

Undo
----

.. image:: images/undo.gif
  :align: right

With this button you can undo the last two moves (the answer to your
last move and your last move) or the last move (if there was no
answer to your last move or in the Show solution/navigate mode
or in 'Try variation' mode).
If you use the undo feature, you cannot get any credit for the 
current problem anymore.


The stop clock
==============


The clock starts when you press the 'next problem' button.
The default time is 150 seconds. You can change it by a
right mouse click on the clock or by choosing the 'change
clock settings' command in the options menu. This only works
when the clock is not running.


Set the clock to 0 seconds to turn it off.


When the time for the current problem is over, it is counted
as a wrong answer.


How the program chooses the next problem from the database (in random order mode)
=================================================================================


Apart from the database, the program maintains a list of all
problems, together with information how often each problem
has been asked already, and with which results (this list
is stored in the xyz.dat file, where xyz is the name of the
SGF file).

When you request the next problem, a problem is chosen
randomly from the first half of the list; problems from
the first third are a little bit more likely to be chosen
then others.


When you answer a problem correctly, it will be moved to
the very end of the list. So it will take some time until
that problem can come up again. When you give a wrong answer,
the problem will be moved to a random location in the 
second half (more precisely: in the 4th sixth) of the list;
so this problem cannot appear again immediately, but it
could after a relatively short time, and the more problems you
answer correctly, the more likely it is that you will asked 
problems that you got wrong once for a second time.


You can erase the information on your previous answers by
deleting the .dat file corresponding to a database. A new
.dat file (in which the order of problems is that of the 
SGF file) will be created when you open the database.


(In case you installed uliGo system-wide under Unix, the
.dat files are in the .uligo subdirectory of your home
directory. See the file install.txt for more details.)


Using your own problem database
===============================


The format used for the problem database is just the SGF format.
So in order to make your own database, just put a bunch of SGF
games in one single file. Some conventions (explained below)
have to be followed, but I think they are much or less
common sense. So probably you can just enter a problem
into any SGF editor, and everything will work.


The following conventions have to be satisfied:


* The first node(s) of the SGF file may contain anything. If the first node
  contains a GN[gamename] item, the game name is displayed. Besides that
  the program ignores the nodes until a node with an AB[] (place black
  stone) and/or AW[] (place white stone) item comes up. All other AB's and
  AW's have to follow this node without any interruption (the program gets
  confused if there is an empty node in between). After that, the program
  expects nodes with a B[] ('play black stone') or W[] ('play white stone')
  item, and they must alternate properly. Two black plays in a row, for
  instance, are not allowed.
* If you want to have 'wrong variations' in your problems (as a refutation
  to some answer), the first node of that variation has to contain a WV
  ('Wrong Variation', this is not an official SGF tag) item or a TR[] item
  ('triangle label').  The triangle label option is there in order to make
  it easier for you to edit problems with an arbitrary SGF editor; just
  place triangle labels on the first move of a wrong variation.  Of course,
  that also means that no other triangle labels should appear in the SGF
  files. (Other labels may appear, but are ignored at the moment.)
* You can insert a general comment about the collection which is displayed
  after the file is loaded, but before you look at the first problem. Just
  place it at the very beginning of the SGF file. Anything before the first
  '(' is considered as a general comment. The only restriction is that your
  comment must not contain a '('.


One final remark: since every move that is not in the SGF file
is considered wrong, it is desirable to put every correct
solution into the file. Unfortunately, it is easy to miss
some alternative moves, especially after some moves have already
been played. Certainly there are some correct alternatives
missing in the problems that come with uliGo; so don't
take it too seriously if your answer is counted as wrong
although it is right ...


.. _guess-next-move:

Replaying games ("guess next move")
===================================

One fun way to study go is to replay professional games by guessing the
next move. You can load an SGF file with "Replay game" in the File menu. The
stop clock will then be replaced by a few buttons and a frame with a small 
"go board".


With the buttons, you can choose if you want to guess only black or only white
moves, or both. Clicks on the board will be interpreted as guesses - if 
you managed to guess the next
move in the current SGF file, that move is played; otherwise no stone is
placed on the board.


In the frame below the buttons you get some feedback on your guesses. If your
guess is right, it displays a green square (and the move is played on the 
board). If the guess is wrong, it displays a red rectangle; the rectangle is
roughly centered at the position of the next move, and the closer your
guess was, the smaller, and more accurately positioned is that rectangle. 
Furthermore the number of correct guesses and the number of all guesses, 
as well as the success percentage are given.


If you just can't find the next move, you can always use the
'HINT' button, and the move will be played out. You can restart the game 
with the middle button in the first row.




The menu
========

File menu
---------

Open
^^^^


Load a new problem database. A database just consists of
several SGF files. Some example databases are included in
the uliGo distribution. See below for more information how
to create your own databases.

Statistics
^^^^^^^^^^


Open the statistics window. It shows the name of the 
current database, how many problems are in it, how many problems 
the program has asked you to answer, and how many right/wrong 
answers you have given.

Clear Statistics
^^^^^^^^^^^^^^^^

Delete all information about problems done so far, and about correct and
wrong answers, and reload the problem collection from disk. In particular,
this should be used after making changes to the SGF file with 
your problem collection.

Exit
^^^^

Quit the program.

Options
-------


Fuzzy stone placement
^^^^^^^^^^^^^^^^^^^^^

In order to make the board and stones look more like 'in real
life', by default the stones are not placed precisely on the 
intersections, but by a small, random amount off. 
On a smaller board this doesn't well (and maybe some people
don't like it at all?), so you can disable this fuzzy placement.

Shaded stone mouse pointer
^^^^^^^^^^^^^^^^^^^^^^^^^^

Disables the shaded stone cursor which shows where the next 
move would be if you clicked at the current position.

Allow color switch
^^^^^^^^^^^^^^^^^^

In order to make sure that you don't just learn one particular
problem, but rather a shape, uliGo randomly alters the position
of the problem on the go board, and also the color of the stones.
Because the latter could cause problems if your database contains
comments referring to the colors ('good for black', 'white to move'),
you can force uliGo to use the colors of the SGF file by disabling
this option.

Allow mirroring/rotating
^^^^^^^^^^^^^^^^^^^^^^^^

With this checkbutton, you can switch off the automatical
mirroring/rotating of the problems. That might be useful,
for example, if there are comments referring to the "upper
left" or the "right side".

.. _show-solution-mode:

Show solution mode
^^^^^^^^^^^^^^^^^^

Switch between animate and navigate mode. See the description
of the 'Show solution' button above.

Replay speed
^^^^^^^^^^^^

Choose the speed for replaying the solution (in animate mode).

Change clock settings
^^^^^^^^^^^^^^^^^^^^^

Change the maximal time for solving a problem. You can achieve
the same by right clicking on the clock. (Also see below: The 
stop clock.)

Wrong variations
^^^^^^^^^^^^^^^^

This determines what uliGo does with 'wrong variations', i.e. with wrong answers
to which a refutation is given in the SGF file. You can choose if uliGo should 
tell you your move was wrong immediately when entering the variation, or only at the end of the refutation,
or if uliGo should not descend into wrong variations at all, i.e. 
just show that the move was wrong and take it back.

Random/sequential order mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Choose if the problems should be presented in

* random order: here, the problem is basically chosen at random,
  but problems that you have been asked already are less likely
  to be chosen, especially if your answer was correct.
  (See below for more details.)
* sequential order (keep track of solutions): The program 
  maintains a list of all problems in the SGF file; in this
  mode, it always presents the first problem from that list.
  If you solve the problem, it is moved to the end of the list;
  if your answer is wrong, it is moved somewhere to the second
  half of the list (so it will reappear sooner).
* sequential order (don't record results): In this mode,
  the problems are presented in the same order as in the
  SGF file. Correct or wrong answers are not recorded in
  any way. You can specify the starting point. If you don't
  specify it (or if the entry is invalid, e.g. not an integer),
  it starts with the first problem in the SGF file.



The mode, together with the current position in 'sequential
order, don't record results' mode, is stored in the .dat file;
so basically each problem collection has its own mode.
If you check the "use as default" option, then the current
mode will be chosen for other collections which do not yet
have a .dat file (i.e. you use then for the first time)
or have a .dat file from version 0.1.

Use 3D stones
^^^^^^^^^^^^^

Toggle the use of the more beautiful 3D stones versus flat stones.
The 3D stones were provided by Patrice Fontaine. (Thank you!)

Help menu
---------

About
^^^^^


Some basic information about uliGo.

Documentation
^^^^^^^^^^^^^

Open this documentation in a web browser.


License
^^^^^^^

The uliGo license.



Miscellaneous
=============

That's it for the moment, I think. Feel free to contact me (at
uligo@g0ertz.de) if you have any questions, or - in particular - 
if you find any bugs in the program.

.. _installation:

Installation
============

The program is written in `Python <http://www.python.org>`_, a high-level
interpreted programming language.

Windows
-------

.. TODO FIXME --

Linux/Unix
----------


It is likely that Python is already included
in your distribution. It is also easy to build it yourself with the
source from the Python website. But be sure to install
the Tkinter module which is needed for the GUI, too; look at the
in the README file coming with Python for instructions how to do that.

Once you have Python working, just download and unpack the
uliGo file (uligo-0.4.tar.gz). It will create 
a subdirectory called uligo in the directory where you unzip
it, and all files needed for uliGo will be placed in that
subdirectory. Then just start src/uligo.py::

  cd uligo/src
  python uligo.py


You can also install uliGo system-wide; see below.

Other operating systems
-----------------------

Python is available for many operating systems, so you should also be able to run
uliGo. See the `Python website <http://www.python.org/>`_ for more 
information.

Upgrade from uliGo 0.1, 0.2
---------------------------

.. TODO FIXME


Basically, you should just install uliGo 0.3 from scratch,
and delete the old version (Make sure that you don't delete any sgf files
with problems ...). In particular, you should not use
the files uligo.def and uligo.opt from version 0.1 or 0.2 with
version 0.3 (these files contain the default problem collection
and the saved options, respectively).

You can use the .dat files from uliGo 0.1, though (these files
contain the information about right/wrong answers etc.; for
each SGF file that you used with uliGo there is a corresponding
.dat file). Just copy the .dat files from the sgf subdirectory
of uligo01 to the sgf subdirectory of uligo03. (In case you
installed uliGo system-wide under Unix, it is slightly more
complicated; please see below.)

Systemwide installation under Unix/Linux
----------------------------------------

.. TODO FIXME


To install uligGo system-wide (in /usr/local/share, for instance),
proceed as follows:

Put the uliGo files in /usr/local/share/uligo03 (if you put them
somewhere else, you have to adapt the unixinst.py script
accordingly).

Carefully read, and -if necessary- edit the script unixinst.py .
(I think that you probably will not want to change much.)
Basically, the unixinst.py script writes a 'global' uligo.def
file (in the uligo03 directory) which tells uligo to look
for individual .def files (in $HOME/.uligo ) when it is
started. So for every user who uses uligo, a subdirectory
called .uligo will be created in the user's home directory.
In this directory, the individual .def file (which stores
the path and name of the SGF file used last), the .opt
file (which stored the saved options), and the .dat files
(which store the number of correct/wrong answers for
each problem in the corresponding SGF file) are stored.
In order to avoid name conflicts between .dat files for
.sgf files in different directories, the path is shadowed
in the .uligo directory: for a .sgf file in 
/usr/local/share/uligo/sgf, for example, the corresponding
.dat file is in $HOME/.uligo/usr/local/share/uligo/sgf.

Furthermore the unixinst.py script creates a link
in /usr/local/bin, pointing to uligo.py.

After you edited the unixinst.py script, execute it with
'python unixinst.py'. The only other thing you might have 
to do (if your python interpreter is not in /usr/bin),
is to change the very first line of the file uligo.py,
which must contain the location of the python interpreter,
so that uligo can be started by 'uligo.py'.

History
=======

May 2003: uliGo 0.3, with a few new features, and a Windows installer.

June 2001: uliGo 0.2: some minor bugfixes, and the option to change the
order in which the problems are presented (random vs. sequential)

May 2001: uliGo 0.1 is published.

April 2001: Started writing uliGo.

