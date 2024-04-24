# def is_even(i):

#     '''
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     '''

#     print("inside is_even")     #run some commands
#     return i%2 == 0             #return something
# function call
# is_even(3)

# def f(x):
# x is a formal parameter
# they don't have a value yet - this is only determined at the function call
    # x =x + 1
    # print ('in f(x): x =', x)
    # return x


# x = 3
# z = f(x)
# x in this case is the actual parameter

# def is_even(i):
#     '''
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     '''
#     remainder = i % 2           #run some commands
#     return remainder == 0             #return something

# # use the is_even function

# for i in range(20):
#    if is_even(i):
#       print(i, "even")
#    else:
#       print(i, "odd")

# #functions as arguments
# def func_a():
#     print ('inside func_a')

# def func_b(y):
#     print ('inside func_b')
#     return y

# def func_c(z):
#     print ('inside func_c')
#     return z()

# print (func_a())
# print (5*func_b(2))
# print (func_c(func_a))

variable access and scope

def f(y):
    x = 1
    x += 1
    print(x)
# x is redefined in scope of f

x = 5
f(x) 
print(x)

#the x in the main program is different from the x returned by x

def g(y):
    print(x)
    print(x+1)
# x is from outside of g


x = 5
g(x)
print(x)
#the x inside g is picked up from the scope that called g
# no x inside scope, temporarily goes outside scope to the program that called the function

#this is not allowed
def h(y):
    x += 1

# did not initialize x within the local scope
# but directly trying to change the value of x that is from the global scope
x = 5
h(x)
print(x)

# harder scope example

def g(x):
    # nesting a function within a function
    def h():
        x = 'abc'
    x = x + 1
    print ('g: x = ' , x)
    h ()
    return x

x = 3
z = g(x)

# try debugging this in pythontutorial.org



