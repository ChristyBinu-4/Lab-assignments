import PyPDF2 as py

pdf = open('pdf.pdf', 'rb')
pdf_reader = py.PdfReader(pdf) 

page = pdf_reader.pages[0]
text = page.extract_text()

print(text)
pdf.close()