
def load_input(input_file):
    output = []
    with open(input_file) as f:
        for line in f.readlines():
            output.append(int(line))
    return output


def find_multiples(input_data):
    a = 0
    b = 0
    for i in range(len(input_data)):
        a = input_data[i]
        check_list = list(input_data[i:])
        for b in check_list:
            if a + b == 2020:
                print(f"{a} + {b} = 2020; {a} * {b} = {a*b}")
                return a, b


def find_triple(input_data):
    for a in set(input_data):
        for b in set(input_data):
            for c in set(input_data):
                if a + b + c == 2020:
                    print(f"{a} + {b} + {c}= 2020; {a} * {b} * {c} = {a * b * c}")
                    return a, b, c


if __name__ == '__main__':
    data = load_input("input.txt")
    find_multiples(data)
    find_triple(data)

