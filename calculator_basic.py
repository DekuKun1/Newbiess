a=float(input("a= "))
cal = input("")
b=float(input("b= "))


if cal.lower() =="+":
    print("Ans:", a+b)
elif cal.lower() =="-":
    print("Ans:",a-b)
elif cal.lower() =="*":
    print("Ans:",a*b)
elif cal.lower() =="/":
    print("Ans:",a/b)   
elif cal.lower() =="%":
    print("Ans:",a/100*b)
# elif cal.lower() =="+%":
#     print("Ans:",a+b/100)
# elif cal.lower() =="-%":
#     print("Ans:",a-b/100)
# elif cal.lower() =="*%":
#     print("Ans:",a*b/100)

else:
    print("try again")
    



