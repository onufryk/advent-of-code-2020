from functools import reduce

offsets = []
with open('input.txt', 'r') as data:
  lines = data.readlines()
  offsets = [int(route) if route != 'x' else None for route in lines[1].rstrip().split(',')]

print(offsets)

m = list(filter(None, offsets))
C = [len(offsets) - 1 - i for i, o in enumerate(offsets) if o is not None]

print('m(i)={}'.format(m))
print('C(i)={}'.format(C))

M = product = reduce((lambda x, y: x * y), m)

print('M={}'.format(M))

Mi = [int(M/mi) for mi in m]

print('M(i)={}'.format(Mi))

y = []
for i in range(len(m)):
  for j in range(1, m[i]):
    if ((Mi[i] * j) - 1) % m[i] == 0:
      y.append(j)

print('y(i)={}'.format(y))

x0 = sum(Mi[i] * y[i] * C[i] for i in range(len(m)))

print('x0={}'.format(x0))

x = x0 - (M * (x0 // M))

print('x={}'.format(x))

t = x - max(C)

print('t={}'.format(t))
