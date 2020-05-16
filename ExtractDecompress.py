import sys
import os
from NARC import *

narcs = []

for file in os.listdir(os.getcwd()):
	if file.endswith(".narc"):
		narcs.append(file)

for narc in narcs:
	NARC_Unpack(narc, narc[:-5] + "_extracted")