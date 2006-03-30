
from distutils.core import setup
import glob
import py2exe

setup(
	# The first three parameters are not required, if at least a
	# 'version' is given, then a versioninfo resource is built from
	# them and added to the executables.
	version = "0.6.2",
	description = "Dabo Runtime Engine",
	name = "daborun",
#- 	data_files=[ ("", glob.glob("\\projects\\dabo\\icons\\*.png")) ],
	# targets to build
#	console = ["daborun.py"],
	windows = ["daborun.py"],
	#exclude the actual framework
	options = { "py2exe": 
			{"includes" : ["ConfigParser", "threading", "mx.DateTime", "winpdb"],
			"excludes" : ["dabo", "dabo.db", "dabo.biz", "dabo.lib", "dabo.ui", 
				"dabo.common", "dabo.icons", "dabo.ui.uiwx"],
			"packages" : ["MySQLdb", "encodings", "kinterbasdb", "pysqlite2",
				"wx.gizmos", "wx.lib.calendar", "wx.lib.foldpanelbar", 
				"wx.lib.hyperlink", "reportlab", "PIL"]} },
	)

# To build, run:
#
# python setup.py py2exe --bundle 1