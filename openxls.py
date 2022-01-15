from openpyxl import load_workbook
wb = load_workbook("Payment list - test.xlsx")
sheet = wb.active
first_courier = sheet["A2":"K2"]
#for loop
for cell in first_courier:
    for x in cell:
        print(x["A2"].value)

