import os
import subprocess
import time
import sys
from shutil import copyfile


import xml.etree.ElementTree as ET
import csv
  
### open a file for writing, set fields at top   ###

output_file = open('Annotations-export.csv', 'w')

# create the csv writer object
# .tag, .attrib, .text

csvwriter = csv.writer(output_file)
csv_titles = []
csv_titles.append('image')
csv_titles.append('xmin')
csv_titles.append('ymin')
csv_titles.append('xmax')
csv_titles.append('ymax')
csv_titles.append('label')
csvwriter.writerow(csv_titles)

dir = 'subset_annotations/'

### Define inputfile to read and convert   ###
for file in os.listdir(dir):
    input_file = dir + file
    if input_file.endswith(".xml"):


        tree = ET.parse(input_file)
        root = tree.getroot()
        #print("root is: ", *root)


        count = 0
        filename = root.find('filename').text;

        for object in root.findall('object'):
            box_details = []

            box_details.append(filename)

            print("filename is: ", filename)

            #print("count is: ", count)
            name = object.find('name')
            print("name of object is: ", name.text)
            
            bndbox = object.find('bndbox')
            xmin = bndbox.find('xmin').text
            box_details.append(xmin)
            ymin = bndbox.find('ymin').text
            box_details.append(ymin)
            xmax = bndbox.find('xmax').text
            box_details.append(xmax)
            ymax = bndbox.find('ymax').text
            box_details.append(ymax)
            
            box_details.append(name.text)

            csvwriter.writerow(box_details)
            count = count + 1

output_file.close()


