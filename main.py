import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
from fpdf.enums import XPos, YPos

# create list of excel files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # get data from excel file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Create pdf
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # get data from name of files
    filename = Path(filepath).stem
    invoice_number, date = filename.split("-")

    # Add to page invoice number
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=(f"Invoice nr.{invoice_number}"),
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add to page data invoice
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=(f"Date: {date}"),
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # excecute PDF
    pdf.output(f"PDFs/{filename}.pdf")