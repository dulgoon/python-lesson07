a = int(input("a:"))
b = 0
c = 0
while a > 0:
    c = a % 10
    b += c
    a = a // 10
    print(c)
print("niilber",b)
    
