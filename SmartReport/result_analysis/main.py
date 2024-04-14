import re
import pandas as pd
import PyPDF2
from io import StringIO


def get_ese_marks(singlePage, sem: int, sub: int):
    # abb for Abbreviations
    abb_ese = re.compile(f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\d+\s*\|(\d+)")
    match = abb_ese.search(singlePage)

    if match:
        abb_ese_marks = match.group(1)
    else:
        abb_ese_marks = ""
    return abb_ese_marks


def get_ise_marks(singlePage, sem: int, sub: int):
    abb_ise = re.compile(f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)")
    match = abb_ise.search(singlePage)

    if match:
        abb_ise_marks = match.group(1)
    else:
        abb_ise_marks = ""
    return abb_ise_marks


def get_ica_marks(singlePage, sem: int, sub: int):
    abb_ica = re.compile(
        f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)"
    )
    match = abb_ica.search(singlePage)

    if match:
        abb_ica_marks = match.group(1)
    else:
        abb_ica_marks = ""
    return abb_ica_marks


def get_poe_marks(singlePage, sem: int, sub: int):
    abb_poe = re.compile(
        f"BTN06{sem}0{sub}\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)"
    )
    match = abb_poe.search(singlePage)
    if match:
        abb_poe_marks = match.group(1)
    else:
        abb_poe_marks = ""
    return abb_poe_marks


def get_total_marks(singlePage, sem: int, sub: int):
    subject_total = re.compile(
        f"BTN06{sem}0{sub}\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|(\d+)\s*\|--\s*\|(\d+)"
    )
    subMatch = subject_total.search(singlePage)
    if subMatch:
        sub_total_marks = subMatch.group(2)
    else:
        sub_total_marks = ""
    return sub_total_marks


def get_sts(singlePage, sem: int, sub: int):
    subject_sts = re.compile(
        f"BTN06{sem}0{sub}\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|\d+\s*\|--\s*\|\d+\s*\|\S\s*\|\s*\d+\.\d+\|\s*\d+\.\d+\|\s*(\w)"
    )
    subMatch = subject_sts.search(singlePage)
    if subMatch:
        sub_sts_value = subMatch.group(1)
    else:
        sub_sts_value = ""
    return sub_sts_value


