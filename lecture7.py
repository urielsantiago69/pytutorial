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
