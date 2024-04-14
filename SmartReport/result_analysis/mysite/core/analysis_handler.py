import random

from tabula import read_pdf
import pandas as pd
import os

try:
    import queue
except ImportError:
    import Queue as queue

import os
import glob
import time

import pandas as pd
from operator import itemgetter
import xlsxwriter

SUPPORTED_CLASS = {"HSC-SCIENCE": ["ENGLISH", "MARATHI", "MATHEMATICS & STATISTICS", "PHYSICS", "CHEMISTRY", "BIOLOGY"]}


class HSCScienceParser:

    @staticmethod
    def get_subjects():
        return SUPPORTED_CLASS["HSC-SCIENCE"]

    @staticmethod
    def get_student_data(result_file):
        df = read_pdf(result_file, pages="all", multiple_tables=True, stream=True)

        info = {}
        #print(df)

        df = df.pop(0)
        df = df["MAHARASHTRA STATE BOARD OF SECONDARY & HIGHER SECONDARY EDUCATION,"]
        # print(df)

        info = {"NAME": df[2].split(":")[1].lstrip(),
                "ROLL NO": df[4].split(":")[1].lstrip(),
                "ENGLISH": int(df[7].split(" ")[2]),
                "MARATHI": int(df[8].split(" ")[2]),
                "MATHEMATICS & STATISTICS": int(df[9].split(" ")[4]),
                "PHYSICS": int(df[10].split(" ")[2]),
                "CHEMISTRY": int(df[11].split(" ")[2]),
                "BIOLOGY": int(df[12].split(" ")[2]),
                "MARKS": int(df[13].split(" ")[1].split("/")[0]),
                "TOTAL": int(df[13].split(" ")[1].split("/")[1]),
                "RESULT": df[15].split(":")[1].lstrip()
                }
        print(info)
        return info


class DiplomaParser:

    @staticmethod
    def get_subjects():
        return SUPPORTED_CLASS["HSC-SCIENCE"]

    @staticmethod
    def get_student_data(result_file):
        df = read_pdf(result_file, pages="all", multiple_tables=True, stream=True)

        info = {}
        #print(df)

        df = df.pop(0)
        df = df["MAHARASHTRA STATE BOARD OF SECONDARY & HIGHER SECONDARY EDUCATION,"]
        # print(df)

        info = {"NAME": df[2].split(":")[1].lstrip(),
                "ROLL NO": df[4].split(":")[1].lstrip(),
                "ENGLISH": int(df[7].split(" ")[2]),
                "MARATHI": int(df[8].split(" ")[2]),
                "MATHEMATICS & STATISTICS": int(df[9].split(" ")[4]),
                "PHYSICS": int(df[10].split(" ")[2]),
                "CHEMISTRY": int(df[11].split(" ")[2]),
                "BIOLOGY": int(df[12].split(" ")[2]),
                "MARKS": int(df[13].split(" ")[1].split("/")[0]),
                "TOTAL": int(df[13].split(" ")[1].split("/")[1]),
                "RESULT": df[15].split(":")[1].lstrip()
                }
        print(info)
        return info


