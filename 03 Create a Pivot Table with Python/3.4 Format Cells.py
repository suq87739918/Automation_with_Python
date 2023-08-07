from openpyxl import load_workbook
from openpyxl.styles import Font

wb = load_workbook("/Users/sunyueqian/Desktop/Automation with Python/pivot_table.xlsx")
sheet = wb["Report"]

#add title and subtitle
sheet['A1'] = "Salse Report"
sheet['A2'] = "Jan"

#edit font
sheet['A1'].font = Font("Arial", bold=True,size=20)
sheet['A2'].font = Font("Arial", bold=True,size=10)

wb.save("report_Jan.xlsx")
