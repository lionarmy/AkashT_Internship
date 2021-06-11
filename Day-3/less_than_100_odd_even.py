num = int(input("Enter a number: "))
if num < 100 :
    print("inputed number is less than 100")
    mod = num % 2
    if mod > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
else :
    print("inputed number is not less than 100")        