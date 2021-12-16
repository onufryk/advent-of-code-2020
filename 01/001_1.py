class Solution:

    def __init__(self):
        self.numbers = set()

    def read_input(self):
        input_file = open("input_001_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.numbers.add(int(input_line))

        input_file.close()

    def calculate(self):
        for number in self.numbers:
            if 2020 - number in self.numbers:
                return number * (2020 - number)


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
