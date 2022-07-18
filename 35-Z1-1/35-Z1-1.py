fi = open("in", "r")
fo = open("out", "w")
foo = []
bar = []

n, q = fi.readline().split(" ")

for i in range(int(n)):
    foo.append(fi.readline().strip())

bar = fi.read().splitlines()
foo.sort()

for i in bar:
    a, b = i.split()
    s = abs(foo.index(a) - foo.index(b)) - 1
    fo.write(str(s)+"\n")


