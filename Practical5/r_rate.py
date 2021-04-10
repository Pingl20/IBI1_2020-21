#define the number
n = 84
#define the rate
r =1.2
#define a variable used to count
i = 0
while i < 5:
    n = n + n*r
    i += 1
#print what we need in a clear way
    print("after 5 rounds, when r rate = %.2f, the number "
      "of infected will be %d" % (r, n))
