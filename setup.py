# -*- coding: utf-8 -*-
from distutils.core import setup
import glob
import py2exe

setup(
	# The first three parameters are not required, if at least a
	# 'version' is given, then a versioninfo resource is built from
	# them and added to the executables.
	version = "0.8.4",
	description = "Dabo Runtime Engine",
	name = "daborun",
	# targets to build
#	console = ["daborun.py"],
	windows = ["daborun.py"],
	#exclude the actual framework
	options = { "py2exe": 
			{"includes" : ["code", "compiler", "ConfigParser", "copy", "cStringIO", 
				"datetime", "encodings", "imghdr", "inspect", "keyword", "locale", 
				"math", "mx.DateTime", "operator", "PIL", "platform", "pydoc", 
				"random", "sqlite3", "string", "tempfile", "test", "threading", "time", 
				"traceback", "types", "unittest", "urllib", "urllib2", "urlparse", "warnings"],
			"excludes" : ["dabo", "dabo.db", "dabo.biz", "dabo.lib", "dabo.ui", 
				"dabo.common", "dabo.icons", "dabo.ui.uiwx", "Tkconstants", "Tkinter", "tcl",
				"_imagingtk", "PIL._imagingtk", "ImageTk", "PIL.ImageTk", "FixTk"],
			"packages" : ["MySQLdb", "kinterbasdb", "psycopg2", "reportlab",
				"wx.aui", "wx.calendar", "wx.gizmos", "wx.grid", "wx.html", "wx.lib.buttons", 
				"wx.lib.calendar", "wx.lib.foldpanelbar", "wx.lib.hyperlink", "wx.lib.masked", 
				"wx.lib.mixins.listctrl", "wx.lib.pdfwin", "wx.lib.plot", "wx.py", "wx.stc"]} },
	)

# To build, run:
#
# python setup.py py2exe --bundle 1
