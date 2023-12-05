

num = int(input('input a number: '))
while 1 > num or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
    num = int(input('input a number: '))
count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count += 1
if count == 0:
    print(True)
else:
    print(False)










            








