N = int(input("Введіть трьохзначне число: "))
a = (N//100)
b = ((N//10)%10)
c = (N%10)
print(a*b*c)