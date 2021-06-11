#1
def my_function():
    print("Hello world")

my_function()
my_function()

#2
def nikhil(x):
    print(x, " is the new black.")

nikhil("\nPython")

#3
def add(a, b):
    return a + b
  
def is_true(a):
    return bool(a)
  
res = add(2, 3)
print("\nResult of add function is {}".format(res))
  
res = is_true(2<5)
print("Result of is_true function is {}".format(res))

#4
print("\n")
def add1 (*num):
    sum1 =0 
    for n in num:
        sum1 = sum1 + n
    print("sum:",sum1)

add1(20,30)
add1(10,20,30)

