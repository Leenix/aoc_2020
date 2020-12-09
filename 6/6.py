from functools import reduce


def load_input(input_file):
    output = []
    with open(input_file) as f:
        output = f.read().split('\n\n')
    return output


def get_any_count(data):
    output = []
    for group in data:
        output.append(len(reduce(set.union, map(set, group.split()))))
    return output

def get_all_count(data):
    output = []
    for group in data:
        output.append(len(reduce(set.intersection, map(set, group.split()))))
    return output

if __name__ == '__main__':
    data = load_input("input.txt")
    print(data)
    print(sum(get_any_count(data)), get_any_count(data))
    print(sum(get_all_count(data)), get_all_count(data))

