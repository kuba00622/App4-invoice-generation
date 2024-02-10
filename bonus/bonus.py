import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
from fpdf.enums import XPos, YPos

# Create a list of filepaths
filepaths = glob.glob("files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    # Create page
    pdf.add_page()

    # Convert filename to title case
    name = Path(filepath).stem
    header = name.split(".")[0].title()

    # Add the title to PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, text=(header), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Produce the PDF
pdf.output("output.pdf")