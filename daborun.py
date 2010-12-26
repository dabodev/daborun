# -*- coding: utf-8 -*-
import sys
import traceback
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

def debugmsg(*args):
	# Change this to True to see all the debugging info
	debug = True
	if debug:
		for arg in args:
			print arg,
		print
		
# Add the current dir and library path
pth = sys.path
basepth = os.getcwd()

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
			debugmsg( "INSERTED %s INTO PATH" % basepth)
		break

# Reroute stderr to avoid the popup window:
sys.stderr = open(os.path.join(basepth, "error.log"), "a")

currdir = os.getcwd()
libdir = os.path.join(currdir, "lib")
if not currdir in pth:
	sys.path.insert(0, "\"%s\"" % currdir)
	debugmsg("INSERTING %s INTO PATH" % currdir)
	
def dummyImport():
	# This proc does nothing except force the inclusion of all the modules
	# included below.
	import dabo
	import dabo.biz
	import dabo.db
	import dabo.icons
	import dabo.lib
	import dabo.ui
	import dabo.ui.uiwx
	# import dabo.ui.uitk
	
	import wx
	import wx.build
	import wx.lib
	import wx.lib.mixins
	import wx.lib.platebtn
	import wx.tools.Editra.src.extern.flatnotebook
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
	import sqlite3
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
	
	# Logging handlers are ignored without this.
	import logging
	import logging.handlers


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
				# Make it absolute
				pth = os.path.abspath(pth)
				sys._daboRunHomeDir = pth

				# This prg path may have been appended already, but we need
				# it to be the first in sys.path. Remove it and insert:
				try:
					sys.path.remove(pth)
					debugmsg("INIT: REMOVED %s TO PATH" % pth)
				except ValueError:
					pass
				sys.path.insert(0, pth)
				debugmsg("INIT: INSERTED %s TO PATH" % pth)
		
		# Debugging!
		debugmsg("-"*44)
		debugmsg("RUN")
		debugmsg("ARGS", sys.argv)
		debugmsg("PATH", sys.path)
		debugmsg("CURDIR", os.getcwd())
		
		# Update the argv list to eliminate this program
		sys.argv = sys.argv[1:]


	def run(self):
		if not self.prg:
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

			debugmsg("SELECTION", pth)
			debugmsg("DLG RESULT", res, res == wx.ID_OK)

			openDlg.Destroy()
			if res == wx.ID_OK:
				self.prg = pth

		if self.prg:
			impt = self.prg
			isFile = (impt.endswith(".py"))
			if isFile:
				impt = self.prg[:-3]
			sys._daboRunHomeDir = os.path.dirname(self.prg)
			
			debugmsg("self.prg:", self.prg)
			debugmsg("impt", impt)
			debugmsg("homedir", sys._daboRunHomeDir)
			debugmsg("self.module:", self.module)

			if os.path.exists("C:\DABO-DEBUG.TXT"):
				import pdb
				pdb.set_trace()
	
			hasRun = False
			if self.module:
				debugmsg("EXEC:", impt + "." + self.module + "()")
				try:
					exec(impt + "." + self.module + "()")
					hasRun = True
				except StandardError, e:
					print "EXEC ERROR:", e

			if not hasRun:
				if isFile:
					pthDir, prg = os.path.split(self.prg)
					if not pthDir:
						pthDir = os.getcwd()
					pthDir = os.path.abspath(pthDir)
					debugmsg("PTHDIR", pthDir, "PRG", prg)
					if pthDir not in sys.path:
						sys.path.insert(0, pthDir)
						debugmsg("BEFORE EXEC ISFILE: INSERTING %s INTO PATH"% pthDir)
						debugmsg("SYSPATH", sys.path)
					os.chdir(pthDir)
					sys._daboRunHomeDir = pthDir
					try:
						debugmsg("ABOUT TO EXECFILE:", prg)
						debugmsg("CURDIR:", os.getcwd())
						execfile(prg, {"__name__": "__main__"} )
					except StandardError, e:
						debugmsg("EXECFILE ERROR", e)
						print "-"*60
						print "ARGS:", sys.argv
						print "-"*60
						traceback.print_exc(file=sys.stdout)
						print "-"*60
				else:
					# File should run directly when imported
					exec("import " + impt)
			

if __name__ == "__main__":
	dEngine = DaboRuntimeEngine()
	dEngine.run()
