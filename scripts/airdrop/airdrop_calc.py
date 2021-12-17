import csv
import json

filename = 'data.csv'
sum = 0

data = {}
sum = 0
filtered_data = {}
out = {}

not_in = {
    '0xBcaA871742Cc603C297e956DF8d6A398ef975551',
    '0xE35E97438Fd16593e285546260C8585dea7909Dd',
    '0x9c71787c5b5885e11F74af7E5Dc1324e87375a95',
    }

for fil in ['usdc.csv', 'usdt.csv']:
    with open(fil, 'r') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        for row in csvreader:
            if row[0] not in not_in:
                if row[0] in data:
                    data[row[0]] += float(row[1].replace(',', ''))
                else :
                    data[row[0]] = float(row[1].replace(',', ''))
            else: 
                print('eric!')

for key, val in data.items():
    if val > 9.5:
        filtered_data[key] = val
        sum += val

for key, val in filtered_data.items():
    out.update({key: val/sum})

with open('early-users-mobius.json', 'w+') as f:
    json.dump(out, f)

    # check 
    sum = 0
    for num in out.values():
        sum += num
    print(sum)