import sys, os
import wx
import wx.lib.mixins.listctrl
import wx.lib.gridmovers

import xml
import xml.dom
import xml.sax
import xml.dom.minidom

# Add the current dir and library path
pth = sys.path
# For py2exe installations: sys.path will be the path to 'library.zip',
# which contains all the compiled modules. We need to strip that off
# to get the base path, which includes the images, etc.
for pthItem in pth:
	if "library.zip" in pthItem:
		sys.path.insert(0, os.path.dirname(pthItem))
		break

currdir = os.getcwd()
libdir = os.path.join(currdir, "lib")
if not currdir in pth:
	sys.path.append(currdir)
if not libdir in pth:
	sys.path.append(libdir)
	
def dummyImport():
	# This proc does nothing except force the inclusion of all the modules
	# included below.
	import dabo
	import dabo.biz
	import dabo.common
	import dabo.db
	import dabo.icons
	import dabo.ui
	import dabo.ui.uiwx
	# import dabo.ui.uitk
	
	import wx
	import wx.build
	import wx.lib
	import wx.lib.mixins
	import wx.py
	import wx.tools
	import wx.calendar
	import wx.grid
	import wx.html
	import wx.wizard
	# import wx.activex
	import wx.gizmos
	import wx.glcanvas
	# import wx.iewin
	# import wx.ogl
	import wx.stc
	import wx.xrc
	
	import mx.DateTime
	import xml
	import xml.dom
	import xml.dom.minidom


class DaboRuntimeEngine(object):
	def __init__(self):
		try:
			self.prg = sys.argv[1]
		except:
			self.prg = None
		try:
			self.module = sys.argv[2]
		except:
			self.module = None
		
		# Update the argv list to eliminate this program
		sys.argv = sys.argv[1:]



####################################################
#			NOTE: the following is my attempt to exclude Dabo from the 
#			frozen app. IOW, create a static set of libs, but without Dabo, 
#			so that they can simply add the current version of Dabo without
#			having to download a huge chunk of code that doesn't
#			change. It's still very shaky, but I'm leaving it in here in
#			case I get around to implementing this in the future.
####################################################
#		try:
#			import pathToDabo
#			self.daboPath = pathToDabo.getDaboPath()
#		except:
#			self. daboPath = "."
#			
#		# Add Dabo to the path
#		self.setupDabo()
		# Add the current dir to the path
#		sys.path.append(os.getcwd())
#		# Add the library path, too.
#		sys.path.append(os.path.join(os.getcwd(), "lib"))

#	def setupDabo(self):
#		try:
#			sys.path.append(self.daboPath)
#			import dabo as dabo
# 
#		except:
#			print "The Dabo module was not found in any of these directories:"
#			for p in sys.path:
#				print "\t", p
#			print "Current directory is:", os.getcwd()
####################################################


	def run(self):
		if self.prg:
			impt = self.prg
			isFile = (impt[-3:] == ".py")
			if isFile:
				impt = self.prg[:-3]
#- 		print "self.prg:", self.prg, impt
#- 		print "self.module:", self.module

			if not self.module:
				if isFile:
					execfile(self.prg, {"__name__": "__main__"} )
				else:
					# File should run directly when imported
					exec("import " + impt)
			else:
				#print "EXEC:", impt + "." + self.module + "()"
				exec(impt + "." + self.module + "()")
		else:
			app = wx.PySimpleApp()
			prmpt = "Please select the Python file to run..."
			wildcard = "Python Files (*.py)|*.py|" \
				"Compiled Python (*.pyc)|*.pyc|" \
				"All files (*.*)|*.*"
			openDlg = wx.FileDialog(None, prmpt, wildcard=wildcard, 
					defaultDir=os.getcwd(), style=wx.OPEN ) #| wx.HIDE_READONLY)
			res = openDlg.ShowModal()
			
			app.Destroy()
			pth = openDlg.GetPath()
			openDlg.Destroy()
			if res == wx.ID_OK:
				execfile(pth, {"__name__": "__main__"} )
			

if __name__ == "__main__":
	dEngine = DaboRuntimeEngine()
	dEngine.run()