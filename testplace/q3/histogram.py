import sys
import re
import pandas as pd
import matplotlib.pyplot as plt

# ensg2hugo.py -f2 expression_analysis.tsv >expression_analysis.hugo.tsv
if (re.findall(r'[-]\w', '-f2')[0]=='-f'):
    filename = sys.argv[2]
    column_index = int(re.findall(r'\d', sys.argv[1])[0])
else:
    filename = sys.argv[1]
    column_index = 2
    
# Get data
rawdata_input = pd.read_csv(filename,sep='\t')

print("plot {0} column, that is {1}.".format(column_index,rawdata_input.columns[column_index-1]))

# prepare plot
fig, ax = plt.subplots()
rawdata_input.hist(column=rawdata_input.columns[column_index-1], bins=50, ax=ax)
fig.savefig('histfigure.png')
