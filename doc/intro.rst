============
Introduction
============


Acknowledgments
===============

I am grateful to everybody who pointed out bugs in previous versions,
or made suggestions about new features.

The images of the board and the stones were created by Patrice Fontaine.

Disclaimer
==========

I have thoroughly tested uliGo on one Linux box, and installed and briefly
tested it on a Windows system (Win2000).
There are no bugs that I know of, but since this is the very first published
version, probably some bugs exist nevertheless. So let me state clearly that
this program comes WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General 
Public License for more details.

Where to get uliGo
==================

- You can download the uliGo distribution (as a .tar.gz for Linux/Unix or
  as a .zip file for Windows/Macintosh) from

    http://www.u-go.net/uligo/

  On that page you can also find more information about uliGo, including some
  screenshots.

Give it a try and please send me your feedback! Any comments, and especially
bug reports are welcome. 

Features
========

To get stronger at go, it is essential to develop one's reading ability. That
is why professionals recommend to study life and death or tesuji problems.
uliGo is a program that allows you to do that: basically, the computer
displays a problem, and asks for the answer. You enter the first move, the
computer responds, and so on until you reach the final solution or enter a
wrong move. 

The main features of uliGo are

* It is free. uliGo is published under the GNU General Public License 
  (GPL), so you don't have to pay anything to use it. Moreover you may 
  freely distribute it. You also get the full source code and may add your 
  own features to the program, as long as you also release the changes
  under the GPL.

* It is cross-platform. uliGo is written in Python (with Tkinter for 
  the graphical user interface). So you may have to install Python first; 
  but it comes with most Linux distributions nowadays, can be installed on 
  Windows machines in a minute with a comfortable installer, and is 
  available on nearly any platform (Apple Macintosh, of course, but also 
  other UNIX versions, etc.). Go to http://www.python.org/ for more 
  information on Python (and how to install it; also see the uliGo 
  documentation).

* It uses the SGF format for storing the problems. That means that you can
  easily (with any SGF editor, in fact) generate your own problem database.
  Also, if you find an error in an existing database, you can fix it yourself.
  Comments from the SGF files are automatically displayed, and you can 
  also give 'wrong variations' that contain the refutation of a certain move.

* In order to make sure that you do not only learn the answer in one particular
  position, but rather the right move for a certain shape, uliGo randomly
  switches the colors (black <-> white) and changes the position on the
  board (by mirroring/rotating) of the problem. 

* If you are stuck, you can look at the solution of the problem. You can
  also, at any time, play out a variation of your own (for example when you
  want to convince yourself why a certain move does not (or does) work.

* There is a customizable stop clock; so you can set the time you have
  for answering yourself. If the problems in the current database are easy,
  try to solve them in thirty seconds (or less ...), if they hard, allow
  yourself more time to think or turn off the clock.

* It comes with two problem collections (easy & hard) with 80 problems 
  altogether. Some of these problems I composed myself, the other
  ones are taken from classical problem collections.
  Certainly for some people the "easy" problems are not so easy, 
  and others will not find the "hard" problems difficult at all. 
  I hope you will find some problems that are suitable for you, anyway. 
  Considering that only some of the problems will be useful for any 
  particular level, 80 problems obviously are not much.
  It would be desirable to make more problems available in SGF format;
  of course, because of the copyright, it is not possibly to put a
  whole book into SGF and give it away; also from an ethical point of view,
  this would be undesirable, since I think it is important to support the 
  authors and publishers of such books. I would find it ideal if 
  some go publishers would sell problem collections in SGF format, at a 
  reasonable price. It should be easy enough to find volunteers who put 
  (parts of) a book into SGF.
  If you own a copy of Cho's Encyclopedia of Life and Death on disk,
  you can use the program cho2sgf.py (to be found on the same web page
  as uliGo) to translate those problems into SGF format and use them
  with uliGo. 


