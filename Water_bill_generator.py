import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Border, Side, Alignment
from openpyxl.utils import get_column_letter

beginning_readings = {
    "G1": 99863,
    "G2": 103518,
    "101": 92688,
    "102": 12031,
    "201": 243871,
    "202": 54573,
    "301": 116874,
    "302": 33537,
    "Watchman": 44089
}

ending_readings = {
    "G1": 100996,
    "G2": 104364,
    "101": 99334,
    "102": 12711,
    "201": 243871,
    "202": 55579,
    "301": 117243,
    "302": 34130,
    "Watchman": 44089
}
balance = {
    "G1": 0,
    "G2": 0,
    "101": 0,
    "102": 0,
    "201": 0,
    "202": 0,
    "301": 93,
    "302": 143,
    "Watchman": 0
}

# Converting dictionary values to lists
balancel = list(balance.values())
beg_redl = list(beginning_readings.values())
end_redl = list(ending_readings.values())
flat_no  =  list(beginning_readings.keys())
unit_no = [0.19]*9

# Calculating total units consumed
total_units = []
for i,j in zip(beg_redl,end_redl):
    total_units.append(j - i)

amount = []
for k in total_units:
    amount.append(round(k*0.19))


total_amt = []
for o,n in zip(amount,balancel):
    total_amt.append(o + n)    

total_unitsk = 0
for l in total_units:
    total_unitsk += l  

total_amth = 0
for d in amount:
    total_amth += d 

total_amtr = 0
for f in total_amt:
    total_amtr += f

# Creating a DataFrame and exporting to Excel
data = {
    
"flat no" :  flat_no,

"beggnig reading" : beg_redl,

"ending reading" : end_redl,

"Amount per unit" : unit_no,

"total units" : total_units,

"sep bills" : amount,

"balance" : balancel,

"toatl amount" : total_amt

}

file = pd.DataFrame(data)

file_name = "Water bill.xlsx"
file.to_excel(file_name, index=False)

# Formatting the Excel file
wb = load_workbook(file_name)
ws = wb.active

# Define the table range
table_ref = f"B2:H{len(file)+1}"
table = Table(displayName="WaterConsumption", ref=table_ref)

# Add a default style with striped rows and banded columns
thick_border = Border(
    left=Side(style='thick'),
    right=Side(style='thick'),
    top=Side(style='thick'),
    bottom=Side(style='thick')
)

# Apply thick border to all cells that have data
for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column):
    for cell in row:
        cell.border = thick_border

ws.add_table(table)

#spacing and alignment
for column_cells in ws.columns:
    max_length = 0
    column = column_cells[0].column_letter
    for cell in column_cells:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    ws.column_dimensions[column].width = max_length + 2

#saving the file
wb.save(file_name)
print("✅ Excel table created successfully as 'water bill.xlsx'")
