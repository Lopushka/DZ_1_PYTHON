b = input("Введите номер билета: ")
b1 = int(b[0])
b2 = int(b[1])
b3 = int(b[2])
b4 = int(b[3])
b5 = int(b[4])
b6 = int(b[5])
if b1+b2+b3 == b4+b5+b6:
    print("Съешь его! Он счастливый.")
else:
    print("Билет не счастливый.")