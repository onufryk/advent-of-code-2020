import collections


class Solution:

    def __init__(self):
        self.passwords = []
        self.policies = []

    def read_input(self):
        input_file = open("input_002_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            tokens = input_line.split(": ")
            policy = tokens[0]
            tokens2 = policy.split(" ")
            quantity = tokens2[0]
            tokens3 = quantity.split("-")
            position1 = int(tokens3[0])
            position2 = int(tokens3[1])
            letter = tokens2[1]
            password = tokens[1]
            self.passwords.append(password)
            self.policies.append((letter, position1, position2))

        input_file.close()

    def is_valid(self, password, policy):
        return (password[policy[1]-1] == policy[0] and password[policy[2]-1] != policy[0]) or (password[policy[1]-1] != policy[0] and password[policy[2]-1] == policy[0])

    def calculate(self):
        valid_count = 0
        for index, password in enumerate(self.passwords):
            if self.is_valid(password, self.policies[index]):
                valid_count += 1
        return valid_count

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
