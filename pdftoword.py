from pdf2docx import Converter,parse

pdf_file = 'demo.pdf'
word_file = 'demo.docx'

cv=Converter(pdf_file)
cv.convert(word_file,start=0,end=None)
cv.close()

#parse(pdf_file, word_file,start=0,end=None)