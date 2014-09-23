#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

spFiles = {} # global dictionary for keeping one copy of file

def copy_special_path(dir):  
  """
    Given a directory 'dir' return absolute file path of a 
    matching pattern 'e.g: __word__txt'
  """ 
  rSP = re.compile(r'__\w+__') # special path pattern 'e.g: __word__.txt'  

  try:
    # find all files in an existing 'dir' directory that matches the special path regular expression match
    files = []
    print ".............................\nChecking Directory: %s" % (os.path.abspath(dir)) 
    for f in os.listdir(dir): # both files and directories
      path = os.path.join(dir, f) 
      if (os.path.isfile(path) and re.search(rSP, f)): # only include matched special path and files
        if(f in spFiles): # discard and error out duplicate file names
          print "DUPLICATE FILES FOUND!"
          print "File %s already exists in %s/%s" % (path, spFiles[f], f)
          sys.exit(1)
        else:
          files.append(path)
          spFiles[f] = os.path.abspath(dir)
    print "Found %d files:" % len(files)      
    for v in files:
      print "%s" % v
  except OSError, e:
    print e
    sys.exit(1)    
  except Exception, e:
    raise
    sys.exit(1)
  return files     
  
def zip_to(paths, zippath):
  files = []
  for path in paths:
    files += copy_special_path(path) 

  cmd = 'zip -j %s %s' % (zippath, ' '.join(files))
  print 'Executing Command: %s' % (cmd)

  (status, output) = commands.getstatusoutput(cmd) # 
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  print output
  return

def copy_to(paths, dir):
  """
  Given a list of files 'paths' copy to 'dir' 
  Create 'dir' if it doesn't exist
  """
  for path in paths:
    files = copy_special_path(path)
    for f in files:
      if os.path.exists(os.path.abspath(dir)):
        shutil.copy(f, dir)
      else: 
        os.mkdir(dir)
        shutil.copy(f, dir)
    print ".....................................\nCopied %d files to %s" % (len(files), os.path.abspath(dir))
  return  

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':  
    todir = args[1]
    del args[0:2]
    copy_to(args, todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zip_to(args, tozip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if (todir == '' and tozip == ''): 
    for arg in args:
      copy_special_path(arg)
    

  # +++your code here+++
  # Call your functions

  
if __name__ == "__main__":
  main()
