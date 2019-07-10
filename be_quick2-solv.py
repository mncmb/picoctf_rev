

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def funcy():

    key = [0x99, 0x4d, 0x8e, 0x2e]  # key constructed from last bytes of hxkey, see main
    # key = [0x2c, 0x97, 0xa5, 0xe9] constructed key for the wrong sequence... (be quick1) 
    i = 0
    flag = [0xe9, 0x24, 0xed, 0x41, 0xd9, 0x19, 0xc8, 0x55, 0xef, 0x25, 0xeb, 0x71, 0xfa, 0x24, 0xec, 0x41, 0xf3, 0x2c, 0xed, 0x4d, 0xf7, 0x12, 0xfd, 0x4b, 0xee, 0x38, 0xeb, 0x40, 0xc3, 0x28, 0xd1, 0x4d, 0xc0, 0x23, 0xd1, 0x4c, 0xc7, 0x12, 0xea, 0x41, 0xcd, 0x28, 0xd1, 0x48, 0xc5, 0x3e, 0xfa, 0x71, 0xc0, 0x2e, 0xbb, 0x16, 0x9f, 0x7b, 0xb9, 0x4c, 0xda, 0x00]
    while (i < 0x39):
        # if was an elaborate guess
        if not i % 4 and i // 4:
                key[0] += 1
        

        tmp = ( i >> 0x1f ) >> 0x1e
        flag[i] = flag[i] ^ (key[((i + tmp) & 0x3) - tmp]) # the key expression can be replaced by "i % 4"
        i += 1
    print("".join([chr(elem) for elem in flag]))


if __name__ == "__main__":
    # key = fibi(0x42b)
    # print(key)
    ######################
    # the following key was calculated by fibi
    # hex representation is returned by hex(key)
    # see funcy() for usage of the key
    intkey = 4368447739709774716003881551397205159088952756411141941533814668901464054869881997817744932743716769887780898920209866426445447485522551760777962122217963045451173078851717190916177144613851841799958503738854017612313939353
    hxkey = 0xc15c945eb857334b1857447a4a82d4d62ede32709539f9dae4b7e832368bf63f9c17c1cec85c8a0d43d23713ba63073c7099c1d7c5c0fa1cb94b75ac0ff850b5ca50523ceeab7dfc670a58591dd7cbc9a78aac9fcabd93ba22e8e4d99
    funcy()
