
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Border, Side, Alignment
from openpyxl.utils import get_column_letter
import database    


# Converting d ictionary values to lists
balancel = list(database.balance.values())
beg_redl = list(database.beginning_readings.values())
end_redl = list(database.ending_readings.values())
flat_no  =  list(database.beginning_readings.keys())
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



wb = load_workbook(file_name)
ws = wb.active

wb.save(file_name)
print("✅ Excel table created successfully as 'water bill.xlsx'")

