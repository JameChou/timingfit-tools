#!/usr/local/bin/python

import os
import csv

def readData(list):
    hasEmailCount = 0
    fetchDataCount = 0
    duplicateCount = 0
    emails = []
    csv_file = open('bodysolid_all_area.csv', 'a')
    writer = csv.writer(csv_file)
    #writer.writerow(['name', 'address', 'email'])
    csv_read_file = csv.reader(open('/Users/chowjames/Desktop/body-solid-datas.csv', 'r'))
    for i in csv_read_file:
        name = i[1]
        address = i[0]
        email = i[2]
        fetchDataCount = fetchDataCount + 1
        if email == '':
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
    readData(list)

