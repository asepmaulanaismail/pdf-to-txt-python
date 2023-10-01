import PyPDF2
import Split
from subprocess import call
import sys

if (len(sys.argv) < 2):
    print("Error\nFormat: \n\tpython main.py your-pdf-file")
else:
    filename = sys.argv[1]
    directory = "splitted/" + filename

    Split.split(directory, filename)
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    for i in range(len(pdfReader.pages)):
        splitted_file_name = directory + "/" + repr(i)
        call(["pdftotext", splitted_file_name + ".pdf"])
        f = open(splitted_file_name + '.txt', 'r')
        print("Page %s" % repr(i+1))
        print(f.read())
        print("====================")
