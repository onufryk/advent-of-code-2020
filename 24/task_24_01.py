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

        return new_tile

    def run(self):
        self.read_data()
        for instructions in self.instructions:
            self.process_path(instructions)

        # for pos, tile in self.tiles.items():
        #     print(tile)

        print(sum(tile.color == "black" for pos, tile in self.tiles.items()))


solution = Solution()
solution.run()
