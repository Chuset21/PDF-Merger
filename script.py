import PyPDF2


def main():
    with open('./PDF\'s/dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(reader.getPage(0).rotateClockwise(180))
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


if __name__ == '__main__':
    main()
