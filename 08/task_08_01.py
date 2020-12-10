program = []

with open('input.txt') as data:
  for line in data:
    program.append(line.rstrip().split())

audit = set()
acc = 0
pointer = 0

while pointer not in audit and pointer < len(program):
  instruction = program[pointer][0]
  argument = int(program[pointer][1])
  print('{} {}'.format(instruction.upper(), argument))
  audit.add(pointer)
  if instruction == 'nop':
    pointer += 1
  elif instruction == 'acc':
    acc += argument
    pointer += 1
  elif instruction == 'jmp':
    pointer += argument

print(acc)
