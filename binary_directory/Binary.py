def to_binary(num, bits):
    b = ""
    temp = []
    temp_n = 1
    for bit in range(bits):
        temp.insert(0, temp_n)
        temp_n *= 2

    index = 0
    for n in temp:
        if n <= num:
            b += "1"
            num -= n
        else:
            b += "0"
        index += 1
    return b


def binary_not(b):
    b2 = ""
    for n in b:
        if n == '1':
            b2 += '0'
        else:
            b2 += '1'
    return b2


def add_to2(b):
    index = len(b) - 1
    b2 = ""
    carry = True
    while index >= 0:
        current = int(b[index])
        if carry:
            current += 1
        if current == 1:
            carry = False
        if current == 2:
            current = 0
        b2 = str(current) + b2
        index -= 1
    return b2


def binary_transform(num, bits):
    binary = to_binary(num, bits)
    binary = binary_not(binary)
    binary = add_to2(binary)
    return binary


def main():
    num = int(input("enter number: "))
    bits = int(input("enter bits: "))
    binary = binary_transform(num, bits)
    print(binary)


main()
