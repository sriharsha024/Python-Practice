def myfunc(a,b,c=0,d=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d)) * 0.05

print(myfunc(40, 60,100,100))  # Output: 15.0

#error case
#print(myfunc(40, 60,20,3,0))  # Output: 6.15

def myfunc_1(*args):
    # Returns 5% of the sum of all arguments
    return sum(args) * 0.05

print(myfunc_1(40, 60,100,300))  # Output: 15.0
print(myfunc_1(40, 60,20,3,0))  # Output: 6.15

def myfunc_2(* args):
    print(args)

myfunc_2(1,2,3,4,5)  # Output: (1, 2, 3, 4, 5)
myfunc_2('a','b','c')  # Output: ('a', 'b', 'c')

def myfunc_3(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")

myfunc_3(fruit='apple', veggie='lettuce')  # Output: My fruit of choice is apple
myfunc_3(veggie='lettuce')  # Output: I did not find any fruit here
# myfunc_3(fruit='apple', veggie='lettuce', fruit='banana')  # Output: My fruit of choice is apple

def myfunc_4(* args, **kwargs):
    print("I would like  to eat {} {}".format(args[2], kwargs['food']))

myfunc_4(3, 2, 5, fruit='apple', food='eggs', animal='dog')  # Output: I would like  to eat 5 eggs