import sys
from NARC import *

if len(sys.argv) > 2:
    if sys.argv[1].lower() == "extract":
        text = input("Do you want to decompress the files when you extract? (Y/N)")
        if text.lower() == "n":
            NARC_Unpack(sys.argv[2], sys.argv[3], False)
        else:
            NARC_Unpack(sys.argv[2], sys.argv[3])
    elif sys.argv[1].lower() == "compile":
        text = input("Do you want to compress the files when you compile? (Y/N)")
        if text.lower() == "n":
            NARC_Pack(sys.argv[2], sys.argv[3], False)
        else:
            NARC_Pack(sys.argv[2], sys.argv[3])
else:
    print("Usage:\n\nTo decompile: python NARCTool.py extract <NARC> <output directory>\nTo compile: python NARCTool.py compile <extracted NARC> <output directory>")
