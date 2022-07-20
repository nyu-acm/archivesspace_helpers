"""tc_number_and_barcode.py Creates text file of top containers and barcodes"""

#This script takes a csv export of top containers from ArchivesSpace's
#Manage Top Containers search and returns a text file of the
#container's type, indicator, and barcode. This version is compatible with
#the v.3.2.0 container csv export.

import csv

#Replace this file with your export
my_file = 'top_040.csv'

fh = open(my_file)
next(fh)

#Write to a text file. Comment this section out if you just want to print the results
result_file = "my_boxes_and_barcodes.txt"
wfh = open(result_file, 'w', newline='')

#Loop through csv file. Comment out line 25 (print) if you just want the file;
#Comment out line 26 (wfh.write) if you just want to print the results
for line in fh:
    items = line.split(',')
    container_type = items[4]
    container_num = items[5]
    barcode = items[6]
    box_info_string = f'{container_type} {container_num}: {barcode}'
    print(box_info_string)
    #wfh.write(box_info_string + '\n')

#wfh.close()
fh.close()