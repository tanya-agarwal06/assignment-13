#quess 1:
from builtins import ZeroDivisionError

try:
    a=3
    if a<4:
      a=a/(a-3)
      print(a)
except ZeroDivisionError:
    print("division by zero error\n")


#ques 2:
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("An Index error encountered,the index given is not present")

#ques 3:

try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
   # raise

#ques 4:
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#ques 5:
#import error
try:
    import sjawn  #any library which is not present when entered
except ImportError:
    print("Library imported is not available")

#value error

try:
     n= int(input("enter a number"))
except ValueError:
    print("PLease enter the correct value of integer")

#index error
try:
    n = [3, 5, 7]
    def myFun(x):
        for i in x:
            print(x[i])
            myFun(n)
except IndexError:
    print("The index is not present")

#ques 6:
class AgeTooSmallError(Exception):
    pass
age=0
while age < 18 :
    try:
        age = int(input("Enter your age"))
        if age < 18:
           raise AgeTooSmallError
    except AgeTooSmallError:
      print("Enter Only Integer")
    else:
        print("Program done Eligible person to do stuff")