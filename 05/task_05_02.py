seats = []
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
      seats.append(seat_id)
      if seat_id > max_seat_id:
        max_seat_id = seat_id

  sorted_seats = sorted(seats)
  for i in range(1, len(sorted_seats)):
    if sorted_seats[i] - sorted_seats[i - 1] == 2:
      print(sorted_seats[i - 1], sorted_seats[i])
