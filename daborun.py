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

def debugout(*args):
	# Change this to True to see all the debugging info
	debug = True
	if debug:
		for arg in args:
			print arg,
		print
		
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
		if not basepth in pth:
			sys.path.insert(0, basepth)
			debugout( "INSERTED %s INTO PATH" % basepth)
		break

# Reroute stderr to avoid the popup window:
sys.stderr = open(os.path.join(basepth, "error.log"), "a")

currdir = os.getcwd()
libdir = os.path.join(currdir, "lib")
if not currdir in pth:
	sys.path.insert(0, "\"%s\"" % currdir)
	debugout("INSERTING %s INTO PATH" % currdir)
	
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
	
	import winpdb
	import MySQLdb
	import pysqlite2
	import kinterbasdb

	# For PIL compatibility
	import PIL
	import Image
	import ArgImagePlugin
	import BmpImagePlugin
	import BufrStubImagePlugin
	import CurImagePlugin
	import DcxImagePlugin
	import EpsImagePlugin
	import FitsStubImagePlugin
	import FliImagePlugin
	import FpxImagePlugin
	import GbrImagePlugin
	import GifImagePlugin
	import GribStubImagePlugin
	import Hdf5StubImagePlugin
	import IcnsImagePlugin
	import IcoImagePlugin
	import ImImagePlugin
	import ImtImagePlugin
	import IptcImagePlugin
	import JpegImagePlugin
	import McIdasImagePlugin
	import MicImagePlugin
	import MpegImagePlugin
	import MspImagePlugin
	import PalmImagePlugin
	import PcdImagePlugin
	import PcxImagePlugin
	import PdfImagePlugin
	import PixarImagePlugin
	import PngImagePlugin
	import PpmImagePlugin
	import PsdImagePlugin
	import SgiImagePlugin
	import SpiderImagePlugin
	import SunImagePlugin
	import TgaImagePlugin
	import TiffImagePlugin
	import WmfImagePlugin
	import XVThumbImagePlugin
	import XbmImagePlugin
	import XpmImagePlugin


class DaboRuntimeEngine(object):
	def __init__(self):
		try:
			self.prg = sys.argv[1]
		except IndexError:
			self.prg = None
		try:
			self.module = sys.argv[2]
		except IndexError:
			self.module = None

		# Inform the framework that we are using the dabo runtime:
		sys._daboRunHomeDir = None

		if self.prg:
			# If this program contains a path, insert that path to 
			# the sys.path. This will be the first place libraries will
			# be searched for, and it will become Application.HomeDirectory.
			pth = os.path.split(self.prg)[0]
			if pth:
				sys._daboRunHomeDir = pth

				# This prg path may have been appended already, but we need
				# it to be the first in sys.path. Remove it and insert:
				try:
					sys.path.remove(pth)
					debugout("INIT: REMOVED %s TO PATH" % pth)
				except ValueError:
					pass
				sys.path.insert(0, pth)
				debugout("INIT: INSERTED %s TO PATH" % pth)
		
		# Debugging!
		debugout("-"*44)
		debugout("RUN")
		debugout("ARGS", sys.argv)
		debugout("PATH", sys.path)
		debugout("CURDIR", os.getcwd())
		
		# Update the argv list to eliminate this program
		sys.argv = sys.argv[1:]



	def run(self):
		if self.prg:
			impt = self.prg
			isFile = (impt[-3:] == ".py")
			if isFile:
				impt = self.prg[:-3]
				
			debugout("self.prg:", self.prg, impt)
			debugout("self.module:", self.module)
	
			if not self.module:
				if isFile:
					pthDir, prg = os.path.split(self.prg)
					if not pthDir:
						pthDir = os.getcwd()
					debugout("PTHDIR", pthDir)
					if pthDir not in sys.path:
						sys.path.insert(0, pthDir)
						debugout("BEFORE EXEC ISFILE: INSERTING %s INTO PATH"% pthDir)
					os.chdir(pthDir)

					try:
						execfile(prg, {"__name__": "__main__"} )
					except StandardError, e:
						debugout("EXECFILE ERROR", e)
				else:
					# File should run directly when imported
					exec("import " + impt)
			else:
				debugout("EXEC:", impt + "." + self.module + "()")
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
			
			debugout("SELECTION", pth)
			
			openDlg.Destroy()
			if res == wx.ID_OK:
				if pth:
					pthDir, prg = os.path.split(self.prg)
					if not pthDir:
						pthDir = os.getcwd()
					debugout("PTHDIR", pthDir)
					if pthDir not in sys.path:
						sys.path.insert(0, pthDir)
						debugout("BEFORE EXEC: APPENDING %s to PATH"% pthDir)
					os.chdir(pthDir)
						
				debugout("")
				debugout("PATH BEFORE EXECUTION", sys.path)

				execfile(pth, {"__name__": "__main__"} )
			

if __name__ == "__main__":
	dEngine = DaboRuntimeEngine()
	dEngine.run()
