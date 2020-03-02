# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 00:27:26 2020
@author: susan
Module to read CSV file into nested dictionary and
write nested dictionar to CSV file
rd_csv requires 1 argument file, as file name for reading
wrt_csv requires 2 arguments file name and dictionary name to write CSV file. 

"""
import csv
def wrt_csv(file, dictionary):
    with open(file, 'w',newline='') as f:
        dic = dictionary[0]
        header = list(dic.keys())
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for dic in dictionary:
            writer.writerow(dictionary[dic])

def rd_csv(file):
    dictionary = {}
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:        
            dictionary[line_count] = row
            line_count += 1
    return dictionary

#rabbits = rd_csv('rabbits.csv')  # example use read            
# wrt_csv('rabbits1.csv', rabbits) # example use write
#k = len(list(rabbits.keys()))
#lrk = []
#for num in range(k):
#    print(num)
#    rk = list(rabbits[num].values())
#    lrk.append(rk)
#print(lrk)