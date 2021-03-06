import backend.PySimpleGUI as sg
import backend.NARCFunctions as nf
sg.theme('DefaultNoMoreNagging')


layout = [[sg.Text('Path of NARC to extract')],
					[sg.In(), sg.FileBrowse()],
					[sg.Button('Extract'), sg.Button('Extract and Decompress')],
					[sg.Text('Directory of NARC subfiles to compile')],
					[sg.In(), sg.FolderBrowse()],
					[sg.Button('Compile'), sg.Button('Compile and Compress')],
					[sg.Text('NARCs are compiled to the same folder as your extracted data')],
					[sg.Exit(pad=((5,5),(20,3))), sg.Button('About', pad=((5,5),(20,3)))]
				 ]

window = sg.Window('NARCTool 0.3', layout)

while True:
		event, values = window.Read()
		if event is None or event == 'Exit':
			break
		if event == 'Extract':
			nf.extract(values[0])
		elif event == 'Extract and Decompress':
			nf.extractDecompress(values[0])
		elif event == 'Compile':
			nf.compile(values[1])
		elif event == 'Compile and Compress':
			nf.compileCompress(values[1])
		elif event == 'About':
			sg.Popup('NARCTool v0.3', f'Downloaded from github.com/VendorPC', f'Source code dumped by Vendor', f'Modifications and GUI made by FrankieD', title = 'About')

window.close()