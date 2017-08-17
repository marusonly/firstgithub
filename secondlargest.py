__author__ = 'marva'

x = 0
x1 = 0
li = [1, 2, 8, 4, 7, 5, 6]

for n in li:
    if n >= x:
        x1 = x
        x = n
    elif n > x1:
        x1 = n

print ("highest is %d,second is %d" % (x, x1))
