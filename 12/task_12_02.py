import math
import re

ship_latitude = 0  # N or S
ship_longitude = 0  # E or W

waypoint_latitude = 1
waypoint_longitude = 10

command_pattern = re.compile(r'(\w)(\d+)')

with open('input.txt', 'r') as data:
  for line in data:
    result = command_pattern.search(line.rstrip())
    if not result:
      raise ValueError(line)
    command = result.group(1)
    argument = int(result.group(2))
    print('{} {}'.format(command, argument))
    if command == 'N':
      waypoint_latitude += argument
    elif command == 'S':
      waypoint_latitude -= argument
    elif command == 'E':
      waypoint_longitude += argument
    elif command == 'W':
      waypoint_longitude -= argument
    elif command == 'L':
      print('Ship Long:{}, Lat:{}. Waypoint Long:{}, Lat:{}.'.format(ship_longitude, ship_latitude, waypoint_longitude, waypoint_latitude))
      angle =  -argument % 360
      rel_lat = waypoint_latitude - ship_latitude
      rel_long = waypoint_longitude - ship_longitude

      new_rel_lat = round(rel_lat * math.cos(math.radians(angle)) - rel_long * math.sin(math.radians(angle)))
      new_rel_long = round(rel_long * math.cos(math.radians(angle)) + rel_lat * math.sin(math.radians(angle)))

      print('Relative Long: {}, Lat: {}'.format(rel_long, rel_lat))
      print('New relative Long: {}, Lat: {}'.format(new_rel_long, new_rel_lat))
      waypoint_latitude = ship_latitude + new_rel_lat
      waypoint_longitude = ship_longitude + new_rel_long
    elif command == 'R':
      print('Ship Long:{}, Lat:{}. Waypoint Long:{}, Lat:{}.'.format(ship_longitude, ship_latitude, waypoint_longitude, waypoint_latitude))
      angle =  argument % 360
      rel_lat = waypoint_latitude - ship_latitude
      rel_long = waypoint_longitude - ship_longitude

      new_rel_lat = round(rel_lat * math.cos(math.radians(angle)) - rel_long * math.sin(math.radians(angle)))
      new_rel_long = round(rel_long * math.cos(math.radians(angle)) + rel_lat * math.sin(math.radians(angle)))

      print('Relative Long: {}, Lat: {}'.format(rel_long, rel_lat))
      print('New relative Long: {}, Lat: {}'.format(new_rel_long, new_rel_lat))
      waypoint_latitude = ship_latitude + new_rel_lat
      waypoint_longitude = ship_longitude + new_rel_long
    elif command == 'F':
      print('Ship Long:{}, Lat:{}. Waypoint Long:{}, Lat:{}.'.format(ship_longitude, ship_latitude, waypoint_longitude, waypoint_latitude))
      rel_lat = waypoint_latitude - ship_latitude
      rel_long = waypoint_longitude - ship_longitude
      print('Relative Long: {}, Lat: {}'.format(rel_long, rel_lat))
      ship_latitude += argument * rel_lat
      ship_longitude += argument * rel_long
      waypoint_latitude = ship_latitude + rel_lat
      waypoint_longitude = ship_longitude + rel_long
      print('Ship Long:{}, Lat:{}. Waypoint Long:{}, Lat:{}.'.format(ship_longitude, ship_latitude, waypoint_longitude, waypoint_latitude))
    else:
      raise ValueError(command)
    # if command in ['L', 'R']:
    print('Ship Long:{}, Lat:{}. Waypoint Long:{}, Lat:{}.'.format(ship_longitude, ship_latitude, waypoint_longitude, waypoint_latitude))


print(abs(ship_latitude) + abs(ship_longitude))
