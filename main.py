import CalFun

a=int(input("Enter number1:"))

b=int(input("Enter number2:"))

c=input("Enter the operation to be perform(add/sub/mul/div/mod/sqr):")

if c == "add":
    print(CalFun.add(a,b))

elif c == "sub":
    print(CalFun.sub(a,b))

elif c == "mul":
    print(CalFun.mul(a,b))

elif c == "div":
    print(CalFun.div(a,b))

elif c == "mod":
    print(CalFun.mod(a,b))

elif c == "sqr":
    print(CalFun.sqr(a,b))

else:
    print("Enter the valid operation - (add/sub/mul/div/mod/sqr)")