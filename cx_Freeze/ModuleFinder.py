"""Wrapper for the standard library Python module modulefinder which manages
   a few of the things that the standard module does not manage."""

import glob
import imp
import modulefinder
import os
import shutil
import sys

# ensure that PyXML is handled properly if found
modulefinder.ReplacePackage("_xmlplus", "xml")

class ModuleFinder(modulefinder.ModuleFinder):
    """Subclass of modulefinder which handles a few situations that the
       base class does not handle very well."""

    def __init__(self, excludes):
        modulefinder.ModuleFinder.__init__(self, excludes = excludes)
        self.dependentFiles = {}

    def AddDependentFile(self, sourceName, targetName = None):
        """Add a dependent file to the list of dependent files."""
        if targetName is None:
            targetName = os.path.basename(sourceName)
        self.dependentFiles[targetName] = sourceName

    def CopyDependentFiles(self, dir, listFileName = None):
        """Copy the required files to the directory and optionally include the
           list of files in the file specified."""
        if sys.platform == "win32":
            self.AddDependentFile(sys.dllname)
        for targetName, sourceName in self.dependentFiles.iteritems():
            print "Copying", sourceName
            targetName = os.path.join(dir, targetName)
            if os.path.exists(targetName):
                os.remove(targetName)
            shutil.copy2(sourceName, targetName)
        if listFileName is not None:
            fileNames = [os.path.join(dir, n) for n in self.dependentFiles]
            fileNames.sort()
            print >> file(listFileName, "w"), "\n".join(fileNames)

    def find_module(self, name, path, parent = None):
        """Find the module and return a reference to it."""
        if path is None and name in ("pythoncom", "pywintypes"):
            module = __import__(name)
            return None, module.__file__, (".dll", "rb", imp.C_EXTENSION)
        return modulefinder.ModuleFinder.find_module(self, name, path, parent)

    def load_module(self, fqname, fp, path, stuff):
        """Load the module and return a reference to it."""
        try:
            module = modulefinder.ModuleFinder.load_module(self, fqname, fp,
                    path, stuff)
        except SyntaxError, value:
            raise "Module %s from file %s has %s." % (fqname, path, value)
        if fqname in ("wxPython.wxc", "wx._core_", "wx._stc", "wx._gizmos",
              "wx._glcanvas", "wx._ogl", "wx._xrc"):
            if sys.platform == "win32":
                dir = os.path.dirname(module.__file__)
                for dll in glob.glob(os.path.join(dir, "wx*.dll")):
                    self.AddDependentFile(dll)
            else:
                for line in os.popen("ldd %s" % module.__file__).readlines():
                    line = line.strip()
                    if not line.startswith("libwx"):
                        continue
                    libName, libLocation = line.split(" => ")
                    if libLocation == "not found":
                        raise "Library %s not found." % libName
                    self.AddDependentFile(libLocation.split()[0])
        return module

    def load_file(self, pathname, moduleName):
        """Load a module from a given file."""
        fp = file(pathname, "r")
        name, ext = os.path.splitext(pathname)
        stuff = (ext, "r", imp.PY_SOURCE)
        self.load_module(moduleName, fp, pathname, stuff)

