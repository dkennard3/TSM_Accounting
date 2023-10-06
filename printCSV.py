from pretty_csv import pretty_csv
import sys
#try:
pretty_csv.pretty_file(sys.argv[1])
#except:
#	print(f'usage: python printCSV.py <csv_file>')
#	sys.exit(0)

result = 'new_'+sys.argv[1]
with open(result, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip('\n'))

