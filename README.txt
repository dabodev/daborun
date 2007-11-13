The Dabo Runtime Engine for Windows
-------------------------------------


What is it?
--------------
The Dabo Runtime Engine is an EXE that contains all the files needed to run Dabo: the full development environment as well as generated apps. It allows people who are interested in Dabo to try it out without having to install the various prerequisites, and to uninstall it if they decide that it's not for them. The installer does not affect the Windows Registry in any way, and so can be installed without fear of breaking something else.


How do I run stuff?
--------------------
There are two ways: from a DOS command prompt, you can type:
	
	<path>daborun.exe <path to .py file>
	
and the engine will run the specified script. Or, if you don't like the command-line approach, simply double-click either the shortcut installed on your desktop, or the daborun.exe file itself. You will then be presented with a file selection dialog, where you can pick the file you want to run.

If you like using the command prompt, you can add the Dabo Runtime directory to your system's PATH environmental variable. Then you can simply type: "daborun myscript.py" in order to run the 'myscript.py' file.


There's a whole bunch of .py files! Which ones should I run?
----------------------------------------------------------
In order to make it easy to try Dabo, there are several shortcuts set up, located inside the 'Common' directory off of the directory in which you installed the engine. You can just double-click them to run. Here are the various shortcuts and what they do:

Demo Programs:
----------------
DaboDemo - An example of some of the UI controls and how to work with them. The code for each demo is visible, and you can modify it and run that modified code without harming the original. This is a great way to learn about programming the Dabo UI.


Development Tools:
-------------------
AppWizard - as mentioned above, this is a wizard that guides you through the creation of a complete application that can connect to one of many backend databases. The runtime engine only supports MySQL and Firebird databases currently.

Class Designer - this tool allows you to visually lay out your UI classes, and also add code that will fire when the appropriate events occur. You can create classes that can be re-used inside of other classes, and save the whole thing as a runnable application.

Report Designer - Most database applications also need to be able to generate reports on the data, and this tool allows you to visually lay out and control the apppearance of your reports.

Connection Editor - Dabo can store information for connecting to a database in a small XML file. This tool allows you to enter the information, test the connections, and save the info in that XML format.

Text Editor - A powerful Python text editor written in Dabo. It features code completion, syntax coloring, and lots of other cool stuff.

Preference Editor - a handy tool for viewing, editing and/or deleting any saved preferences on your system. Still a work in progress, so some visual elements may not work consistently.
