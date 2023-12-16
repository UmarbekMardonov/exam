import PyPDF2


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        # PDF faylining umumiy sahifalar soni
        num_pages = pdf_reader.numPages

        # Har bir sahifani o'qish
        for page_number in range(num_pages):
            page = pdf_reader.getPage(page_number)
            text = page.extractText()
            print(f"Page {page_number + 1}:\n{text}\n")


# Fayl nomini o'zgartiring
pdf_file_path = 'sizning_faylingiz.pdf'

# PDF faylini o'qish
read_pdf(pdf_file_path)
