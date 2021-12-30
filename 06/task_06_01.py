total = 0

answers = []
with open('input.txt', 'r') as data:
  accumulator = set()
  for line in data:
    line = line.strip()

    if line == '':
      answers.append(accumulator)
      accumulator = set()
    else:
      accumulator |= set(line)

if len(accumulator) > 0:
  answers.append(accumulator)
  accumulator = set()

for answer in answers:
  total += len(answer)

print(total)
