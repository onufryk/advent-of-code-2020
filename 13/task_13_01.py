ready_to_depart = 0
fleet = []
with open('input.txt', 'r') as data:
  lines = data.readlines()
  ready_to_depart = int(lines[0])
  fleet = [int(route) for route in lines[1].rstrip().split(',') if route != 'x']

print(ready_to_depart)
print(fleet)

min_diff = ready_to_depart
min_route = None
diffs = {}
for route in fleet:
  print('{:-^100}'.format(route))
  diff = route - (ready_to_depart % route)
  diffs[route] = diff
  if diff < min_diff:
    min_diff = diff
    min_route = route

for r, d in diffs.items():
  print(r, d, ready_to_depart + d)

print(min_route, min_diff, min_route * min_diff)