import PyPDF2
import sys


def main():
    template_file = sys.argv[1]

    try:
        watermark_file = sys.argv[2]
    except IndexError:
        watermark_file = 'default_watermark.pdf'

    template = PyPDF2.PdfFileReader(open(template_file, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark_file, 'rb')).getPage(0)
    output = PyPDF2.PdfFileWriter()
    output_name = 'watermarked_output.pdf'

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark)
        output.addPage(page)

        with open(output_name, 'wb') as file:
            output.write(file)


if __name__ == '__main__':
    main()
