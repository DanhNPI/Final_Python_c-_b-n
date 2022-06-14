def dec2bin(dec_num):
    temp = ''
    bin_num = ''

    while (True):
        thuong = dec_num//2
        if thuong != 0:
            temp += str(dec_num%2)
            dec_num = thuong
        else:
            temp += str(dec_num%2)
            do_dai = len(temp)
            while(do_dai<16):
                temp += str(0)
                do_dai = len(temp)
            break
        
    for i in range(len(temp)-1, -1, -1):
        bin_num += temp[i]
    return bin_num

def dec2hex(dec_num):
    bin2hex = {'0000': '0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5'
                ,'0110':'6', '0111':'7', '1000':'8', '1001':'9', '1010':'A', '1011':'B',
                '1100':'C', '1101':'D', '1110':'E', '1111':'F'}   

    temp = dec2bin(dec_num)
    temp1 = ''
    hex_num = ''
    count = 0

    for i in range(len(temp)):
        temp1 += temp[i]
        if (count==3):
            temp1 += ' '
            count = 0
        else:
            count += 1
    temp1 = temp1.split()

    for i in temp1:
        if i in bin2hex.keys():
            hex_num += bin2hex[i]
    return hex_num

def bin2dec(bin_num):
    dec_num = 0
    for i in range(len(bin_num)):
        if bin_num[i] in ['0', '1']:
            dec_num += int(bin_num[i])*(2**((len(bin_num)-1)-i))
    return dec_num

def hex2dec(hex_num):
    temp = ''
    hex2bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4':'0100','5':'0101'
            ,'6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    for i in range(len(hex_num)):
        if hex_num[i] in hex2bin.keys():
            temp += hex2bin[hex_num[i]]
    dec_num = bin2dec(temp)
    return dec_num

def bin2hex(bin_num):
    temp1 = ''
    hex_num = ''
    bin2hex = {'0000': '0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5'
                ,'0110':'6', '0111':'7', '1000':'8', '1001':'9', '1010':'A', '1011':'B',
                '1100':'C', '1101':'D', '1110':'E', '1111':'F'}
    if len(bin_num) < 4:
        bin_num = bin_num.rjust(4, '0')
    elif len(bin_num) < 8:
        bin_num = bin_num.rjust(8, '0')
    elif len(bin_num) < 16:
        bin_num = bin_num.rjust(16, '0')

    count = 0
    for i in range(len(bin_num)):
        temp1 += bin_num[i]
        if (count==3):
            temp1 += ' '
            count = 0
        else:
            count += 1
    temp1 = temp1.split()

    for i in temp1:
        if i in bin2hex.keys():
            hex_num += bin2hex[i]
    return hex_num    

def hex2bin(hex_num):
    bin_num = ''
    hex2bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4':'0100','5':'0101'
            ,'6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
            'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    for index in range (len(hex_num)):
        bin_num += hex2bin[hex_num[index]]
    return bin_num





