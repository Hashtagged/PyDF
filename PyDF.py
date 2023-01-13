import PySimpleGUI as sg  
import os  
import PyPDF2  
import sys  

# Create the main window layout
layout = [[sg.Text('Generate PDF', size=(20, 1), font=("Helvetica", 25))],  
          [sg.Text('Choose an image or text file to generate your PDF', size=(40, 1))],  
          [sg.Input(key='input_file'), sg.FileBrowse()],  
          [sg.Button('Generate PDF', size=(15, 2))],  
          [sg.Text('_' * 80)],  
          [sg.Output(size=(70, 10))]]

# Create the window and show it without the plot
window = sg.Window('PDF Generator', layout)  

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Generate PDF':
        filename = values['input_file']
        try:
            if os.path.splitext(filename)[1] == '.txt':
                with open(filename, 'r') as infile:
                    text = infile.read()

                pdf_file = PyPDF2.PdfFileWriter()
                pdf_file.addBlankPage()
                pdf_file.addPage(pdf_file.makeTextPage(text))

                with open('generated_pdf.pdf', 'wb') as outfile:
                    pdf_file.write(outfile)
                    print('PDF successfully generated!')
            elif os.path.splitext(filename)[1] in ['.jpg', '.png']:
                from PIL import Image

                image = Image.open(filename)
                image.save('generated_pdf.pdf', 'PDF', resolution=100.0)
                print('PDF successfully generated!')
            else:
                print('Error: Invalid file type')
        except:
            print("Unexpected error:", sys.exc_info()[0])

window.close()