file = open("Payment list - test.csv",mode="r",encoding = "utf-8-sig")
file_new = open("Payment new.txt", mode="w")

header = file.readline()

row = file.readline()
while row != "":
    row_list = row.split(";")
    courier_ID=row_list[0]
    amount=float(row_list[1].replace(",","."))
    amount=round(amount,2)
    bank_code=row_list[3]
    branch_code=row_list[4]
    bank_account=row_list[5]
    bank_name=row_list[8].replace("\u200b","")
    date_payment = 20211221
    bank_note = "CP PAYOUT 21.12.21"
    row_new = "#IL#DFT#"+str(date_payment)+"#####ILS#"+str(amount)+"##501334006#Wolt Enterprises Israel LTD##CITIILIT#Citibank N.A#Menachem Begin 121st 121#TEL AVIV - YAFO 6701203#Israel##2827#OUR#"+str(date_payment)+"#ILS###################"+str(bank_account)+"#"+str(courier_ID)+"######"+str(bank_code)+str(branch_code)+"####"+bank_name+"################"+bank_note+"#006##########\n"
    file_new.write(row_new)
    row = file.readline()










