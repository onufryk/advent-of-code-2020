import pprint
import re

raw_lines = None
with open('input.txt', 'r') as data:
  raw_lines = [line.rstrip() for line in data.readlines()]

raw_rules = []
messages = []

i = 0
while i < len(raw_lines) and raw_lines[i] != '':
  raw_rules.append(raw_lines[i])
  i += 1

i += 1
while  i < len(raw_lines) and i < len(raw_lines):
  messages.append(raw_lines[i])
  i += 1

rules = [None] * len(raw_rules)

for raw_rule in raw_rules:
  index, ruledef = raw_rule.split(':')
  disjunction_rules = ruledef.split('|')

  if len(disjunction_rules) > 1:
    rules[int(index)] = {
      'operator': 'OR',
      'arguments':  [[rule.strip(' "') if '"' in rule else int(rule) for rule in disjunction_rule.strip().split(' ')] for disjunction_rule in disjunction_rules]
    }
  else:
    tokens = disjunction_rules[0].strip().split(' ')
    if len(tokens) > 1:
      rules[int(index)] = [rule.strip(' "') if '"' in rule else int(rule) for rule in tokens]
    else:
      rules[int(index)] = tokens[0].strip(' "')

print('{:-^100}'.format(' RULES '))
for i, r in enumerate(rules):
  print('{}: {}'.format(i, r))
print('{:-^100}'.format(''))

def compile_pattern(rule):
  if isinstance(rule, dict):
    if rule['operator'] == 'OR':
      new_rule = []
      for subrule in rule['arguments']:
        new_rule.append('({})'.format(compile_pattern(subrule)))
      return '({})'.format('|'.join(new_rule))
  elif isinstance(rule, list):
    new_rule = []
    for subrule_index in rule:
      new_rule.append(compile_pattern(rules[subrule_index]))
    return ''.join(new_rule)
  elif rule.isnumeric():
    return compile_pattern(rules[int(rule)])
  else:
    return rule


pattern_string = '^' + compile_pattern(rules[0]) + '$'
print(pattern_string)

count = 0
print('{:-^100}'.format(' MESSAGES '))
pattern = re.compile(pattern_string)
for i, r in enumerate(messages):
  match = pattern.match(r)
  print('{}: {} {}'.format(i, r, match))
  if match is not None:
    count += 1
print('{:-^100}'.format(''))

print(count)
