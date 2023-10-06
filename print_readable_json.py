import json
import sys

try:
    in_file = sys.argv[1]
except:
    print('usage: python print_readable_json.py <filename>.json')
    sys.exit(-1)
with open(in_file,'r') as f:
    data = json.load(f)

s = in_file.strip().split('.')[0]
outfile = f"{s}_readable.json"
with open(outfile, 'w') as g:
    g.write(json.dumps(data,indent=2))
'''
curr_max = 0
for key in data.keys():
    #new_max = max(len(str(entry)) for entry in data[key])
    new_max = max(len(str(entry)) for entry in data)
    if new_max > curr_max:
        curr_max = new_max

for key in data.keys():
    border_width = len(key)
    print(('/'+('_'*border_width)+'\\').center(curr_max))
    print(('|'+key+'|').center(curr_max))
    print(('\\'+('_'*border_width)+'/').center(curr_max))
    for entry in data[key]:
        print(f'{entry}')	
    print()
'''
