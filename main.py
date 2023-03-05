from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format="A4")

df = pd.read_csv("topics.csv", sep=",")
for index,row in df.iterrows():    
#Create a new page for pdf
    pdf.add_page()
#Any cells created after the font will have the same font

    pdf.set_font(family="Times", style="B",size=24)
    pdf.set_text_color(100,100,100) 
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    
    pdf.line(10,22,200,22)


pdf.output("output.pdf")