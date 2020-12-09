from queue import Queue

def load_input(input_file):
    output = {}
    with open(input_file) as f:
        for line in f.readlines():
            bits = line.split('contain ')
            parent_data = bits[0].split(' ')
            parent = parent_data[0] + parent_data[1]

            children = {}
            if len(bits) > 1 and not bits[1].startswith('no'):
                child_bits = bits[1].split(', ')

                for child in child_bits:
                    child_data = child.split(' ')
                    child = child_data[1] + child_data[2]
                    number = child_data[0]
                    children[child] = number
            output[parent] = children
    return output


def search_children(target, data):
    targets = Queue()
    output = set()
    targets.put(target)

    while not targets.empty():
        current_target = targets.get()
        for parent in data.keys():
            if current_target in data[parent].keys() and current_target not in output:
                targets.put(parent)
        output.add(current_target)
        targets.task_done()
    output.remove(target)
    return output

def find_num_children(parent, data):
    num_children = 0
    for child in data[parent]:
        num_child = int(data[parent][child])
        num_children += num_child + num_child*find_num_children(child, data)
    return num_children


if __name__ == '__main__':
    data = load_input("input.txt")
    output = search_children('shinygold', data)
    print(len(output))

    output2 = find_num_children('shinygold', data)
    print(output2)