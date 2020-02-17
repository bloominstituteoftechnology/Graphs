
# simple recursion example
def recurse(x):
   if x > 0:
       print(x)

       recurse(x - 1)

recurse(10)