# trgn_assignment3

All scripts are kept in <code>/scripts</code>.

Test cases are placed in <code>/testplace/q1-3</code>.

Thank you in advance for the effort reviewing my code. --SQ 

# extract_phonenum.py

## Usage
<code>python extract_phonenum.py myfile.txt</code>

## Description
Extracts phone numbers from a text file, and prints formatted phone numbers.

## Known Issues
N/A

# ensg2hugo.py

## Usage
step 1 <code>./download.sh</code>

step 2 <code>python3 ensg2hugo.py [-f][0-9] [file]</code>

## Description
(1) Running download.sh will automatically download Homo_sapiens.GRCh37.75.gtf.gz from http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens,
and unzip it. It will also automatically clone test unit from https://github.com/davcraig75/unit.

(2) Running ensg2hugo.py will load the database, extract useful information and make a dictionary. Then will load the test unit, fetch for information in specified column, and replace gene_id for gene_name if it exists in dictionary.

## Known Issues
There exists some gene id (such as 'ENSG00000235146') that do not appear in Homo_sapiens.GRCh37.75.gtf, but appear in unit/expres.anal.csv.

This issue can be verified by doing a grep search <code>grep -rl 'ENSG00000283616' ./</code> I'll keep look into this issue, perhaps I have downloaded a wrong database.

# histogram.py 

## Usage
<code>python3 histogram.py [-f][1-4] book1.txt</code>

## Description
Creates a histogram as a png from a file using the specified column in a tab delimited file.

I added an ad hoc tab seperated file called book1.txt.

## Known Issues
N/A


