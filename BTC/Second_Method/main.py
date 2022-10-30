from bitcoinaddress import Wallet
import csv

new_list = []
with open('wallets.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(0, 2000):
    new_Data = data[i][0]
    new_list.append(new_Data)

current_num_key = 226781
last_key = 115792089237316195423570985008687907852837564279074904382605163141518161494336

for i in range(current_num_key, last_key):
    new = "{:064X}".format(i)
    wallet = Wallet(new)
    # print(wallet)
    print(f"Num KEY = {i}")
    if wallet.address.mainnet.pubaddr3 in new_list:
        f = open("found_wallets.txt", "a")
        f.write(str(wallet))
        f.close()
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddr1 in new_list:
        f = open("found_wallets.txt", "a")
        f.write(str(wallet))
        f.close()
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddr1c in new_list:
        f = open("found_wallets.txt", "a")
        f.write(str(wallet))
        f.close()
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddrbc1_P2WPKH in new_list:
        f = open("found_wallets.txt", "a")
        f.write(str(wallet))
        f.close()
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddrbc1_P2WSH in new_list:
        f = open("found_wallets.txt", "a")
        f.write(str(wallet))
        f.close()
        print(wallet)
        print('------------------------------------------------------')
    i += 1
