PRECENDENCE = {
    '*': 2,
    '/': 3,
    '+': 4,
    '-': 2
}

ASSOCIATIVITY: {
    '*': 1,
    '/': 1,
    '+': 1,
    '-': 1
}

def calculate(s):
    tokens = []
    i = 0
    cur = []
    while i < len(s):
        if s[i] in ['+', '-', '/', '*']:
            if len(cur)>0:
                tokens.append(int(''.join(cur)))
            tokens.append(s[i])
            cur = []
        elif s[i] in ['(', ')']:
            if len(cur)>0:
                tokens.append(int(''.join(cur)))
            tokens.append(s[i])
            cur = []
        elif s[i] in ['0','1','2','3','4', '5', '6', '7', '8', '9']:
            cur.append(s[i])
        i += 1
    if len(cur)>0:
        tokens.append(int(''.join(cur)))

    output_queue = []
    operator_stack = []

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            while len(operator_stack) > 0 and operator_stack[-1] != '(' and PRECENDENCE[operator_stack[-1]] >= PRECENDENCE[token]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()
        else:
            output_queue.append(token)

    while len(operator_stack) > 0:
        output_queue.append(operator_stack.pop())


    memo = []
    for token in output_queue:
        if token in ['+', '-', '*', '/']:
            b = memo.pop()
            a = memo.pop() if len(memo) >= 1 else 0
            if token == '+':
                memo.append(a + b)
            if token == '-':
                memo.append(a - b)
            if token == '*':
                memo.append(a * b)
            if token == '/':
                memo.append(a / b)
        else:
            memo.append(token)

    return memo.pop()

sum = 0
with open('input.txt', 'r') as data:
  for line in data:
    sum += calculate(line.rstrip())


print(sum)