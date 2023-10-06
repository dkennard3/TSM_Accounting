import json
import sys

try:
    inFile = sys.argv[1]
except:
    print(f'usage: python costEffect.py <recipe JSON file>')
    sys.exit(0)

recipes = {}
with open(inFile,'r') as g:
    recipes = json.load(g)

auctions = {}
with open('converted_auction_report.json', 'r') as f1:
    auctions = json.load(f1)
auction_attr = list(auctions[list(auctions.keys())[0]].keys())

expenses = {}
with open('converted_expense_report.json', 'r') as f2:
    expenses = json.load(f2)
expense_attr = list(expenses[list(expenses.keys())[0]].keys())

missing_auctions = []
missing_expenses = []
crafted = {}
for item in recipes.keys():
    try:
        avg_sale = auctions[item][auction_attr[1]]
except:
        continue
        crafted[item] = {}
        no_auctions, no_expenses = [], []
        t = recipes[item]
        total_cost = 0e-2
        total_sale = 0e-2
        for mat,qty in t:
            try:
                check = expenses[mat]
except KeyError:
#print(f'Item {mat} not found in expense history')
missing_expenses.append(mat)
no_expenses.append(mat)
        else:
cost = expenses[mat][expense_attr[1]]
total_cost += round(cost*qty,2)
try:
    check = auctions[mat]
except KeyError:
    #print(f'Item {mat} not found in auction history')
    missing_auctions.append(mat)
    no_auctions.append(mat)
    else:
    sale = auctions[mat][auction_attr[1]]
    total_sale += round(sale*qty,2)
    crafted[item]['total_cost'] = total_cost
    crafted[item]['total_sale'] = total_sale
    crafted[item]['no_auctions'] = no_auctions
    crafted[item]['no_expenses'] = no_expenses
    crafted[item]['avg_sale'] = auctions[item][auction_attr[1]]

for item in crafted.keys():
    avg_sale = crafted[item]['avg_sale'] 
    total_cost = crafted[item]['total_cost']
    profit = round(avg_sale-float(total_cost),2)
    no_auctions = crafted[item]['no_auctions'] 
    no_expenses = crafted[item]['no_expenses'] 
    mat_list = [pair[0]+' x'+str(pair[1]) for pair in recipes[item]]
    align = []
    for i in range(0,len(mat_list)-1,2):
        align.append(f'{mat_list[i]}, {mat_list[i+1]}')
        f = '\n'.join(align)
        print('/'*25)
        print(f'Item: {item}')
        print()
        print(f'{f}')
        print('*'*25)
        print(f'Avg. Sale: {avg_sale}g')
        print(f'Cost for buying mats: {total_cost}g')
        print(f'Mats NOT included in cost: {no_expenses}')
        print(f'Total Profit: {profit}g') 
        print(f'Mats NOT included in profit: {no_auctions}')
        print()
