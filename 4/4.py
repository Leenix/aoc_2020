def load_input(input_file):
    output = []
    with open(input_file) as f:
        entries = f.read().split("\n\n")
        for entry in entries:
            obj = {}
            entry = entry.replace('\n', ' ')
            params = entry.split(' ')
            for param in params:
                pairs = param.split(':')
                obj[pairs[0]] = pairs[1]
            output.append(obj)
    return output


def entry_is_valid(entry):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    entry_valid = len(entry.keys()) > 0
    keys = entry.keys()
    for field in required_fields:
        if field not in keys:
            entry_valid = False
    return entry_valid


def entry_is_valid2(entry):
    entry_valid = entry_is_valid(entry)

    if entry_valid:
        entry_valid = entry_valid and 1920 <= int(entry['byr']) <= 2002
        entry_valid = entry_valid and 2010 <= int(entry['iyr']) <= 2020
        entry_valid = entry_valid and 2020 <= int(entry['eyr']) <= 2030
        entry_valid = entry_valid and (entry['hgt'].endswith('cm') or entry['hgt'].endswith('in'))

        if entry_valid and entry['hgt'].endswith('cm'):
            height = entry['hgt'].replace('cm', '')
            entry_valid = entry_valid and 150 <= int(height) <= 193

        if entry_valid and entry['hgt'].endswith('in'):
            height = entry['hgt'].replace('in', '')
            entry_valid = entry_valid and 59 <= int(height) <= 76

        entry_valid = entry_valid and entry['hcl'].startswith('#') and len(entry['hcl']) == 7
        if entry_valid:
            try:
                int(entry['hcl'][1:], 16)
            except ValueError:
                entry_valid = False

        valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        entry_valid = entry_valid and entry['ecl'] in valid_eye_colours

        entry_valid = entry_valid and len(entry['pid']) == 9
        if entry_valid:
            try:
                int(entry['pid'])
            except ValueError:
                entry_valid = False
    return entry_valid


if __name__ == '__main__':
    data = load_input("input.txt")
    num_valid = 0
    for entry in data:
        if entry_is_valid(entry):
            num_valid += 1
    print(f'{num_valid} of {len(data)} entries')

    num_valid_2 = 0
    for entry in data:
        if entry_is_valid2(entry):
            num_valid_2 += 1
    print(f'{num_valid_2} of {len(data)} entries')

