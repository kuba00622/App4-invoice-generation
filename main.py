import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
from fpdf.enums import XPos, YPos

# create list of excel files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

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

    # get data from excel file
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = list(df.columns)
    columns = [item.replace("_"," ").title() for item in columns]

    # create name_columns row; Header
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, text=columns[0], border=1)
    pdf.cell(w=60, h=8, text=columns[1], border=1)
    pdf.cell(w=40, h=8, text=columns[2], border=1)
    pdf.cell(w=30, h=8, text=columns[3], border=1)
    pdf.cell(w=30, h=8, text=columns[4], border=1,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, text=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, text=str(row['product_name']), border=1)
        pdf.cell(w=40, h=8, text=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, text=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, text=str(row['total_price']), border=1,
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # count total price
    total_price = sum(df["total_price"])

    # Add total price row
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, text="", border=1)
    pdf.cell(w=60, h=8, text="", border=1)
    pdf.cell(w=40, h=8, text="", border=1)
    pdf.cell(w=30, h=8, text="", border=1)
    pdf.cell(w=30, h=8, text=str(total_price), border=1,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add total_price sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, text=f"The total price is {total_price}",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Add company name and log
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=325, h=8, text=f"PythonHow")
    pdf.image("pythonhow.png", w=10)



    # excecute PDF
    pdf.output(f"PDFs/{filename}.pdf")