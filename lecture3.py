#len() function
# s = "abc"
# length = len(s)
# print(length)

# indexing into a string
# s = "abc"
# print (s[1])

# slicing a string
# s = "abcdefgh"
# print(s[3:6])     #evaluates to "def", same as s[3:6:1]
# print(s[3:6:2])   #evaluates to "df"
# print(s[::])      #evaluates to "abcdefgh", same as s[0:len(s):1], to the string itself
# print(s[::-1])    #evaluates to "hgfedcba", same as s[-1:-len(s)+1:-1], to the inverse of the string
# print(s[4:1:-2])  #evaluates to "ec",

#binding to a new object
# s = "hello"
# s = 'y' + s[1:len(s)]
# print(s)

#iterating through numbers derived from the length of a string
# s = "abcdefghijk"

# for index in range(len(s)):
#     if s[index] == 'i' or s[index]=='o':
#         print("There is an i or u")

#more readable, more "pythonic"
# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("From 1 to 10, how enthusiastic are you?: "))

#while loop, indexing from 0 up to the length of the word - 1
# i = 0
# while i < len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)
#     i += 1
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")

#refactoring of the above program based on iterating through a sequence

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("From 1 to 10, how enthusiastic are you?: "))
# for char in word:
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")

#guess and check sample
# cube = 8
# for guess in range (cube+1):
#     if guess ** 3 == cube:
#         print("Cube root of", cube, "is", guess)

# revised to:
# 1) deal with negative cubes and
# 2) tells the user if cube is not a perfect cube

# exhaustive enumeration solution
# cube = 8
# for guess in range (abs(cube)+1):
#     if guess ** 3 >= abs(cube):
#         break
#         #because there is no need to keep searching the moment
#         #guess**3 is greater than the cube
# if guess != abs(cube):
#         print(cube, 'is not a perfect cube')
# else:
#         if cube < 0:
#               guess = -guess
#         print('Cube root of  ' +str(cube)+', is, '+str(guess))

#approximate solution of a cube root
# cube = 27
# epsilon = 0.01
# guess = 0.0
# increment = 0.0001
# num_guesses = 0
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
# print ('Number of guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#     print('Failed on cube root of', cube)
# else:
#     print(guess, 'is close to the cube root of', cube)

#code for bisection search
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
  if guess**3 < cube:
    low = guess
  else:
    high = guess
    guess = (high + low) / 2.0
    num_guesses
