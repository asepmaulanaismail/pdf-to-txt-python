import PyPDF2
import Split
from subprocess import call
import sys

if sys.argv[1][-4:] != ".pdf" :
    exit("""\033[;31;m\033[;1;mError
    Format:
    \t\033[;32;m\033[;4;mpython main.py your-pdf-file\033[;0;m""")

filename = sys.argv[1]
directory = "splitted/" + filename

Split.split(directory, filename)
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

for i in range(pdfReader.numPages):
    splitted_file_name = directory + "/" + repr(i)
    call(["pdftotext", splitted_file_name + ".pdf"])
    # f = open(splitted_file_name + '.txt', 'r')
    # print("Page %s" % repr(i+1))
    # print(f.read())
    # print("====================")
