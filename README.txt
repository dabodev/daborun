The Dabo Runtime Engine for Windows
-------------------------------------


What is it?
--------------
The Dabo Runtime Engine is an EXE that contains all the file needed to run Dabo: the full development environment as well as generated apps. It allows people who are interested in Dabo to try it out without having to install the various prerequisites, and to uninstall it if they decide that it's not for them. The installer does not affect the Windows Registry in any way, and so can be installed without fear of breaking something else.


How do I run stuff?
--------------------
There are two ways: from a DOS command prompt, you can type:
	
	<path>daborun.exe <path to .py file>
	
and the engine will run the specified script. Or, if you don't like the command-line approach, simply double-click either the shortcut installed on your desktop, or the daborun.exe file itself. You will then be presented with a file selection dialog, where you can pick the file you want to run.


There's a whole bunch of .py files! Which ones should I run?
----------------------------------------------------------
In order to make it easy to try Dabo, there are several shortcuts set up, located inside the 'Common' directory off of the directory in which you installed the engine. You can just double-click them to run. Here are the various shortcuts and what they do:

Demo Programs:
----------------
Bubblet - a fun little game where you get to pop lots of bubbles that demonstrates some of the non-database capabilities of Dabo.

Montana - a simple solitaire game that some have found to be very addictive!

SimpleFormWithBizobj - this is the basic application demo. If you have internet connectivity, it will let you query, edit and update a demo database located on the dabodev.com servers. You can create your own apps like this in under a minute using the Dabo AppWizard.

sizerTutorial - a simple demo that helps those who are new to the concept of using sizers to lay out a form figure out how the various settings for a sizer affect the size and position of the objects within the sizer.


Development Tools:
-------------------
AppWizard - as mentioned above, this is a wizard that guides you through the creation of a complete application that can connect to one of many backend databases. The runtime engine only supports MySQL and Firebird databases currently.

ClassDesigner - this tool allows you to visually lay out your UI classes, and also add code that will fire when the appropriate events occur. You can create classes that can be re-used inside of other classes, and save the whole thing as a runnable application.

ReportDesigner - Most database applications also need to be able to generate reports on the data, and this tool allows you to visually lay out and control the apppearance of your reports.

ConnectionEditor - Dabo can store information for connecting to a database in a small XML file. This tool allows you to enter the information, test the connections, and save the info in that XML format.

Editor - A powerful Python text editor written in Dabo. It features code completion, syntax coloring, and lots of other cool stuff.

FieldSpecEditor - The original output of the AppWizard is an XML file containing your applications settings. While you can edit that manually, this tool allows you to more easily control the appearance of your app. You can also preview your changes to make sure that they are what you intended.






