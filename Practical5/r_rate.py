#define the number and the rate

n = 84
r =1.2
i = 0
while i < 5:
    n = n + n*r
    i += 1
print("after 5 rounds, when r rate = %.2f, the number "
      "of infected will be %d" % (r, n))