import openpyxl
from openpyxl import worksheet

data_path = "resources/data3.xlsx"

workbook1 = openpyxl.load_workbook(data_path)

sheet1 = workbook1.active
sheet2 = workbook1
