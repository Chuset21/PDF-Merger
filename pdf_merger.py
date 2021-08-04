import PyPDF2
import sys


def pdf_merger(pdf_list: list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


if __name__ == '__main__':
    pdf_merger(sys.argv[1:])
