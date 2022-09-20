import sys
import re
import pandas as pd

# ensg2hugo.py -f2 expression_analysis.tsv >expression_analysis.hugo.tsv
if (re.findall(r'[-]\w', sys.argv[1])[0]=='-f'):
    filename = sys.argv[2]
    column_index = int(re.findall(r'\d', sys.argv[1])[0])
else:
    filename = sys.argv[1]
    column_index = 1

print(filename,column_index)

# open file
f=open("{0}".format('Homo_sapiens.GRCh37.75.gtf'),'r')
rawdata=f.readlines()
f.close()
print('GTF file read.')

# collect data
packed_data=[]

# oh dear.
for i in range(0,len(rawdata)):
#for i in range(0,20):
    dataline=rawdata[i].split()
    if (len(dataline)>=2):
        get_everything=1
        for j in range(0,len(dataline)):
            if (dataline[j]=='gene_id'):
                gene_id = re.sub(r'[^\w]', "", dataline[j+1])
                get_everything*=2
            if (dataline[j]=='gene_name'):
                gene_name = re.sub(r'[^\w]', "", dataline[j+1])
                get_everything*=2
        if (get_everything==4):
            packed_data.append((gene_id,gene_name))
            
# get the list into a dict.
dictionary = dict(packed_data)

# try to release some memory
del packed_data
del dataline

print('Dict created, clearing cache.')

# read csv file
rawdata_input = pd.read_csv(filename)

# turn everything in!
for i in range(rawdata_input.size):
    rawdata_input.iat[i,column_index-1]=dictionary[re.findall(r'\w+', rawdata_input.iat[i,column_index-1])[0]]

# output csv file
rawdata_input.to_csv('expres.anal.hugo.tsv')

print('Done.')
