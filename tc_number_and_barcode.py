"""tc_number_and_barcode.py Creates text file of top containers and barcodes. This script is comptabile up to version 3.0.2"""

#This script takes a csv export of top containers from ArchivesSpace's
#Manage Top Containers search and returns a text file of the
#container's type, indicator, and barcode.

import csv

#Replace this file with your export
my_file = 'top-containers.csv'

fh = open(my_file)
next(fh)

#Write to a text file. Comment this section out if you just want to print the results
result_file = "my_boxes_and_barcodes.txt"
wfh = open(result_file, 'w', newline='')

#Loop through csv file. Comment out line 25 (print) if you just want the file;
#Comment out line 26 (wfh.write) if you just want to print the results
for line in fh:
    items = line.split(',')
    number_and_barcode = items[0]
    clean_number_and_barcode = number_and_barcode[1:]
    print(clean_number_and_barcode)
    wfh.write(clean_number_and_barcode + '\n')

wfh.close()
fh.close()
