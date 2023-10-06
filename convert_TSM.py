import sys
import re
import json
from datetime import datetime
from unidecode import unidecode
import jedi

jedi.get_default_environment()
'''
1) convert unix Timestamp to datetime obj yyyy-mm-dd
2) remove colons and dashes, replace w/ empty '' string (except the date)
3) double quote '..' around itemString, itemName, otherplayer, player, and date
4) replace 'special' characters in otherPlayer with an A
re.sub(r'pattern', 'with_string', str)
'''
try:
    export_file = sys.argv[1]
    table_name = sys.argv[2]
except IndexError:
    print('usage: python getRecent.py TSM_csv_export_file desired_table_name')
    sys.exit(0)
else:
    if re.findall(r'\d', table_name) or not table_name.strip():
        print(f'\nInvalid name: {table_name} --  \
            name cannot contain numbers nor be an empty string\n')
        sys.exit(-1)

with open(export_file,'r') as f:
    lines = f.readlines()

headers = lines[0].rstrip('\n').split(',') 
with open('types.json', 'r') as f:
    types = json.load(f, types)





headLine = f"create or replace table {table_name} (\n\t{headers}"

start = f'insert into {table_name} values ('
end = f');'

with open(f'{table_name}_from_{export_file.split(".")[0]}.txt', 'w') as f:
    for line in lines:
        tmp = []
        line = line.replace(':', '')
        line = line.replace('-', '')
        line = line.replace('\'', '')
        chunks = line.split(',')
        for chunk in chunks:
            # timestamp(date) of record
            if re.match(r'\d{10}',chunk):
                date = datetime.fromtimestamp(int(chunk))
                date = str(date).split(' ')[0]
                tmp.append('\''+date+'\'')

                # any number (int or float) that is not a timestamp
            elif re.match(r'\d{1,4}',chunk):
                if headers[chunks.index(chunk)] in ('price','amount'):
                    tmp.append(str(round((float(chunk)/10000),2)))
                else:
                    tmp.append(chunk)

                # A Player's name, itemString, itemName, or source
            elif re.match(r'[((\D\s?)\+)|(i\:\d\+)]',chunk):
                tmp.append('\''+unidecode(chunk).rstrip('\n')+'\'')

        f.write(start+','.join(tmp)+end+'\n')