def sem3Data(singlePage):
    sub1_ese_marks = get_ese_marks(singlePage, 3, 1)
    sub2_ese_marks = get_ese_marks(singlePage, 3, 2)
    sub3_ese_marks = get_ese_marks(singlePage, 3, 3)
    sub4_ese_marks = get_ese_marks(singlePage, 3, 4)
    sub5_ese_marks = get_ese_marks(singlePage, 3, 5)
    sub6_ese_marks = get_ese_marks(singlePage, 3, 6)

    sub1_ise_marks = get_ise_marks(singlePage, 3, 1)
    sub2_ise_marks = get_ise_marks(singlePage, 3, 2)
    sub3_ise_marks = get_ise_marks(singlePage, 3, 3)
    sub4_ise_marks = get_ise_marks(singlePage, 3, 4)
    sub5_ise_marks = get_ise_marks(singlePage, 3, 5)
    sub6_ise_marks = get_ise_marks(singlePage, 3, 6)

    sub1_ica_marks = get_ica_marks(singlePage, 3, 1)
    sub2_ica_marks = get_ica_marks(singlePage, 3, 2)
    sub3_ica_marks = get_ica_marks(singlePage, 3, 3)
    sub4_ica_marks = get_ica_marks(singlePage, 3, 4)
    sub5_ica_marks = get_ica_marks(singlePage, 3, 5)
    sub6_ica_marks = get_ica_marks(singlePage, 3, 6)

    sub1_poe_marks = get_poe_marks(singlePage, 3, 1)
    sub2_poe_marks = get_poe_marks(singlePage, 3, 2)
    sub3_poe_marks = get_poe_marks(singlePage, 3, 3)
    sub4_poe_marks = get_poe_marks(singlePage, 3, 4)
    sub5_poe_marks = get_poe_marks(singlePage, 3, 5)
    sub6_poe_marks = get_poe_marks(singlePage, 3, 6)

    sub1_total_marks = get_total_marks(singlePage, 3, 1)
    sub2_total_marks = get_total_marks(singlePage, 3, 2)
    sub3_total_marks = get_total_marks(singlePage, 3, 3)
    sub4_total_marks = get_total_marks(singlePage, 3, 4)
    sub5_total_marks = get_total_marks(singlePage, 3, 5)
    sub6_total_marks = get_total_marks(singlePage, 3, 6)

    sub1_sts_value = get_sts(singlePage, 3, 1)
    sub2_sts_value = get_sts(singlePage, 3, 2)
    sub3_sts_value = get_sts(singlePage, 3, 3)
    sub4_sts_value = get_sts(singlePage, 3, 4)
    sub5_sts_value = get_sts(singlePage, 3, 5)
    sub6_sts_value = get_sts(singlePage, 3, 6)

    total_pattern = re.compile(
        r"Sem-III\s*Total Credit: (\d+\.\d+).*?EGP: (\d+\.\d+).*?SGPA: (\d+\.\d+)"
    )
    total_match = total_pattern.search(singlePage)

    if total_match:
        total_credit = float(total_match.group(1))
        egp = float(total_match.group(2))
        sgpa = total_match.group(3)
    else:
        total_credit = ""
        egp = ""
        sgpa = ""

    return {
        "BTN06301": {
            "ESE": sub1_ese_marks,
            "ISE": sub1_ise_marks,
            "ICA": sub1_ica_marks,
            "POE": sub1_poe_marks,
            "Total": sub1_total_marks,
            "Sts": sub1_sts_value,
        },
        "BTN06302": {
            "ESE": sub2_ese_marks,
            "ISE": sub2_ise_marks,
            "ICA": sub2_ica_marks,
            "POE": sub2_poe_marks,
            "Total": sub2_total_marks,
            "Sts": sub2_sts_value,
        },
        "BTN06303": {
            "ESE": sub3_ese_marks,
            "ISE": sub3_ise_marks,
            "ICA": sub3_ica_marks,
            "POE": sub3_poe_marks,
            "Total": sub3_total_marks,
            "Sts": sub3_sts_value,
        },
        "BTN06304": {
            "ESE": sub4_ese_marks,
            "ISE": sub4_ise_marks,
            "ICA": sub4_ica_marks,
            "POE": sub4_poe_marks,
            "Total": sub4_total_marks,
            "Sts": sub4_sts_value,
        },
        "BTN06305": {
            "ESE": sub5_ese_marks,
            "ISE": sub5_ise_marks,
            "ICA": sub5_ica_marks,
            "POE": sub5_poe_marks,
            "Total": sub5_total_marks,
            "Sts": sub5_sts_value,
        },
        "BTN06306": {
            "ESE": sub6_ese_marks,
            "ISE": sub6_ise_marks,
            "ICA": sub6_ica_marks,
            "POE": sub6_poe_marks,
            "Total": sub6_total_marks,
            "Sts": sub6_sts_value,
        },
        "Total_Credit": total_credit,
        "EGP": egp,
        "SGPA": sgpa,
    }


