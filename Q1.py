def isPerfect(num):
    sumofNum = 0###A variable to store the sum of all positive divisors
    for i in range(1,num):
        if num%i == 0:
           sumofNum += i
    if sumofNum == num:
        return True
    else:
        return False
num = int(input("Enter a positive integer:"))
if num <= 0:
    print("invalid input... not supported")
    exit()
if isPerfect(num):
    print("Number is Perfect")
else:
    print("Number is not Perfect")
