import csv

new_list = []
data_find = '_'

with open('wallets.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(0, 2000):
    new_Data = data[i][0]
    new_list.append(new_Data)

if data_find in new_list:
    print(f"found: {data_find}")

print(new_list[0])