def sem4Data(singlePage):
    sub1_ese_marks = get_ese_marks(singlePage, 4, 1)
    sub2_ese_marks = get_ese_marks(singlePage, 4, 2)
    sub3_ese_marks = get_ese_marks(singlePage, 4, 3)
    sub4_ese_marks = get_ese_marks(singlePage, 4, 4)
    sub5_ese_marks = get_ese_marks(singlePage, 4, 5)
    sub6_ese_marks = get_ese_marks(singlePage, 4, 6)

    sub1_ise_marks = get_ise_marks(singlePage, 4, 1)
    sub2_ise_marks = get_ise_marks(singlePage, 4, 2)
    sub3_ise_marks = get_ise_marks(singlePage, 4, 3)
    sub4_ise_marks = get_ise_marks(singlePage, 4, 4)
    sub5_ise_marks = get_ise_marks(singlePage, 4, 5)
    sub6_ise_marks = get_ise_marks(singlePage, 4, 6)

    sub1_ica_marks = get_ica_marks(singlePage, 4, 1)
    sub2_ica_marks = get_ica_marks(singlePage, 4, 2)
    sub3_ica_marks = get_ica_marks(singlePage, 4, 3)
    sub4_ica_marks = get_ica_marks(singlePage, 4, 4)
    sub5_ica_marks = get_ica_marks(singlePage, 4, 5)
    sub6_ica_marks = get_ica_marks(singlePage, 4, 6)

    sub1_poe_marks = get_poe_marks(singlePage, 4, 1)
    sub2_poe_marks = get_poe_marks(singlePage, 4, 2)
    sub3_poe_marks = get_poe_marks(singlePage, 4, 3)
    sub4_poe_marks = get_poe_marks(singlePage, 4, 4)
    sub5_poe_marks = get_poe_marks(singlePage, 4, 5)
    sub6_poe_marks = get_poe_marks(singlePage, 4, 6)

    sub1_total_marks = get_total_marks(singlePage, 4, 1)
    sub2_total_marks = get_total_marks(singlePage, 4, 2)
    sub3_total_marks = get_total_marks(singlePage, 4, 3)
    sub4_total_marks = get_total_marks(singlePage, 4, 4)
    sub5_total_marks = get_total_marks(singlePage, 4, 5)
    sub6_total_marks = get_total_marks(singlePage, 4, 6)

    sub1_sts_value = get_sts(singlePage, 4, 1)
    sub2_sts_value = get_sts(singlePage, 4, 2)
    sub3_sts_value = get_sts(singlePage, 4, 3)
    sub4_sts_value = get_sts(singlePage, 4, 4)
    sub5_sts_value = get_sts(singlePage, 4, 5)
    sub6_sts_value = get_sts(singlePage, 4, 6)

    # calculation for BTNENV ese ise total
    subenv_ese = re.compile(f"BTNENV\s*\|\S\S\s*\|\d+\s*\|(\d+)")
    subenv_ese_match = subenv_ese.search(singlePage)

    if subenv_ese_match:
        subenv_ese_marks = subenv_ese_match.group(1)
    else:
        subenv_ese_marks = ""

    subenv_ise = re.compile(f"BTNENV\s*\|\S\S\s*\|\S+\s*\|\S+\s*\|\d+\s*\|(\d+)")
    subenv_ise_match = subenv_ise.search(singlePage)

    if subenv_ise_match:
        subenv_ise_marks = subenv_ise_match.group(1)
    else:
        subenv_ise_marks = ""

    subenv_total = re.compile(
        f"BTNENV\s*\|\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|--\s*\|(\d+)\s*\|--\s*\|(\d+)"
    )
    subenv_total_match = subenv_total.search(singlePage)

    if subenv_total_match:
        subenv_total_marks = subenv_total_match.group(2)
    else:
        subenv_total_marks = ""

    total_pattern = re.compile(
        r"Sem-IV\s*Total Credit: (\d+\.\d+).*?EGP: (\d+\.\d+).*?SGPA: (\d+\.\d+)"
    )
    total_match = total_pattern.search(singlePage)
    if total_match:
        total_credit = total_match.group(1)
        egp = total_match.group(2)
        sgpa = total_match.group(3)
    else:
        total_credit = ""
        egp = ""
        sgpa = ""

    return {
        "BTN06401": {
            "ESE": sub1_ese_marks,
            "ISE": sub1_ise_marks,
            "ICA": sub1_ica_marks,
            "POE": sub1_poe_marks,
            "Total": sub1_total_marks,
            "Sts": sub1_sts_value,
        },
        "BTN06402": {
            "ESE": sub2_ese_marks,
            "ISE": sub2_ise_marks,
            "ICA": sub2_ica_marks,
            "POE": sub2_poe_marks,
            "Total": sub2_total_marks,
            "Sts": sub2_sts_value,
        },
        "BTN06403": {
            "ESE": sub3_ese_marks,
            "ISE": sub3_ise_marks,
            "ICA": sub3_ica_marks,
            "POE": sub3_poe_marks,
            "Total": sub3_total_marks,
            "Sts": sub3_sts_value,
        },
        "BTN06404": {
            "ESE": sub4_ese_marks,
            "ISE": sub4_ise_marks,
            "ICA": sub4_ica_marks,
            "POE": sub4_poe_marks,
            "Total": sub4_total_marks,
            "Sts": sub4_sts_value,
        },
        "BTN06405": {
            "ESE": sub5_ese_marks,
            "ISE": sub5_ise_marks,
            "ICA": sub5_ica_marks,
            "POE": sub5_poe_marks,
            "Total": sub5_total_marks,
            "Sts": sub5_sts_value,
        },
        "BTN06406": {
            "ESE": sub6_ese_marks,
            "ISE": sub6_ise_marks,
            "ICA": sub6_ica_marks,
            "POE": sub6_poe_marks,
            "Total": sub6_total_marks,
            "Sts": sub6_sts_value,
        },
        "BTNENV": {
            "ESE": subenv_ese_marks,
            "ISE": subenv_ise_marks,
            "Total": subenv_total_marks,
        },
        "Total_Credit": total_credit,
        "EGP": egp,
        "SGPA": sgpa,
    }


