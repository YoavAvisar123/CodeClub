file = open("binary", "r")

text = file.read()

words = text.split(" ")


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


const = to_binary(5, 8)


def xor(input1, input2):
    result = ""
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            result += "1"
        else:
            result += "0"
    return result


crypted = ""


for word in words:
    crypted += str(xor(word, const)) + " "

file = open("binary", "w")
file.write(crypted)
file = open("binary", "r")
