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
    hasEmailCount = 0
    fetchDataCount = 0
    duplicateCount = 0
    emails = []
    csv_file = open('all_area.csv', 'a')
    writer = csv.writer(csv_file)
    #writer.writerow(['name', 'address', 'email'])
    for file in list:
        csv_file = csv.reader(open('/Volumes/Code/code_archive/yellowpages/results/' + file, 'r'))
        for i in csv_file:
            name = i[0]
            address = i[1]
            email = i[4]
            fetchDataCount = fetchDataCount + 1
            if email == 'none':
                continue
            hasEmailCount = hasEmailCount + 1
            if emails.__contains__(email):
                duplicateCount = duplicateCount + 1
                continue
            emails.append(email)
            #writer.writerow([name, address, email])
            writer.writerow([name, name, email])

    print ("valid emails num: %d, all data count in the usa: %d, email duplicate count: %d", (len(emails), fetchDataCount, duplicateCount))


if __name__ == "__main__":
    list = file_name('/Volumes/Code/code_archive/yellowpages/results')
    readData(list)

