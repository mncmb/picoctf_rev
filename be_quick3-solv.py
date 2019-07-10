

def keycalc(argsi=0x19965):
    table = create_table(0x19965)
    print(table[0x19965])

def create_table(numsi):
    table = []
    for i in range(numsi+1):
        if i < 5:
            table.append(i*i + 0x2345)
        else:
            table.append(table[i-5] * 0x1234 +( table[i-1]-table[i-2]) + ( table[i-3]-table[i-4]) )
        if i % 1000 == 0 :
            print(i)
    return table


def funcy():
    # key = fibi(0x42b)
    # print(key)
    key = [0x9e, 0x22, 0xc9, 0x8e][::-1]  # key constructed from last bytes of hxkey, see main
    # key = [0x2c, 0x97, 0xa5, 0xe9] constructed key for the wrong sequence ...
    i = 0
    flag = [0xfe, 0xa0, 0x41, 0xf1, 0xcc, 0x9d, 0x64, 0xe5, 0xf4, 0xb0, 0x4c, 0xff, 0xfc, 0xa0, 0x41, 0xc1, 0xe2, 0xbb, 0x12, 0xf9, 0xe1, 0xa8, 0x4f, 0xf3, 0xfd, 0xa7, 0x45, 0xc1, 0xf3, 0xbd, 0x55, 0xc1, 0xf4, 0xfc, 0x41, 0xaa, 0xa2, 0xff, 0x16, 0xab, 0xe5, 0x00]
    while (i < 0x29):
        # if was an elaborate guess
        if not i % 4 and i // 4:
                key[0] += 1
        

        tmp = ( i >> 0x1f ) >> 0x1e
        flag[i] = flag[i] ^ (key[((i + tmp) & 0x3) - tmp]) # the key expression can be replaced by "i % 4"
        i += 1
    print("".join([chr(elem) for elem in flag]))


if __name__ == "__main__":
    #keycalc()
    funcy()
    # executed keycalc at first, then got giant number, only last few digits are 
    # relevant bc using modulo arithmetic to cut off overflowing int values keep 
    # the last digits the same
    hex(79608696550767707287111413127142208284353010408137037056617197259150)
    # only the last digits of hexkey are used as a key due to the program 
    # being compiled for x86-64, which uses little endian
    hexkey = '0x2f3ee057d152532a95866c26f2885d2aad100a4a1a7b075ee9e22c98e'