from pypdf import PdfWriter
merge = PdfWriter()
PDFS = [
    r"C:\Users\evilk\OneDrive\Desktop\Python\Python Advance\PDf\1.pdf",
    r"C:\Users\evilk\OneDrive\Desktop\Python\Python Advance\PDf\2.pdf",
    r"C:\Users\evilk\OneDrive\Desktop\Python\Python Advance\PDf\3.pdf",
    r"C:\Users\evilk\OneDrive\Desktop\Python\Python Advance\PDf\4.pdf",
]

for pdf in PDFS:
    merge.append(pdf)
    
    
merge.write(r"C:\Users\evilk\OneDrive\Desktop\Python\Python Advance\PDf\merged.pdf")
merge.close()