#!/usr/bin/env python
# -*- coding: utf-8 -*-
### dotamatic
###
### Copyright (C) 2003-2004 Roger Binns <rogerb@rogerbinns.com>
### Copyright (C) 2003-2004 Steven Palm <n9yty@n9yty.com>
###
### This file is free software; you can redistribute it and/or modify
### it under the terms of any license of your choice listed at
### http://www.opensource.org/licenses/
###
### $Id: makedist.py,v 1.2 2004/06/30 17:14:30 rogerb Exp $


# Runs on Linux, Windows and Mac

"""Builds a binary distribution of dotamatic

This code runs on Windows, Linux and Mac, and will create binary distributions
suitable for mass use"""

import os
import shutil
import sys
import glob
import re

def rmrf(path):
	"""Delete directory tree like rm -rf does"""
	entries=os.listdir(path)
	for e in entries:
		fullname=os.path.join(path,e)
		if os.path.isdir(fullname):
			rmrf(fullname)
		else:
			os.remove(fullname)
	os.rmdir(path)

def run(*args):
	"""Execute the command.

	The path is searched"""
	print "args"
	sl=os.spawnl
	if sys.platform!="win32":
		sl=os.spawnlp
		ret=apply(sl, (os.P_WAIT,args[0])+args)
	else:
		# win98 was fine with above code, winxp just chokes
		# so we call system() instead
		str=""
		for a in args:
			if a.find(" ")>=0:
				str+=' "'+a+'"'
			else:
				str+=" "+a
		str=str[1:] # remove first space
		# If you ever wanted proof how idiotic windows is, here it is
		# if there is a value enclosed in double quotes, it is
		# taken as the window title, even if it comes after all
		# the switches, so i have to supply one, otherwise it mistakes
		# the command to run as the window title
		ret=os.system('start /b /wait "%s" %s' % (args[0], str))
	print "returned", ret

def clean():
	"""Remove temporary directories created by various packaging tools"""
	if os.path.isdir("dist"):
		rmrf("dist")
	if os.path.isdir("build"):
		rmrf("build")
	for file in ["setup.cfg"]:
		if os.path.isfile(file):
			os.remove(file)

def resources():
	"""Get a list of the resources (images, executables, sounds etc) we ship

	@rtype: dict
	@return: The key for each entry in the dict is a directory name, and the value
			 is a list of files within that directory"""
	tbl={}
	# list of files
	exts=[ "*.png",  "*.jpg", "*.css", "*.htb" ]
	if sys.platform=="win32":
		# on windows we also want the help file and the manifest needed to get Xp style widgets
		exts=exts+["*.chm", "*.manifest"]
	# list of directories to look in
	dirs=[ os.path.join(".", "resources"), ".", "/usr/local/lib/python2.3/site-packages/dabo/icons" ]
	for wildcard in exts:
		for dir in dirs:
			for file in glob.glob(os.path.join(dir, wildcard)):
				d=os.path.dirname(file)
				if not tbl.has_key(d):
					tbl[d]=[]
				tbl[d].append(file)

	files=[]
	for i in tbl.keys():
		files.append( (i, tbl[i]) )

	return files

def copyresources(dest):
	"""Copies the resources to the specified destination directory.

	The directory structure is preserved in the copy"""
	for dir,files in resources():
		if not os.path.exists(os.path.join(dest,dir)):
			os.makedirs(os.path.join(dest,dir))
		for file in files:
			print file
			shutil.copy(file, os.path.join(dest, file))

def getsubs():
	"""Gets the list of substitutions to be performed on the template files

	A partial current list is:
		- VERSION: The full version number of the product
		- OUTFILE: The filename of resulting installer (Windows specific)
		- NAME:	   The product name (in lower case)
		- RELEASE: The release is an increment if multiple releases are
				   made of the same version.  This corresponds to the last
				   part of the filename for RPM packages

	@rtype: dict
	"""
	# Get version info
	import version
	
	verstr=version.version
	if version.testver:
		verstr+="-test"+"version.testver"
	import socket

#	  h=socket.gethostname().lower()
#	  if h!="rogerb" and h!="home.rogerbinns.com" and h!="roger-sqyvr14d3" \
#		 and h!="uibook.n9yty.com" and h!="uibook.local.":
#		  # not built by rogerb (or stevep/n9yty) therefore unofficial
#		  verstr+="-unofficial"

	filename="daboEngine-"+verstr+"-setup"

	if sys.platform=="linux2":
		# linux needs all the dash bits as underscores
		verstr=re.sub("-", "_", verstr)
			


	res={}
	res["VERSION"]=verstr
	res["OUTFILE"]=filename
	res["NAME"]=version.name.lower()
	res["RELEASE"]=version.release
	res["COPYRIGHT"]=version.copyright
# 	res["DQVERSION"]=".".join(["i" for i in version.dqver])
	res["DESCRIPTION"]=version.description
	res["COPYRIGHT"]=version.copyright
	res["URL"]=version.url
	return res

