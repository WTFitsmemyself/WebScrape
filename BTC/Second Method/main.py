from bitcoinaddress import Wallet

choosen_one = '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'
current_num_key = 7881
last_key = 64**16

for i in range(current_num_key, last_key):
    new = "{:064X}".format(i)
    wallet = Wallet(new)
    # print(wallet)
    print(f"Num KEY = {i}")
    if wallet.address.mainnet.pubaddr3 in choosen_one:
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddr1 == choosen_one:
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddr1c == choosen_one:
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddrbc1_P2WPKH == choosen_one:
        print(wallet)
        print('------------------------------------------------------')
    elif wallet.address.mainnet.pubaddrbc1_P2WSH == choosen_one:
        print(wallet)
        print('------------------------------------------------------')
    i += 1


# address_1 = wallet.address.mainnet.pubaddr1
# address_1_comp = wallet.address.mainnet.pubaddr1c
# address_3 = wallet.address.mainnet.pubaddr3
# address_bc1_P2WPKH = wallet.address.mainnet.pubaddrbc1_P2WPKH
# address_bc1_P2WSH = wallet.address.mainnet.pubaddrbc1_P2WSH

