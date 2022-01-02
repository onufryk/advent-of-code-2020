import sys


def solve_game(cups, full_len, num_moves):

    # prep list
    cuplist = {}
    for i in range(full_len):
        if i < len(cups) - 1:
            cuplist[cups[i]] = cups[i + 1]
        elif i == len(cups) - 1 and len(cups) == full_len:
            cuplist[cups[i]] = cups[0]
        elif i == len(cups) - 1 and len(cups) < full_len:
            cuplist[cups[i]] = max(cups) + 1
        elif i < full_len - 1:
            cuplist[i + 1] = i + 2
        elif i == full_len - 1:
            cuplist[i + 1] = cups[0]

    ptr = cups[0]
    for _ in range(num_moves):

        # remove three cups
        c1 = cuplist[ptr]
        c2 = cuplist[c1]
        c3 = cuplist[c2]
        cuplist[ptr] = cuplist[c3]

        # find dest
        dest = ((ptr - 2) % full_len) + 1
        while dest in [c1, c2, c3]:
            dest = ((dest - 2) % full_len) + 1

        # reinsert cups after dest
        cuplist[c3] = cuplist[dest]
        cuplist[dest] = c1

        # move ptr forward
        ptr = cuplist[ptr]

    return cuplist


cups = [int(v) for v in "219347865"]

solved = solve_game(cups, len(cups), 100)
res = ""
x = solved[1]
while x != 1:
    res += str(x)
    x = solved[x]
print(f"Part 1: {res}")

solved = solve_game(cups, 1000000, 10000000)
res = solved[1] * solved[solved[1]]
print(f"Part 2: {res}")
