import csv
new_list = []
data_find = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'
with open('/Users/hosyn/Desktop/wallets.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(0, 2000):
    new_Data = data[i][0]
    new_list.append(new_Data)

if data_find in new_list:
    print(f"found: {data_find}")
