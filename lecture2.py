# hi = "hello there"
# name = "ana"
# greet = hi + name
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# silly = hi + (" " + name) * 3
# print(silly)

# x = 1
# print(x)
# x_str = str(x)
# print("my fav num is", x, ".", "x=", x)
# print("my fav num is" + x_str + "." + "x= " + x_str)

# text = input("Type anything...")
# print(5*text)
# num = int(input("Type a number..."))
# print(5*num)

#demonstration of indentations

# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y!=0:
#         print("therefore, x/y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")

# more complicated with while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

# shortcut with for loop
# for n in range(5):
#     print(n)

#customized range
# mysum = 0
# for i in range (7, 10):
#     mysum += i
# print (mysum)

#value of i starts at 7
#next value of i
# 1st time through loop: mysum = 0 + 7
# 2nd tine through the loop: mysum = 7 + 8
# 3rd time though the loop: mysum = 7 + 8 + 9
# we wil not go to i = 10, because we stop at stop - 1

mysum = 0
for i in range (5, 11, 2):
    mysum += i
print (mysum)

# values of i will be 5, 7, 9