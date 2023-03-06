from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format="A4")
#Prevents the inputs to the page from moving onto the next page
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv", sep=",")

#Purpose: Main loop to loop through topics.csv
for index,row in df.iterrows():    
    #Create a new page for pdf
    pdf.add_page()
    #Any cells created after the font will have the same font

    pdf.set_font(family="Times", style="B",size=24)
    pdf.set_text_color(100,100,100) 
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    
    #Creates the lines in document
    line_gap = 22
    while line_gap < 290:
        pdf.line(10,line_gap,200,line_gap)
        line_gap = line_gap + 6

    #Purpose: Sets the footer
    #pdf.ln specifies breakline between previous "cell"(title) not start of page
    pdf.ln(265)
    pdf.set_font(family="Times", style="B",size=8)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    #Purpose: Add additional Pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="B",size=8)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        
        #Creates the lines in document
        line_gap = 22
        while line_gap < 290:
            pdf.line(10,line_gap,200,line_gap)
            line_gap = line_gap + 6


pdf.output("output.pdf")