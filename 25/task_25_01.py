with open("input.txt", "r") as input_file:
    input_lines = [int(input_line.strip()) for input_line in input_file.readlines()]

card_pub = input_lines[0]
door_pub = input_lines[1]

e, n = 0, 1
while n != door_pub:
    n = pow(7, e, 20201227)
    e += 1

print(pow(card_pub, e - 1, 20201227))
