# PDF to Text with Python

## Introduction

This program will:

1. Split your PDF into pages,
2. Extract the text from each pages, and
3. Save them in `.txt` file.

## Required
- [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) ([Why using this?](#whyme))
- [PyPDF2](https://github.com/mstamy2/PyPDF2)

## Run
```
$ python main.py <your-pdf-file>
```

## <a name="whyme"></a> Why Using PDFtk?

Because PyPDF2's extract function doesn't works on some files.