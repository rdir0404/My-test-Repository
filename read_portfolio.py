# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:55:23 2020

@author: rdiru
"""

import csv
from scipy.stats import norm
from BlackScholes import bs_price, bs_delta, bs_gamma, bs_vega, bs_rho, bs_impliedvol
from datetime import date

## filename = 'C:/Users/rdiru/OneDrive/Documents/Programming/Python/BTC-USD.csv'


filename = 'BTC Options Portfolio.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    line_count = 0
    ThisDay = date.today()
    ExpDate = date( 2021, 9, 27)
    print (ExpDate - ThisDay)
    for line in reader:
        if line_count <= 10000:  
            print(line[0],':',line[1],':',line[2],':',line[3],':',line[4],':',line[5],':',line[6],':',line[7])
##                print(TokenName,InstType,Strike,CallPut,Quantity,ExpDate)
        line_count += 1