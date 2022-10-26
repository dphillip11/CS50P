from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_text_color(0, 0, 0)
        self.set_font("helvetica", style="", size=50)
        self.cell(190, 50, "CS50 Shirtificate", align="C")
        self.ln(20)


pdf = PDF(orientation="portrait", format="A4")
pdf.set_text_color(250, 250, 250)
pdf.add_page()
pdf.image('shirtificate.png', 20, 70, pdf.w - 40, pdf.h -110)
pdf.set_font("helvetica", style="", size=30)
text = input("Name: ") + " took CS50"
pdf.cell(190, 210, txt=text, align="c")

pdf.output("shirtificate.pdf")