with open('input.txt', 'r') as data:
  max_seat_id = 0
  for ticket in data:
    row_min = 0
    row_max = 127
    seat_min = 0
    seat_max = 7
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
      if seat_id > max_seat_id:
        max_seat_id = seat_id
      print(c, row_min, row_max, seat_min, seat_max)

    print(ticket, end='')
    print(row_min, row_max)
    print(seat_min, seat_max)

  print(max_seat_id)