def dosubs(infile, outfile, subs):
	"""Performs substitutions on a template file

	@param infile:	filename to read
	@param outfile: filename to write resutl to
	@type subs: dict
	@param subs: the substitutions to make
	"""
	f=open(infile, "r")
	stuff=f.read()
	f.close()

	for k in subs:
		stuff=re.sub("%%"+k+"%%", subs[k], stuff)

	f=open(outfile, "w")
	f.write(stuff)
	f.close()


def windowsbuild():
	"""Do all the steps necessary to make a Windows installer"""
		
	# clean up
	clean()
	# need setup.cfg with version info in it
	v=getsubs()
	# Build python and stuff
	run( "c:\\python23\python", "p2econfig.py", "py2exe", "-O2")

	v=getsubs()
	dosubs("daboEngine.iss", "daboEngine-out.iss", v)
	filename=v["OUTFILE"]

	# Run innosetup
	### TODO - fix path!
	run("c:\\program files\\inno setup 4\\compil32.exe", "/cc", "daboEngine-out.iss")

	# copy to S: drive
	if os.path.isdir("s:\\"):
		shutil.copyfile("dist\\"+filename+".exe", "s:\\"+filename+".exe")

def linuxbuild():
	"""Do all the steps necessary to make a Linux RPM"""
	try:
		rmrf("i386")
	except:
		pass
	clean()
	os.mkdir("dist")
	cxfreezedir="/home/ed/cx_Freeze"
	j=os.path.join
	run("env", "PYTHONOPTIMIZE=2", "PATH=%s:%s" % (cxfreezedir, os.environ["PATH"]), "FreezePython", "--install-dir="+os.path.abspath("dist"),
		"--base-binary="+j(cxfreezedir, "ConsoleSetLibPathBase"), "-t", "daboEngine.py")
	copyresources("dist")
	v=getsubs()
	instdir="/usr/lib/%s-%s" % (v["NAME"], v["VERSION"])
	run("sh", "-c", "cd dist ; ../unixpkg/rpathfixup "+instdir)
	run("sh", "-c", "cd dist ; tar cvf ../dist.tar *")
	clean()
	os.mkdir("dist")
	for f in glob.glob("unixpkg/*"):
		if os.path.isfile(f):
			shutil.copy(f, "dist")

	dosubs("unixpkg/daboEngine.spec", "dist/daboEngine.spec", v)
	shutil.copy("dist.tar", "dist")
	os.remove("dist.tar")

	n="%s-%s" % (v["NAME"], v["VERSION"])
	try:
		rmrf(n)
	except:
		pass
	
	os.rename("dist", n)
	run("tar", "cvfz", n+".tar.gz", n)
	rmrf(n)
	run("rpmbuild", "-ta", "--define=_rpmdir %s" % (os.getcwd(),), "--target", "i386-linux", n+".tar.gz")
	os.remove(n+".tar.gz")
	
def macbuild():
	"""Do all the steps necessary to make a Mac dimg"""
	try:
		rmrf("dist")
	except:
		pass
	clean()
	os.mkdir("dist")
	import bundlebuilder
	import string
	myapp = bundlebuilder.AppBuilder(verbosity=1)
	packageroot="."
	myapp.mainprogram = os.path.join(packageroot, "daboEngine.py")
	myapp.standalone = 1
	myapp.name = "daboEngine"
	myapp.strip = 1
	myapp.builddir = "dist"
	myapp.iconfile="daboEngine.icns"
	v=getsubs()
	verstr = "%s-%s" % (v["NAME"], v["VERSION"])
	myapp.plist.CFBundleShortVersionString=verstr
	for dir,files in resources():
		for file in files:
			fname = os.path.basename(file)
			myapp.files.append( (os.path.join(dir, fname), os.path.join("Contents", "Resources", dir, fname)))
	
	# hardcoded for the moment as bundlebuilder doesn't know how to look for them
	myapp.libs.append("/usr/local/lib/libwx_mac-2.4.0.dylib")
	myapp.libs.append("/usr/local/lib/libwx_mac-2.4.0.rsrc")
	myapp.libs.append("/usr/local/lib/libwx_mac_gl-2.4.0.dylib")

	myapp.setup()
	myapp.build()
	if (os.uname()[2] >= "7.0.0"):
		ret=os.system("hdiutil create -srcfolder dist -volname daboEngine -nouuid -noanyowners dist/PANTHER-%s.dmg" % verstr)
		print "image creation returned", ret
	else:
		# print "Create disk image with dist folder as the source in DiskCopy with name:\n	  -> JAGUAR-%s.dmg <-." % verstr
		ret=os.system("/usr/local/bin/buildDMG.pl -buildDir=dist -compressionLevel=9 -volName=daboEngine -dmgName=JAGUAR-%s.dmg dist/daboEngine.app" % verstr)
		print "image creation returned", ret

if __name__=="__main__":
	if sys.platform=="win32":
		windowsbuild()
	elif sys.platform=="linux2":
		linuxbuild()
	elif sys.platform=="darwin":
		macbuild()
	else:
		print "Unknown platform", sys.platform

