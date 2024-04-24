#sample tuples

# te=()
# t=(2, "mit",3)
# x=t[1:3]
# print(x)

#tuples can enable functions to return more than one value (it returns the tuple)

# def quotient_and_remainder(x,y):
#         q = x//y
#         r = x%y
#         return (q,r)

# (quot, rem) = quotient_and_remainder(4,5)

# print(quot, rem)


#iterating over a tuple
#aTuple is a tuple composed of other tuples
#first element of an inner tuple is an int
#second element of the inner tuple is a string
def get_data(aTuple):
  nums = ()  #create an empty tuple called nums()
  words = ()  #create an empty tuple called words()

  for t in aTuple:
    #for loop iterates through every inner tuple in aTuple
    #each time through the loop, add an  element of the current inner tuple to the nums tuple
    # previous value of nums and add to it a singleton tuple
    # a single tuple of one element (whatever is at position
    # zero of the current tuple (an integer)
    nums = nums + (t[0], )
    # populating the words tuple
    # but only if not part of the existing word tuple
    if t[1] not in words:
      words = words + (t[1], )
  min_n = min(nums)
  max_n = max(nums)
  unique_words = len(words)
  return (min_n, max_n, unique_words)


#iterating over a list
#compute the sum of element of a list
L = [2, 1, 3]
# total = 0
# for i in range(len(L)):
#   total += L[i]

# print(len(L))
# print(total)

# same operation as above,but cleaner
# total = 0
# for i in L:
#   total += i
# print(total)

# note
# list elements are indexed 0 to len(L)-1
# range(n) goes from 0 to n-1

# aliases and side effects
# hot is an alias for warm - changing one
# changes the other
# append() has a side effect

# a = 1
# b = a
# print(a)
# print(b)

# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

# cloning a list

# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print(chill)
# print(cool)

# mutation in the context of sorting

# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)

# mutation in nested lists

# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)
# print(brightcolors)
# hot.append('pink')
# print(hot)
# print(brightcolors)

# iterating through a list as you mutate it
# wrong way:

def remove_dups(L1, L2):
  for e in L1:
    if e in L2:
      L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2, 5, 6]
remove_dups (L1,, L2)

# correct way:
def remove_dups(L1, L2):
  L1_copy = L1[:]
  for e in L1_copy:
    if e in L2:
      L1.remove(e)

# clone first, and iterate over the clone