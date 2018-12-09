#!/usr/bin/python

import os
import sys, getopt

"""
Core
"""
def printBigFileSize(fileSize, outputSize = False):
  def compareAndPrintBigFileSize (file):
    if (os.path.getsize(file) >= fileSize):
      size = os.path.getsize(file)
      if (outputSize):
        print ("%s (%d MB / %d Bytes)" % (file, size / 1024 / 1024, size))
      else:
        print (file)
  return compareAndPrintBigFileSize

def parseFolderTree(path, callback):
  for file in os.listdir(path):
    pathFile = os.path.join(path, file)
    if os.path.isfile(pathFile):
      callback(pathFile)
    elif os.path.isdir(pathFile) and not os.path.islink(pathFile):
      parseFolderTree(pathFile, callback)


"""
Helpers
"""
def printHelp():
  print ('bigfile help \n')
  print ('Basic usage: bigfile -f 300 -d /home/me -o \n')
  print ('-f, --fileSize   <int|float> [required] [the size in MB of the files you are looking for.]')
  print ('-d, --dir        <string>    [required] [the directory path from where you want to start.]')
  print ('-o, --outputSize                        [will output the files size in the results.] [default false]')

def fromMBToBytes(value):
  return value * 1024 * 1024

def fromBytesToMB(value):
  return value / 1024 / 1024

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass

  return False

"""
Entrypoint
"""
def main(argv):
  path = None
  fileSize = None
  outputSize = False
  try:
    opts, args = getopt.getopt(argv,"hod:f:",["dir=", "fileSize=", "outputSize", "help"])
  except getopt.GetoptError:
    printHelp()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      printHelp()
      sys.exit()
    elif opt in ("-d", "--dir"):
      path = arg
    elif opt in ("-f", "--fileSize"):
      fileSize = arg
    elif opt in ("-o", "--outputSize"):
      outputSize = True

  # validation
  try:
    fileSize = float(fileSize)
  except:
    print ("file size should be a number")
    printHelp()
    sys.exit(2)
  if not path or not os.path.isdir(path):
    print ("dir is not a valid directory")
    printHelp()
    sys.exit(2)
  print ("searching %s MB files in %s " % (fileSize, path))
  try:
    parseFolderTree(path, printBigFileSize(fromMBToBytes(fileSize), outputSize))
    print("Done!")
  except (KeyboardInterrupt, SystemExit):
    print("\nAborted ...\nBye!")

if __name__ == "__main__":
    main(sys.argv[1:])