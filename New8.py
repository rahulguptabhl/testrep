import random
for x in range(6,36):
    print random.randrange(6),random.randrange(6)
    print repr(x*x*x).rjust(4)

