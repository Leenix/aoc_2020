def load_input(input_file):
    output = []
    with open(input_file) as f:
        for line in f.readlines():
            row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
            seat = int(line[7:].strip('\n').replace('R', '1').replace('L', '0'), 2)
            output.append((row, seat))
    return output


def get_missing_seats(input_data):
    seats = set(range(35, 886))
    for seat in input_data:
        id = seat[0] * 8 + seat[1]
        seats.remove(id)
    return seats


if __name__ == '__main__':
    data = load_input("input.txt")
    highest_id = 0
    for entry in data:
        id = entry[0]*8 + entry[1]
        if id > highest_id:
            highest_id = id
    print(f'Highest ID: {highest_id}')

    remaining_sets = get_missing_seats(data)
    print(remaining_sets)
