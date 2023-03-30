from PyPDF2 import PdfMerger

pdfs = ["one.pdf", "two.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

# If you want to use append method and append certain pages
# merger = PdfMerger()

# merger.append("one.pdf")
# merger.append("two.pdf")
# merger.append("three.pdf", pages=(0, 4, 2))

merger.write("merged.pdf")
merger.close()

# The example one.pdf and two.pdf are the files that I had in my directory that were named that. 
# You have to use the correct file name (within the same directory) to merge the pdf files. 
