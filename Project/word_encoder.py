from extract_data import *

###############################################################################
# Converts the given string data into ASCII format
###############################################################################

def encode(data):
    i = 0;
    word = 0
    test = []
    new_array = []

    while i < len(data):
        number_string = 0
        word = 0
        ch=0
        for arr in data[i]:
            for s in arr:
                ch = ["".join("%d" % ord(c) for c in s)]
                word += int(ch[0])
            test.append(word)
        new_array.append(test)
        test = []
        i += 1;
    return new_array
