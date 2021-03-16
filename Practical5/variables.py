a = 50802
b = 190784
c = 31021
d = abs(a - c)
e = abs(a - b)
if d > e:
    print("d>e")
elif d == e:
    print("d=e")
elif d < e:
    print("d<e")

X = True
Y = False
Z = (X and not Y) or (Y and not X)
print(Z)
W = X != Y
print(W == Z)
