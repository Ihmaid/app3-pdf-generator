from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.set_font(family="Times", size=24, style="B")
    pdf.add_page()
    pdf.cell(w=0, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 17, 200, 17)
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.cell(w=0, txt=row["Topic"], ln=1, align="L")

pdf.output("output.pdf")
