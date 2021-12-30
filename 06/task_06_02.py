total = 0

answers = []
ALL_ANSWERS = 'abcdefghijklmnopqrstuvwxyz'
with open('input.txt', 'r') as data:
  accumulator = set(ALL_ANSWERS)
  for line in data:
    line = line.strip()

    if line == '':
      answers.append(accumulator)
      accumulator = set(ALL_ANSWERS)
    else:
      accumulator &= set(line)

if len(accumulator) > 0:
  answers.append(accumulator)
  accumulator = set(ALL_ANSWERS)

for answer in answers:
  total += len(answer)

print(total)
