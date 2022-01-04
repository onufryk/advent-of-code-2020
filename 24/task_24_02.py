from copy import copy, deepcopy


class Tile:
    def __init__(self):
        self.position = None
        self.color = "white"
        self.east = None
        self.southeast = None
        self.southwest = None
        self.west = None
        self.northwest = None
        self.northeast = None

    def __str__(self):
        return '{} {} Tile {}'.format(self.position, self.color, id(self))

    def __repr__(self):
        return '{} {} Tile {}'.format(self.position, self.color, id(self))

    def has_neighbour(self, direction):
        if direction == "e":
            return self.east is not None
        if direction == "w":
            return self.west is not None
        if direction == "se":
            return self.southeast is not None
        if direction == "sw":
            return self.southwest is not None
        if direction == "nw":
            return self.northwest is not None
        if direction == "ne":
            return self.northeast is not None

    def neighbour(self, direction):
        if direction == "e":
            return self.east
        if direction == "w":
            return self.west
        if direction == "se":
            return self.southeast
        if direction == "sw":
            return self.southwest
        if direction == "nw":
            return self.northwest
        if direction == "ne":
            return self.northeast

    def flip(self):
        self.color = "white" if self.color == "black" else "black"


class Solution:
    def __init__(self):
        self.root = Tile()
        self.root.position = (0, 0)
        self.tiles = {self.root.position: self.root}
        self.instructions = []

        self.min_row = 0
        self.max_row = 0
        self.min_col = 0
        self.max_col = 0

    def read_data(self):
        with open("input.txt", "r") as input_file:
            for input_line in input_file:
                input_line = input_line.strip()
                path = []
                i = 0
                while i < len(input_line):
                    direction = input_line[i]
                    if direction == "s" or direction == "n":
                        direction = direction + input_line[i+1]
                        i += 1
                    i += 1
                    path.append(direction)
                self.instructions.append(path)

    def process_path(self, path):
        # print(path)
        current_tile = self.root
        for direction in path:
            # print()
            # print("Go {} from {}".format(direction.upper(), current_tile))
            if current_tile.has_neighbour(direction):
                # print("Has neighbour")
                current_tile = current_tile.neighbour(direction)
                # print("Existing tile {}".format(current_tile))
            else:
                # print("No neighbour")
                current_tile = self.add_neighbour(current_tile, direction)
                # print("New tile {}".format(current_tile))
        # print(self.tiles)
        # print(current_tile)
        current_tile.flip()

    def add_neighbour(self, tile, direction):
        new_tile = Tile()

        if direction == "e":
            new_tile.position = (tile.position[0], tile.position[1] + 2)
        if direction == "w":
            new_tile.position = (tile.position[0], tile.position[1] - 2)
        if direction == "se":
            new_tile.position = (tile.position[0] + 1, tile.position[1] + 1)
        if direction == "sw":
            new_tile.position = (tile.position[0] + 1, tile.position[1] - 1)
        if direction == "nw":
            new_tile.position = (tile.position[0] - 1, tile.position[1] - 1)
        if direction == "ne":
            new_tile.position = (tile.position[0] - 1, tile.position[1] + 1)

        if new_tile.position in self.tiles:
            raise Exception("Position {} is already populated.".format(new_tile.position))

        # process all neighbours of new tile position and update links
        # E
        pos = new_tile.position[0], new_tile.position[1] + 2
        if pos in self.tiles:
            new_tile.east = self.tiles[pos]
            self.tiles[pos].west = new_tile
        # W
        pos = new_tile.position[0], new_tile.position[1] - 2
        if pos in self.tiles:
            new_tile.west = self.tiles[pos]
            self.tiles[pos].east = new_tile
        # SE
        pos = new_tile.position[0] + 1, new_tile.position[1] + 1
        if pos in self.tiles:
            new_tile.southeast = self.tiles[pos]
            self.tiles[pos].northwest = new_tile
        # SW
        pos = new_tile.position[0] + 1, new_tile.position[1] - 1
        if pos in self.tiles:
            new_tile.southwest = self.tiles[pos]
            self.tiles[pos].northeast = new_tile
        # NE
        pos = new_tile.position[0] - 1, new_tile.position[1] + 1
        if pos in self.tiles:
            new_tile.northeast = self.tiles[pos]
            self.tiles[pos].southwest = new_tile
        # NW
        pos = new_tile.position[0] - 1, new_tile.position[1] - 1
        if pos in self.tiles:
            new_tile.northwest = self.tiles[pos]
            self.tiles[pos].southeast = new_tile

        self.tiles[new_tile.position] = new_tile

        if new_tile.position[0] < self.min_row:
            self.min_row = new_tile.position[0]

        if new_tile.position[0] > self.max_row:
            self.max_row = new_tile.position[0]

        if new_tile.position[1] < self.min_col:
            self.min_col = new_tile.position[1]

        if new_tile.position[1] > self.max_col:
            self.max_col = new_tile.position[1]

        return new_tile

    def black_tiles(self):
        return sum(tile.color == "black" for pos, tile in self.tiles.items())

    def neighbours(self, tile):
        adjacent = []
        # E
        pos = tile.position[0], tile.position[1] + 2
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])
        # W
        pos = tile.position[0], tile.position[1] - 2
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])
        # SE
        pos = tile.position[0] + 1, tile.position[1] + 1
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])
        # SW
        pos = tile.position[0] + 1, tile.position[1] - 1
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])
        # NE
        pos = tile.position[0] - 1, tile.position[1] + 1
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])
        # NW
        pos = tile.position[0] - 1, tile.position[1] - 1
        if pos in self.tiles:
            adjacent.append(self.tiles[pos])

        return adjacent

    def move(self):
        check_tiles = set()
        black_tiles = [tile for pos, tile in self.tiles.items() if tile.color == "black"]
        for tile in black_tiles:
            check_tiles.add(tile.position)
            for neighbour in self.neighbours(tile):
                check_tiles.add(neighbour.position)

        new_tiles = {}
        for pos in check_tiles:
            num_blacks = sum(tile.color == "black" for tile in self.neighbours(self.tiles[pos]))

            # print(tile, num_blacks)
            if self.tiles[pos].color == "black" and (num_blacks == 0 or num_blacks > 2):
                new_tiles[self.tiles[pos].position] = copy(self.tiles[pos])
                new_tiles[self.tiles[pos].position].color = "white"
            elif self.tiles[pos].color == "white" and num_blacks == 2:
                new_tiles[self.tiles[pos].position] = copy(self.tiles[pos])
                new_tiles[self.tiles[pos].position].color = "black"
            else:
                new_tiles[self.tiles[pos].position] = copy(self.tiles[pos])
        self.tiles = new_tiles

    def print_floor(self):
        for row in range(self.min_row, self.max_row + 1):
            for col in range(self.min_col, self.max_col + 1):
                if (row, col) in self.tiles:
                    if row == 0 and col == 0:
                        print("w" if self.tiles[(row, col)].color == "white" else "b", end="")
                    else:
                        print("W" if self.tiles[(row, col)].color == "white" else "B", end="")
                else:
                    print(" ", end="")
            print()

    def run(self):
        self.read_data()
        for instructions in self.instructions:
            self.process_path(instructions)

        # print(self.min_row, self.max_row)
        # print(self.min_col, self.max_col)

        self.print_floor()
        print("Black {} tiles.".format(self.black_tiles()))

        move_id = 0

        while move_id < 100:
            move_id += 1

            self.move()

            self.print_floor()

            print("Day {}: {}".format(move_id, self.black_tiles()))

        print(len(self.tiles.keys()))




solution = Solution()
solution.run()
