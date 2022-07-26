from bitcoinaddress import Wallet
from multiprocessing import Process
import csv

key_file_name = "found_wallets.txt"
excel_wallet = "wallets.csv"
mode_key_file = "a"
new_list = []
curr_key = 114126733
last_key = 115792089237316195423570985008687907853269984665640564039457584007913129639935
last_wallet_number = 10000


def wallets_list(name_of_file, last_wallet_num):
    with open(name_of_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i in range(0, last_wallet_num):
        new_data = data[i][0]
        new_list.append(new_data)


def write_to_a_file(filename, mode, string):
    f = open(filename, mode)
    f.write("------------------------------------------------------")
    f.write(str(string))
    f.write("------------------------------------------------------")
    f.close()


def print_status(key):
    print('------------------------------------------------------')
    print(key)
    print('------------------------------------------------------')


def main_program(cur_key, las_key):
    for i in range(cur_key, las_key):
        new = "{:064X}".format(i)
        wallet = Wallet(new)
        print(f"Num KEY = {i}")
        # print(wallet)
        if wallet.address.mainnet.pubaddr3 in new_list:
            write_to_a_file(key_file_name, mode_key_file, wallet)
            print_status(wallet)
        elif wallet.address.mainnet.pubaddr1 in new_list:
            write_to_a_file(key_file_name, mode_key_file, wallet)
            print_status(wallet)
        elif wallet.address.mainnet.pubaddr1c in new_list:
            write_to_a_file(key_file_name, mode_key_file, wallet)
            print_status(wallet)
        elif wallet.address.mainnet.pubaddrbc1_P2WPKH in new_list:
            write_to_a_file(key_file_name, mode_key_file, wallet)
            print_status(wallet)
        elif wallet.address.mainnet.pubaddrbc1_P2WSH in new_list:
            write_to_a_file(key_file_name, mode_key_file, wallet)
            print_status(wallet)
        i += 1


wallets_list(excel_wallet, last_wallet_number)

p1 = Process(target=main_program, args=(curr_key, last_key))
# p2 = Process(target=main_program, args=(50377288, 60377288))
# p3 = Process(target=main_program, args=(60377288, 70377288))
# p4 = Process(target=main_program, args=(70377288, 80377288))
# p5 = Process(target=main_program, args=(80377288, 90377288))
# p6 = Process(target=main_program, args=(90377288, 100377288))
# p7 = Process(target=main_program, args=(100377288, 110377288))

if __name__ == '__main__':
    p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    # p6.start()
    # p7.start()
    p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()
    # p6.join()
    # p7.join()
