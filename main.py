from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(0, 0, 0)

    pdf.add_page()
    pdf.cell(w=0, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 17, 200, 17)

    pdf.ln(272)
    pdf.set_font(family="Times", size=10, style="I")
    pdf.set_text_color(189, 189, 189)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.set_font(family="Times", size=10, style="I")
        pdf.set_text_color(189, 189, 189)

        pdf.add_page()
        pdf.ln(278)

        pdf.cell(w=0, txt=row["Topic"], align="R")

pdf.output("output.pdf")
