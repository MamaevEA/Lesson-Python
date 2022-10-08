#  Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal

def required_accuracy(count):
    print("Enter the required accuracy '0.0001':")
    count = count.quantize(Decimal(input()))
    print(count)

print ('Enter a real number:')
required_accuracy(Decimal(input()))

# num = float(input('Enter a real number: '))

# _, accu = input("Enter the required accuracy '0.0001': ").split(".")
# print(f"{num:.{len(accu)}f}")