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
            remainder = 2020 - number
            for number2 in self.numbers:
                if number == number2:
                    continue
                if remainder - number2 in self.numbers:
                    return number * number2 * (remainder - number2)

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
