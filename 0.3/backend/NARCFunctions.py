import ntpath
from backend.NARC import *

def extract(narc):
	try:
		if os.path.exists("./extracted"):
			NARC_Unpack(narc, "./extracted/" + ntpath.split(narc)[1][:-5], False)
		else:
			os.mkdir("./extracted")
			NARC_Unpack(narc, "./extracted/" + ntpath.split(narc)[1][:-5], False)
	except:
		pass

def extractDecompress(narc):
	try:
		if os.path.exists("./extracted"):
			NARC_Unpack(narc, "./extracted/" + ntpath.split(narc)[1][:-5])
		else:
			os.mkdir("./extracted")
			NARC_Unpack(narc, "./extracted/" + ntpath.split(narc)[1][:-5])
	except:
		pass


def compile(narcDir):
	try:
		NARC_Pack(narcDir, narcDir, False)
	except:
		print('Something went wrong. Errors are most commonly caused by leftover files. Check your directory for leftover files and try again (e.g. a backup of a file edited with HxD).')
		pass


def compileCompress(narcDir):
	try:
		NARC_Pack(narcDir, narcDir)
	except:
		print('Something went wrong. Errors are most commonly caused by leftover files. Check your directory for leftover files and try again (e.g. a backup of a file edited with HxD).')
		pass