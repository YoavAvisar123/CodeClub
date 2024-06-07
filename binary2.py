def to_binary(number, bits):
    b = ""
    temp = []
    temp_n = 1
    for bit in range(bits):
        temp.insert(0, temp_n)
        temp_n *= 2

    index = 0
    for n in temp:
        if n <= number:
            b += "1"
            number -= n
        else:
            b += "0"
        index += 1
    return b


def to_decimal(binary):
    i = len(binary) - 1
    temp = []
    while i >= 0:
        temp.append(2**i)
        i -= 1

    decimal = 0
    i = 0
    for n in binary:
        if n == "1":
            decimal += temp[i]
        i += 1
    return decimal


def xor(input1, input2):
    result = ""
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            result += "1"
        else:
            result += "0"
    return result


file = open("binary", "r")

text = file.read()

const = to_binary(5, 8)

ascii_list = list(text.encode('ascii'))

crypted = ""

for num in ascii_list:
    num = to_binary(num, 8)
    num = xor(num, const)
    num = to_decimal(num)
    crypted += str(chr(num))


file = open("binary", "w")
file.write(crypted)
