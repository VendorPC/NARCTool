# Original tool developed by PlatinumMaster

# Version History

# NARCTool 0.4

### Updated and maintained by FrankieD

#### An .exe version that does not require Python has been compiled for Windows users.

Changelog:

Some scripts were optimized

About popup has been updated

An error popup has been added to "Compile" and "Compile and Compress" upon failure

A bug causing NARCTool GUI to continue running in the background when closing with the X button has been fixed

# NARCTool 0.3

### Credits to FrankieD for creating the GUI and custom scripts

A GUI has been created in favor of multiple scripts

If you wish to continue using individual scripts please use version 0.2-p

# NARCTool 0.2-p

### Modified by FrankieD, Vendor, and Zekromaegis

Simplified scripts were created for quicker use

Extract.py

All files ending in ".narc" will be extracted

Place your NARC(s) in this folder and run "Extract.py"

A new folder will appear named after the NARC(s) you extracted followed by "_extracted"

Compile.py

All folders ending with "_extracted" will be compiled

After running Compile.py your compiled NARC(s) will appear in the same folder your NARC(s) were extracted to

Although they are very rarely used I included Compress/Decompress variants of the above scripts

Should either script not function as expected run NARCTool.py in Windows CMD or a CMD equivalent

# narctool 0.1-p

### This is the original, untouched source code dumped by Vendor. Only use this version if you plan to modify the source code yourself. Below is the readme included in the dump of 0.1-p.

This modified version of narctool has been made so that it works with

filename-less NARC files like those in Pokemon Diamond and Pearl by

creating files named (narc_name).(file_number).(file_type)

Refer to the original readme, below:

narctool 0.1 - by natrium42

Tool for working with NARC and compressed NARC files (CARC files).

See narc.h for description of NARC file format.

Run without arguments for help.

Parts of code use work by Haruhiko Okumura and Andre Perrot,
