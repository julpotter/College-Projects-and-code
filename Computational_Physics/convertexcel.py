# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:08:46 2018

@author: Julian
"""

import xlrd
import csv

def xls_to_csv():

    x =  xlrd.open_workbook('Hubble.xlsx')
    x1 = x.sheet_by_name('Sheet1')
    csvfile = open('data.csv', 'wb')
    writecsv = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    for rownum in xrange(x1.nrows): #To determine the total rows. 
        writecsv.writerow(x1.row_values(rownum))

    csvfile.close()