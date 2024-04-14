# Import FPDF class
import random

from fpdf import FPDF

# Create instance of FPDF class
# Letter size paper, use inches as unit of measure
pdf = FPDF()

# Add new page. Without this you cannot create the document.
pdf.add_page()

# Effective page width, or just epw
epw = pdf.w - 2 * pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
# col_width = epw / 4

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.
from faker import Factory

fake = Factory.create("en_IN")
student_name = f"{fake.first_name()} {fake.first_name_male()} {fake.last_name_male()}"
student_details = [
    student_name, fake.first_name_female(), f"P11{random.randint(10, 40)}{random.randint(10, 50)}", "Pune", random.randint(1, 40), random.randint(1, 40),
    random.randint(20, 100), random.randint(20, 30), random.randint(1, 40), random.randint(1, 40)
]

subject_idx = 4
subjects = [
    ['Subject Code', 'Subject Name', 'Marks Obtained'],
    [1, 'ENGLISH', student_details[subject_idx]],
    [2, 'MARATHI', student_details[subject_idx + 1]],
    [40, 'MATHEMATICS & STATISTICS', student_details[subject_idx + 2]],
    [54, 'PHYSICS', student_details[subject_idx + 3]],
    [55, 'CHEMISTRY', student_details[subject_idx + 4]],
    [56, 'BIOLOGY', student_details[subject_idx + 5]]
]

font_size = 12.0
pdf.set_font('Arial', '', font_size)
th = pdf.font_size
space = 1.7

max_tb_widths = [epw / 3.5, epw / 2.5, epw / 3.5]

pdf.set_font('Arial', '', 8)
pdf.cell(max_tb_widths[0], 0.0,
         f"{random.randint(1, 27):02d}/{random.randint(6, 12):02d}/2022, {random.randint(1, 24)}:{random.randint(1, 60)}")
pdf.cell(max_tb_widths[1], 0.0, "HSC Result March-2022", align='C')

pdf.ln(space * 2 * th)

pdf.set_font('Arial', 'B', font_size)
pdf.multi_cell(sum(max_tb_widths), space * th,
               "MAHARASHTRA STATE BOARD OF SECONDARY & HIGHER SECONDARY EDUCATION,\nPUNE\nHSC EXAMINATION RESULT "
               "MARCH-2022",
               border=1, align='C')
pdf.ln(0.0)

space = 2.0

name = student_details[0]
pdf.cell(max_tb_widths[0], space * th, "Name:", border=1)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, name, border=1)
pdf.ln(space * th)

mother = student_details[1]
pdf.cell(max_tb_widths[0], space * th, "Mother:", border=1)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, mother, border=1)
pdf.ln(space * th)

seat_no = student_details[2]
pdf.cell(max_tb_widths[0], space * th, "Seat No:", border=1)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, seat_no, border=1)
pdf.ln(space * th)

division = student_details[3]
pdf.cell(max_tb_widths[0], space * th, "Seat No:", border=1)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, division, border=1)
pdf.ln(space * th)

sub_marks = []
for row_idx, row in enumerate(subjects):
    if row_idx == 1:
        pdf.set_font('Arial', '', font_size)
    for idx, datum in enumerate(row):
        if idx == 2 and type(datum) == int:
            sub_marks.append(datum)
        txt = datum
        if type(datum) == int:
            txt = "{:03d}".format(datum)
        pdf.cell(max_tb_widths[idx], space * th, txt, border=1, align='C')
    pdf.ln(space * th)

# print(sub_marks)
pdf.set_font('Arial', 'B', font_size)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, "TOTAL", border=1, align='C')
pdf.set_font('Arial', '', font_size)
pdf.cell(max_tb_widths[2], space * th, f"{sum(sub_marks)}/{len(sub_marks) * 100}", border=1, align='C')

pdf.ln(space * th)

percentage = sum(sub_marks) / len(sub_marks)
pdf.set_font('Arial', 'B', font_size)
pdf.cell(max_tb_widths[0] + max_tb_widths[1], space * th, "PERCENTAGE", border=1, align='C')
pdf.set_font('Arial', '', font_size)
pdf.cell(max_tb_widths[2], space * th, "{:.2f}".format(percentage), border=1, align='C')

pdf.ln(space * th)
pdf.set_font('Arial', 'B', font_size)
result = "FAIL"
if percentage > 35.00:
    result = "PASS"

pdf.cell(sum(max_tb_widths), space * th, f"RESULT:{result}", border=1, align='C')

pdf.ln(space * th)

space = 1.7

pdf.set_font('Arial', 'B', font_size)
# pdf.x = max_tb_widths[0]-max_tb_widths[0]+0.5
pdf.cell(max_tb_widths[0], space * th, "DISCLAIMER:")
pdf.set_font('Arial', '', font_size)
# pdf.x = max_tb_widths[0]-0.5
# pdf.cell(sum(max_tb_widths[1:]), space * th, "Neither MKCL nor Maharashtra State Board of Secondary and Higher")
pdf.ln(0.0)

txt = """                           Neither MKCL nor Maharashtra State Board of Secondary and Higher
Secondary Education, Pune are responsible for any inadvertent error that may have crept in the
results being published online. The results published on net are for immediate information only.
These cannot be treated as original statement of marks. Please verify the information from the
original statement of marks issued by the board separately and available at the time of
declaration with the respective Jr college."""

pdf.set_font('Arial', '', font_size)
pdf.multi_cell(sum(max_tb_widths), space * th,
               txt,
               border=1)

pdf.ln(0.0)

pdf.set_font('Arial', 'B', font_size)
# pdf.x = max_tb_widths[0]-max_tb_widths[0]+0.5
pdf.cell(max_tb_widths[0], space * th, "Note for CIS Candidates:")
pdf.set_font('Arial', '', font_size)
# pdf.x = max_tb_widths[0]+0.4
# pdf.cell(sum(max_tb_widths[1:]), space * th, "It is obligatory for candidates admitted for class improvement to")
pdf.ln(0.0)

txt = """                                              It is obligatory for candidates admitted for class improvement to
give their option within one month from the date on which the marklists have been distributed.
After that the board marklist with option will be given within the period of six months after
paying extra charges. If no application with option is received within 6 months the class
improvement performance will be considered as "cancelled" and previous performance will be
taken into account by divisional board."""

pdf.set_font('Arial', '', font_size)
pdf.multi_cell(sum(max_tb_widths), space * th,
               txt,
               border=1)

pdf.ln(space * 3 * th)

pdf.set_font('Arial', '', 8)
pdf.cell(sum(max_tb_widths), 0.0, f"https://hscresult.mkcl.org/result/P/{seat_no}_{mother[:min(len(mother), 3)]}.html",
         align="L")
pdf.ln(0.0)
pdf.cell(sum(max_tb_widths), 0.0, "1/1", align="R")

pdf_name = "_".join(name.split(" "))
pdf.output(f'./sample_report/{pdf_name}.pdf', 'F')
