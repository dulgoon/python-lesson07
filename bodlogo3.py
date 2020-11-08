a = int(input("a:"))
b = 0
c = 0
while a > 0:
    b += c
    c = a % 10
    a = a // 10
    print(c)
print("niilber",b)
    
