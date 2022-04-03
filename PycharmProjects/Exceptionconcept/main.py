
# Python program to handle simple runtime error
a=[1,2,3]
try:
    print("Second element = %d" % (a[1]))
    print("Fourth element = %d" % (a[3]))
except:
    print("An error occured")

# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not

