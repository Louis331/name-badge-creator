import csv
import os
import re
import xml.etree.ElementTree as ET
CURRENT_DIRECTORY = os.getcwd()
names = []

#get names from CSV
def read_csv():
    for file in os.listdir(CURRENT_DIRECTORY):
        if file.endswith('.csv'):
            with open (os.path.join(CURRENT_DIRECTORY, file)) as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[4] != 'First Name' and row[5] != 'Surname':
                        name = row[4] + ' ' + row[5]
                        #format the names
                        name = name.title()
                        if re.findall(r'^.*\s[M][c].*$', name):#this is for names that have mc in them
                            name = name.split()[0] + ' ' + name.split()[1][0:2] + name.split()[1][2].upper() + name.split()[1][3:]
                        names.append(name)

#take the svg and add the formatted names to the file
def svg_editor(name):
    tree = ET.parse('badge.svg')
    root = tree.getroot()
    name = name.split()
    print(name)
    first_text = ET.SubElement(root, 'text')
    first_text.text = name[0]
    first_text.attrib = {'x': '150', 'y': '260.98', 'class': "cls-17", 'text-anchor': "middle"}
    second_text = ET.SubElement(root, 'text')
    second_text.text = name[1]
    second_text.attrib = {'x': '150', 'y': '290.98', 'class': "cls-17", 'text-anchor': "middle"}
    location = name[0] + name[1] + '.svg'
    tree.write(os.path.join('pics', location))

read_csv()
for name in names:
    svg_editor(name)