seats = []
with open('input.txt', 'r') as data:
  for ticket in data:
    ticket = ticket.strip()
    row_min = 0
    row_max = 127
    seat_min = 0
    seat_max = 7
    seat_id = None
    for c in ticket:
      if c == 'F':
        row_max = row_max - (row_max - row_min) // 2 - 1
      elif c == 'B':
        row_min = row_min + (row_max - row_min) // 2 + 1
      elif c == 'L':
        seat_max = seat_max - (seat_max - seat_min) // 2 - 1
      elif c == 'R':
        seat_min = seat_min + (seat_max - seat_min) // 2 + 1
      seat_id = row_min * 8 + seat_min

    seats.append(seat_id)

seats = sorted(seats)
for i in range(1, len(seats)):
  if seats[i] - seats[i - 1] == 2:
    print(seats[i] - 1)
