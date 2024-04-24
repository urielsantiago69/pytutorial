def mult_iter(a, b)
  result = 0
  while b > 0:  #iteration
    result += a #current value of the computation, running a sum
    b -= 1 #current value of the iteration variable
  return result

#recursive version
def mult (a,b):
    if b == 1:      #covers the base case of b = 1
        return a
    else:
        return a + mult(a, b-1)


#recursive function scope example
#definition of factorial
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n-1)
#note that the function calls on itself

#at this point i am invoking the function
print(fact(4))

#iterative version of factorial computation

def factorial_iter(n):
  def factorial_iter(n):
  prod = 1
  for i in range(1,n+1):
      prod *= i
  return prod

#inductive reasoning to test recursive code

def multi_iter(a, b):
  result = 0
  while b > 0:
    result += a
    b -= 1
  return result

def mult(a, b):
  if b == 1:
    return a
  else:
    return a + mult(a, b-1)