import sys
import os
import time
import gettext
import glob
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
# to get the base path, from which we can assume that the Dabo files
# are in a subdirectory named 'dabo'.
for pthItem in pth:
	if "library.zip" in pthItem:
		basepth = os.path.dirname(pthItem)
		dabopth = os.path.join(basepth, "dabo")
#		sys.path.insert(0, dabopth)
		sys.path.insert(0, basepth)
		break

currdir = os.getcwd()
libdir = os.path.join(currdir, "lib")
if not currdir in pth:
	sys.path.append(currdir)
#- if not libdir in pth:
#- 	sys.path.append(libdir)
	
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
	
	import reportlab


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
		
		if self.prg:
			# If this program contains a path, add that path to 
			# the sys.path
			pth = os.path.split(self.prg)[0]
			if pth:
				if pth not in sys.path:
					sys.path.append(pth)
		
		# Debugging!
		print "-"*88
		print "RUN"
		print "ARGS", sys.argv
		print "PATH", sys.path
		print "CURDIR", os.getcwd()
		
		time.sleep(5)
		
		# Update the argv list to eliminate this program
		sys.argv = sys.argv[1:]



	def run(self):
		if self.prg:
			impt = self.prg
			isFile = (impt[-3:] == ".py")
			if isFile:
				impt = self.prg[:-3]
				
			print "self.prg:", self.prg, impt
			print "self.module:", self.module
	
			if not self.module:
				if isFile:
					execfile(self.prg, {"__name__": "__main__"} )
				else:
					# File should run directly when imported
					exec("import " + impt)
			else:
				print "EXEC:", impt + "." + self.module + "()"
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
