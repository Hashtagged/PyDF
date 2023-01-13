# PyDF
A simple Python script that generates a PDF from a text or image file using PySimpleGUI and PyPDF2.

## Usage
- Run the script.
- In the window that appears, choose an image or text file by either typing the file path or using the "File Browse" button.
- Click the "Generate PDF" button.
- The generated PDF will be saved as "generated_pdf.pdf" in the same directory as the script.

## Requirements
- PySimpleGUI
- PyPDF2
- PIL (if generating PDF from image)

## Error Handling
- If an invalid file type is chosen, an error message will appear in the output window.
- If any other unexpected error occurs, the error message will be printed in the output window.

## Note
- If you are generating PDF from image, make sure that you have PIL library installed.
- The script will work only on Windows, Mac and Linux systems.

## Features
- Generates PDF from text files and image files(jpg,png)
- User-friendly GUI using PySimpleGUI
- Error handling for invalid file types and unexpected errors
- Outputs success message upon successful PDF generation

## How it works
The script uses PySimpleGUI to create a graphical user interface for the user to select a file and generate a PDF. The chosen file is then processed using PyPDF2 or PIL(if generating PDF from image) to convert the file into a PDF and save it as "generated_pdf.pdf" in the same directory as the script.

## Customization
- You can change the name of the output file by modifying the following line of code:
``` with open('generated_pdf.pdf', 'wb') as outfile:```
- You can also change the size and font of the text in the GUI by modifying the following line of code:
``` layout = [[sg.Text('Generate PDF', size=(20, 1), font=("Helvetica", 25))],```

## Conclusion
This script provides a simple and efficient way to generate a PDF from a text or image file, making it a useful tool for anyone who regularly needs to convert files into PDF format. It is easy to use and customize, and provides error handling to ensure a successful PDF generation. So you can use this script to automate the process of converting text and image files into PDFs.
