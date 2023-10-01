from PyPDF2 import PdfWriter, PdfReader
import os, errno

filename = "long-sample.pdf"
directory = "splitted/"+filename

def split(directory, filename):
    inputpdf = PdfReader(open(filename, "rb"))
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for i in range(len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[i])
        with open(directory+ "/%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

if __name__ == "__main__":
    split(directory, filename)
