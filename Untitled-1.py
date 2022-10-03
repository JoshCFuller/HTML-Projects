from re import A

def has_bit_parity(a_number):
    parity = False
    while a_number:
        parity = not parity
        a_number = a_number & (a_number - 1)
    return int(parity)
    
if __name__ == '__main__':
    a_number = 9
    
    print ("1" if has_bit_parity(a_number) else "0")
    