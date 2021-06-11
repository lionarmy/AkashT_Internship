#1)Comments------------------------------------------------------------------------------------------------

#This is a comment
#print out Hello

"""This is also a
perfect example of
multi-line comments"""

#2)Variables-------------------------------------------------------------------------------------------------

number = 10
website = "nikhilkumbhani.com"
print(number)
print(website)

print("\n")

#Changing the value
website = "akash.com"
print(website)

website = "nikhil.com"
print(website)

print("\n")
#Assigning multiple values to multiple variables

a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)


print("\n")
#3) Datat Types------------------------------------------------------------------------------------------------

#numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
print("\n")

#String
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)

print("\n")

#List
a = [5,10,15,20,25,30,35,40]

print("a[2] = ", a[2])

print("a[0:3] = ", a[0:3])

print("a[5:] = ", a[5:])

print("\n")

#Tuple
t = (5,'program', 1+3j)

print("t[1] = ", t[1])

print("\n")
#Dictionary

d = {1:'value','key':2}
print("d[1] = ", d[1])

print("d['key'] = ", d['key'])


