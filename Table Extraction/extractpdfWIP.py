from pathlib import Path
import camelot.io as camelot

from tabula import read_pdf
from tabulate import tabulate


'''
pdf_path = (
    Path.home()
    / "desktop/sampletables.pdf"
)
df = read_pdf(str(pdf_path), pages=1)
df[0]
'''

df = read_pdf("file:///Users/shrisimac/Desktop/Python%20Automation/Table%20Extraction/sampletables.pdf",
              pages="all")  # address of pdf file
print(tabulate(df))

#tables = camelot.read_pdf('sampletables.pdf', pages='1', flavor='stream',table_areas=['0,800,800,0'])
#print(tables)


#
