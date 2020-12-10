program = []

with open('input.txt') as data:
  for line in data:
    program.append(line.rstrip().split())

pointer = 0
acc = 0
audit_log = set()
instruction_changed = set()
current_instruction_changed = None

while pointer < len(program):
  if pointer in audit_log:
    print('{:-^100}'.format(' ATTEMPT {} '.format(len(instruction_changed))))
    pointer = 0
    acc = 0
    audit_log = set()
    current_instruction_changed = None

  instruction = program[pointer][0]
  argument = int(program[pointer][1])

  print('{} {}'.format(instruction.upper(), argument))
  audit_log.add(pointer)

  if not current_instruction_changed and pointer not in instruction_changed and (instruction == 'nop' or  instruction == 'jmp'):
    print('CHANGE')
    current_instruction_changed = pointer
    instruction_changed.add(pointer)
    instruction = 'jmp' if instruction == 'nop' else 'nop'

  if instruction == 'nop':
    pointer += 1
  elif instruction == 'acc':
    acc += argument
    pointer += 1
  elif instruction == 'jmp':
    pointer += argument

print(acc)