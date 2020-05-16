import sys
import os
from NARC import *

narcs = []

for file in os.listdir(os.getcwd()):
	if file.endswith("_extracted"):
		narcs.append(file)

for narc in narcs:
	NARC_Pack(narc, narc)
