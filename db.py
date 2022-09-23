'''import os
import re

cvecsvpath = input("CVE allitems.csv location. (Download from https://www.cve.org/Downloads): ")
if not os.path.isfile(cvecsvpath):
    print("File path isn't correct!")
    exit(0)

with open(cvecsvpath, "r", encoding="Latin-1") as rfh:
    cvecsv = rfh.read()

cvecsv = cvecsv.split("\n")

for line in cvecsv:
    line = line.split(",", 2)
    cvenum = line[0]
    wholedesc = line[2]
    desc = desc[1:]
    desc = desc[:-1]
    print(cvenum + ";" + desc)'''

import csv
import os

def appendToVulns(line):
    line = line.encode("ascii", "ignore")
    line = line.decode()
    with open("cve.csv", "a") as afh:
        afh.write(line)

cvecsvpath = input("CVE allitems.csv location. (Download from https://www.cve.org/Downloads): ")
if not os.path.isfile(cvecsvpath):
    print("File path isn't correct!")
    exit(0)

with open(cvecsvpath, "r", encoding="Latin-1") as rfh:
    csvread = csv.reader(rfh)
    print(csvread)
    for line in csvread:
        cvenum = line[0]
        desc = line[2]
        line = cvenum + ";" + desc + "\n"
        appendToVulns(line)