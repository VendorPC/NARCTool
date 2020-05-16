import ntpath
import backend.PySimpleGUI as sg
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
		sg.Popup('Something went wrong.', f'Errors are most commonly caused by leftover files.', f'Check your directory for leftover files and try again.', f'E.g. a backup of a file edited with HxD or a NARC', title = 'Error')
		pass


def compileCompress(narcDir):
	try:
		NARC_Pack(narcDir, narcDir)
	except:
		sg.Popup('Something went wrong.', f'Errors are most commonly caused by leftover files.', f'Check your directory for leftover files and try again.', f'E.g. a backup of a file edited with HxD or a NARC', title = 'Error')
		pass