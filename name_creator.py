import csv
import os
import re
CURRENT_DIRECTORY = os.getcwd()
names = []

#get names from CSV
def read_csv():
    for file in os.listdir(CURRENT_DIRECTORY):
        if file.endswith('.csv'):
            with open (os.path.join(CURRENT_DIRECTORY, file)) as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[2] != 'First Name' and row[3] != 'Surname'
                    name = row[2] + ' ' + row[3]
                    #format the names
                    name = name.title()
                    if re.findall(r'^.*\s[M][c].*$', name):#this is for names that have mc in them
                        name = name.split()[0] + ' ' + name.split()[1][0:2] + name.split()[1][2].upper() + name.split()[1][3:]
                    names.append(name)


#take the svg and add the formatted names to the file
#convert the svg and join the 2 images togteher
#convert PDF

read_csv()