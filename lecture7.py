#example for boundary intuition testing

def is_bigger (x,y):
  """Assumes x and y are integers
  Returns True if x is bigger than y, False otherwise"""


#example for black box testing
def sqrt(x, eps):
  """Assumes x, eps, floats, x >= 0, eps > 0
  Returns res such that x-eps <= res*res <= x+eps"""

#example for glass box testing

def abs(x):
    """Assumes x is an int
    Returns x if x >= 0, -x otherwise"""
    if x < -1:
      return -x
    else:
      return x

# if x is less than minus 1, say minus 2 - it returns -2
# otherwise, return x. test with 2, returns 2 as expected
# every branch of the conditional is covered, we are path complete
# however abs (-1) incorrectly returns -1

#exception handling
def sample_exception():
try:
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  print(a/b)
except:
  print("Bug in user input")


def sample_exception2():
try:
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  print(a/b)
  print(a+b)
except ValueError:
  print("Could not convert to a number")
except ZeroDivisionError:
print("Could not convert to a number")
except:
  print("Something really went wrong")


def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios

print(get_ratios([1, 4], [2, 4]))