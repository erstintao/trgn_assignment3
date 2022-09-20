import sys
import re

# Read input file
f=open("{0}".format(sys.argv[1]),'r')
rawdata=f.readlines()
f.close()

# Define pattern
pattern_us_number = re.compile(r'(\d{3})[-](\d{3}[-]\d{4})') 
pattern_international_number = re.compile(r'[+](\d+)[-](\d+)[-](\S+\d)') 

# Analysis input file for each line
for i in range(0,len(rawdata)):
    dataline=rawdata[i].split()
    # let's avoid empty lines.
    if (len(dataline)>0):
        us_numbers_matched=pattern_us_number.findall(rawdata[0])
        internationals_numbers_matched=pattern_international_number.findall(rawdata[0])
       
        # print them if found
        for number in us_numbers_matched:
            print('({0}){1}'.format(number[0],re.sub(r'\D', "", number[1])))
        for number in internationals_numbers_matched:
            print('+{0} ({1}) {2}'.format(number[0],number[1],re.sub(r'\D', "", number[2])))
            