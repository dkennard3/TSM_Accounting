import sys
#try:
inFile = sys.argv[1]
#except:
#	print(f'usage: python printCSV.py <csv_file>')
#	sys.exit(0)

outFile = 'fixed_date_'+sys.argv[1]
lines = []
new_lines = []
with open(infile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        chunks = line.rstrip('\n').split(',')
        date = datetime.fromtimestamp(int(chunks[-1]))
        date = str(date).split(' ')[0]
        chunks[-1] = date
        line = ','.join(chunks)

with open(outFile, 'w') as f:
    for line in lines:
        f.write(f'{line}\n')

