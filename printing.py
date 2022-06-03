# Define all methods to print objects
from fpdf import FPDF

import constants


# Python program to create
# a pdf file


def print_blocks(blocks):
    # save FPDF() class into a
    # variable pdf
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=15)
    for block in blocks:
        print_block(block, pdf)
    # save the pdf with name .pdf
    pdf.output("page.pdf")


def print_block(block, pdf):
    if block.type in constants.BLOCK_TYPES:
        pdf.cell(200, 10, txt=block.content, ln=2, align='C')
