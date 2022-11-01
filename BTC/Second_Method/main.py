from bitcoinaddress import Wallet
import csv

key_file_name = "found_wallets.txt"
mode_key_file = "a"
new_list = []
curr_key = 19000182
last_key = 115792089237316195423570985008687907853269984665640564039457584007913129639935

with open('wallets.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(0, 2000):
    new_Data = data[i][0]
    new_list.append(new_Data)


def write_to_a_file(filename, mode):
    f = open(filename, mode)
    f.write(str(wallet))
    f.close()


def print_status(key):
    print('------------------------------------------------------')
    print(key)
    print('------------------------------------------------------')


for i in range(curr_key, last_key):
    new = "{:064X}".format(i)
    wallet = Wallet(new)
    # print(wallet)
    print(f"Num KEY = {i}")
    if wallet.address.mainnet.pubaddr3 in new_list:
        write_to_a_file(key_file_name, mode_key_file)
        print_status(wallet)
    elif wallet.address.mainnet.pubaddr1 in new_list:
        write_to_a_file(key_file_name, mode_key_file)
        print_status(wallet)
    elif wallet.address.mainnet.pubaddr1c in new_list:
        write_to_a_file(key_file_name, mode_key_file)
        print_status(wallet)
    elif wallet.address.mainnet.pubaddrbc1_P2WPKH in new_list:
        write_to_a_file(key_file_name, mode_key_file)
        print_status(wallet)
    elif wallet.address.mainnet.pubaddrbc1_P2WSH in new_list:
        write_to_a_file(key_file_name, mode_key_file)
        print_status(wallet)
    i += 1