def singlePageData(singlePage):
    # college_code_pattern = re.compile(r"College Code:\s*([^\s]+)")
    # college_code = college_code_pattern.search(singlePage).group(1)

    seat_no_pattern = re.compile(r"Seat No:\s*([^\s]+)")
    seat_match = seat_no_pattern.search(singlePage)
    if seat_match:
        seat_no = seat_match.group(1)
    else:
        seat_no = ""

    prn_no_pattern = re.compile(r"PRN:\s*(\d+)")
    prn_no_match = prn_no_pattern.search(singlePage)
    if prn_no_match:
        prn_no = prn_no_match.group(1)
    else:
        prn_no = ""

    name_pattern = re.compile(r"Name:\s*([^(\n]+)")
    name_match = name_pattern.search(singlePage)
    if name_match:
        name = name_match.group(1).strip()
    else:
        name = ""

    sem3_data = sem3Data(singlePage)
    sem4_data = sem4Data(singlePage)

    overall_status_pattern = re.compile(r"\|Status:\s*(\w+)\s*\|C")
    overall_status_match = overall_status_pattern.search(singlePage)
    if overall_status_match:
        overall_status = overall_status_match.group(1)
    else:
        overall_status = ""

    percentage_match = re.compile(r"\|Percentage:\s*(\d+\.\d+)\s*\%").search(singlePage)
    if percentage_match:
        percentage = percentage_match.group(1)
    else:
        percentage = ""

    return {
        "Exam_Seat_No": seat_no,
        "PRN_No": prn_no,
        "Name": name,
        "Sem3": sem3_data,
        "Sem4": sem4_data,
        "Status": overall_status,
        "Percentage": percentage,
    }


def extract_data_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        data_list = []
        # for page_num in range(2, 3):
        for page_num in range(2, len(reader.pages)):
            single_page = reader.pages[page_num].extract_text()
            data = singlePageData(single_page)
            data_list.append(data)
        return data_list


pdf_path = "input.pdf"
data_list = extract_data_from_pdf(pdf_path)

html_head = """
<thead>
    <tr>
        <td rowspan="3">Exam Seat No.</td>
        <td rowspan="3">PRN No.</td>
        <td rowspan="3">Name of Student</td>
        <td colspan="39">Sem 3</td>
        <td colspan="42">Sem 4</td>
        <td rowspan="3">Status</td>
        <td rowspan="3">Percentage</td>
    </tr>
    <tr>
        <td colspan="6">BTN06301</td>
        <td colspan="6">BTN06302</td>
        <td colspan="6">BTN06303</td>
        <td colspan="6">BTN06304</td>
        <td colspan="6">BTN06305</td>
        <td colspan="6">BTN06306</td>
        <td rowspan="2">Total Credit</td>
        <td rowspan="2">EGP</td>
        <td rowspan="2">SGPA</td>
        <td colspan="6">BTN06401</td>
        <td colspan="6">BTN06402</td>
        <td colspan="6">BTN06403</td>
        <td colspan="6">BTN06404</td>
        <td colspan="6">BTN06405</td>
        <td colspan="6">BTN06406</td>
        <td colspan="3">BTNENV</td>
        <td rowspan="2">Total Credit</td>
        <td rowspan="2">EGP</td>
        <td rowspan="2">SGPA</td>
    </tr>
    <tr>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>ICA</td>
        <td>POE</td>
        <td>Total</td>
        <td>Sts</td>
        <td>ESE</td>
        <td>ISE</td>
        <td>Total</td>
    </tr>
</thead>
"""

all_data = ""
for student in data_list:
    one_row = ""
    one_row += f"<td>{student['Exam_Seat_No']}</td>"
    one_row += f"<td>{student['PRN_No']}</td>"
    one_row += f"<td>{student['Name']}</td>"

    for i in ["Sem3", "Sem4"]:
        for data in student[i]:
            # Check if the value is a dictionary before iterating over it
            if isinstance(student[i][data], dict):
                for abb in student[i][data]:
                    one_row += f"<td>{student[i][data][abb]}</td>"
            else:
                one_row += f"<td>{student[i][data]}</td>"

    one_row += f"<td>{student['Status']}</td>"
    one_row += f"<td>{student['Percentage']}</td>"
    all_data += f"<tr>{one_row}</tr>"


table = f"<table>{html_head}<tbody>{all_data}</tbody></table>"
result = pd.read_html(StringIO(table))
result[0].to_excel("output.xlsx")