class Analyser:

    def __init__(self, stream, media_path, analysis_file):
        if stream == "HSC-SCIENCE":
            self.parser = HSCScienceParser()

        self.df = self.get_df()
        self.writer = self.get_writer(media_path, analysis_file)
        self.analysis_file = analysis_file
        self.media_path = media_path

    @staticmethod
    def get_writer(path, file_name):
        return pd.ExcelWriter(os.path.join(path, 'analysis', file_name), engine='xlsxwriter')

    def get_df(self):
        head = {"NAME": [], "ROLL NO": []}

        for sub in self.parser.get_subjects():
            head[sub] = []

        head["MARKS"] = []
        head["RESULT"] = []

        return pd.DataFrame(head)

    def get_info(self, result_file):
        return self.parser.get_student_data(result_file)

    def parse_results(self):
        for result_file in glob.glob("{}/results/*.pdf".format(self.media_path)):
            self.add(self.get_info(result_file))

        # NUM = 50
        # dummy_infos = {'NAME': ["dummy student-{} ".format(idx) for idx in range(NUM)],
        #                'ROLL NO': [idx for idx in range(NUM)],
        #                "ENGLISH": [random.randint(5, 75) for idx in range(NUM)],
        #                "MARATHI": [random.randint(5, 75) for idx in range(NUM)],
        #                "PHYSICS": [random.randint(5, 75) for idx in range(NUM)],
        #                "CHEMISTRY": [random.randint(5, 75) for idx in range(NUM)],
        #                "BIOLOGY": [random.randint(5, 75) for idx in range(NUM)],
        #                "MARKS": [random.randint(5, 600) for idx in range(NUM)],
        #                "TOTAL": [600 for idx in range(NUM)],
        #                "MATHEMATICS & STATISTICS": [random.randint(5, 75) for idx in range(NUM)]
        #                }
        # subjects = [dummy_infos["ENGLISH"], dummy_infos["MARATHI"], dummy_infos["PHYSICS"], dummy_infos["CHEMISTRY"],
        #             dummy_infos["BIOLOGY"], dummy_infos["MATHEMATICS & STATISTICS"]]
        #
        # dummy_infos["RESULT"] = [random.choice(["PASS", "FAIL"]) for idx in range(NUM)]
        #
        # # for idx in range(NUM):
        # #     mark = sum(list(map(itemgetter(idx), subjects))) / float(len(subjects))
        # #     dummy_infos["MARKS"][idx] = float('{:.2f}'.format(mark))
        # #     if mark < 35.0:
        # #         dummy_infos["RESULT"][idx] = "FAIL"
        # # print(dummy_infos)
        # dummy_df = pd.DataFrame(dummy_infos)
        #
        # for idx in range(dummy_df.shape[0]):
        #     info = dummy_df.iloc[idx].to_dict()
        #     self.add(info)

        return True

    def write_to_sheet(self, sheet_name, temp_df):

        temp_df.to_excel(self.writer, sheet_name=sheet_name, startrow=1, header=False, index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        # workbook = self.writer.book

        temp_worksheet = self.writer.sheets[sheet_name]

        # Get the dimensions of the dataframe.
        (max_row, max_col) = temp_df.shape

        # Create a list of column headers, to use in add_table().
        column_settings = [{'header': column} for column in temp_df.columns]

        # Add the Excel table structure. Pandas will add the data.
        temp_worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})

        # Make the columns wider for clarity.
        temp_worksheet.set_column(0, max_col - 1, 12)

    def do_analysis(self):

        # Get the xlsxwriter workbook and worksheet objects.
        # workbook = self.writer.book

        #  percentage wise topper
        pec_df = self.df.sort_values(by=["MARKS"], ascending=False)
        self.write_to_sheet("MARKS", pec_df)

        # print(self.df)
        # print(pec_df)

        #  subject wise topper
        for sub in self.parser.get_subjects():
            temp_df = self.df[['NAME', 'ROLL NO', sub]]
            temp_df = temp_df.sort_values(by=[sub], ascending=False)
            self.write_to_sheet(sub, temp_df)

        # pass_df = pec_df[pec_df['RESULT'] == "PASS"]
        # passed_student = pass_df.shape[0]
        # failed_student = pec_df.shape[0] - passed_student
        #temp_df = pd.DataFrame()

        # temp_df = temp_df.append(pd.DataFrame({"0": ["No of student Passed"], "1": [passed_student]}))
        # temp_df = temp_df.append(pd.DataFrame({"0": ["No of student Failed"], "1": [failed_student]}))

        # temp_df = temp_df.concat(pd.DataFrame({"0": ["No of student Passed"], "1": [passed_student]}))
        # temp_df = temp_df.concat(pd.DataFrame({"0": ["No of student Failed"], "1": [failed_student]}))

        # temp_df = pd.concat([temp_df, pd.DataFrame.from_records([{"0": ["No of student Passed"], "1": [passed_student]}])])
        # temp_df = pd.concat(
        #     [temp_df, pd.DataFrame.from_records([{"0": ["No of student Failed"], "1": [failed_student]}])])

        # temp_pec_df = pec_df[['NAME', "PERCENTAGE"]]
        # df = df.append(temp_pec_df)

        #temp_df.to_excel(self.writer, sheet_name="CLASS REPORT", startrow=1, header=False, index=False)

        self.save()

    def add(self, info):
        student_info = {}
        cols = self.df.head()
        for col in cols.columns:
            if col in info:
                student_info[col] = info[col]
            else:
                if col == "NAME" or col == "RESULT":
                    student_info[col] = "NONE"
                else:
                    student_info[col] = -1
        self.df = self.df.append(student_info, ignore_index=True)

    def save(self):
        self.writer.save()


if __name__ == "__main__":
    import os
    import glob
    import time

    import pandas as pd
    from operator import itemgetter
    import xlsxwriter

    MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media")

    analyser = Analyser("HSC-SCIENCE", MEDIA_ROOT, "analysis.xlsx")
    analyser.parse_results()
    analyser.do_analysis()

