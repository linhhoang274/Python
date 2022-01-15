amount = sheet(["Amount"].
bank_account = sheet.columns["Acc no"]
bank_code = sheet.columns["Bank Code"]
branch_code = sheet.columns["Branch Code"]
courier_ID = sheet.columns["Courier ID"]
payment = "#IL#DFT#"+str(date_payment)+"#####ILS#"+str(amount)+"##501334006#Wolt Enterprises Israel LTD##CITIILIT#Citibank N.A#Menachem Begin 121st 121#TEL AVIV - YAFO 6701203#Israel##2827#OUR#"+str(date_payment)+"#ILS###################"+str(bank_account)+"#"+str(courier_ID)+"######"+str(bank_code)+str(branch_code)+"####"+bank_name+"################"+bank_note+"#006##########"
amount = pd.DataFrame(workbook, columns = ["Amount"], index=[1])
date_payment = 20211221
bank_note = "CP PAYOUT 21.12.21"


import pandas as pd
workbook = pd.read_excel(r"Payment list - test.xlsx")
#place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
table = pd.DataFrame(workbook)

import csv

file = open("Payment list - test.csv","r")
reader = file.readlines()
for row in reader:
    print(row)
    for column in row[1]:
    print(column)
