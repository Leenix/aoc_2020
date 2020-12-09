from typing import List


class Password:
    def __init__(self, min_count, max_count, criterion, password):
        self.min = min_count
        self.max = max_count
        self.criterion = criterion
        self.password = password

    def is_valid(self):
        count = 0
        is_valid = False

        for letter in self.password:
            if letter == self.criterion:
                count += 1
        if self.min <= count <= self.max:
            is_valid = True
        return is_valid

    def is_valid_position(self):
        count = 0

        if self.password[self.min - 1] == self.criterion:
            count += 1
        if self.password[self.max - 1] == self.criterion:
            count += 1
        return count == 1


def load_input(input_file):
    output: List[Password] = []
    with open(input_file) as f:
        for line in f.readlines():
            bits = line.split(" ")
            password = bits[-1]
            criterion = bits[1].strip(":")
            min_count = int(bits[0].split("-")[0])
            max_count = int(bits[0].split("-")[-1])
            output.append(Password(min_count, max_count, criterion, password))
    return output


if __name__ == '__main__':
    num_valid = 0
    num_valid_2 = 0
    data = load_input("input.txt")
    for entry in data:
        if entry.is_valid():
            num_valid += 1
        if entry.is_valid_position():
            num_valid_2 += 1
    print(f'1: {num_valid} valid passwords (out of {len(data)})')
    print(f'2: {num_valid_2} valid passwords (out of {len(data)})')

