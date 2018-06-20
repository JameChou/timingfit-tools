#!/usr/local/bin/python

import os
import csv

def file_name(file_dir):
    list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            list.append(file)
    return list

def readData(list):
    for file in list:
        csv_file = csv.reader(open('/Volumes/Code/code_archive/yellowpages/results/yellowpages/' + file, 'r'))
        for i in csv_file:
            name = i[0]
            address = i[1]
            email = i[4]
            if email == 'kcshultz@gmail.com':
                print address
                return

if __name__ == "__main__":
    list = file_name('/Volumes/Code/code_archive/yellowpages/results/yellowpages')
    readData(list)