print("enter first number: ")
a = int(input())

print("enter second number: ")
b = int(input())

print("enter an operator: +, -, *, /")
o = input()

if o == '+':
    print(a+b)
if o == '-':
    print(a-b)
if o == '*':
    print(a*b)
if o == '/':
    if b == 0:
        print("not divisible by 0")
    else:
        print(a/b)
    


