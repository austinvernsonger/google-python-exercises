#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it (Done)
 -Extract the names and rank numbers and just print them (Done)
 -Get the names data into a dict and print it (Done)
 -Build the [year, 'name rank', ... ] list and print it (Done)
 -Fix main() to use the extract_names list (Done)
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # Names Hashtable
  rankDb = {}
  rankList = []

  # Compile regular expression
  rYear = re.compile(r'Popularity in (\d\d\d\d)')
  rName = re.compile(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>')

  # Extract the year
  f = open(filename, 'r')
  fileStr = f.read()

  # Parse year and name ranks
  year = re.search(rYear, fileStr)
  ranks = re.findall(rName, fileStr)
  
  # Insert ranks into Db
  for rank in ranks:
    rankDb[rank[1]] = rank[0]
    rankDb[rank[2]] = rank[0]

  def rankHelper(s):
    return s[0]

  # Construct the return year or skip if file isn't the right format
  if year:
    rankList.append(year.group(1))
  else: 
    print "skipping over %s: Year Not Found" % filename
    return 

  # Sort and add result list  
  for k,v in sorted(rankDb.items(), key=rankHelper):
    rankList.append("%s %s" % (k, v))
  
  f.close()
  return rankList


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    result = extract_names(filename)
    if result:
      if summary:
        summaryfile = open('%s.summary' % filename, 'w')
        summaryfile.write('\n'.join(result) + '\n')
        summaryfile.close()
      else:
        print '\n'.join(result) + '\n'
   
  
if __name__ == '__main__':
  main()
