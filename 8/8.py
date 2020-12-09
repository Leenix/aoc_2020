from copy import deepcopy

pc = 0
accumulator = 0


def nop(arg):
    global pc
    pc += 1


def acc(arg):
    global pc, accumulator
    accumulator += int(arg)
    pc += 1


def jmp(arg):
    global pc
    pc += int(arg)


global instructions
instructions = {'nop': nop, 'acc': acc, 'jmp': jmp}


def load_input(input_file):
    output = []
    with open(input_file) as f:
        for line in f.readlines():
            output.append(line.split(' '))
    return output


def run_until_loop(instruction_list):
    visited_steps = set()
    while pc not in visited_steps:
        visited_steps.add(pc)
        line = instruction_list[pc]
        instruction = line[0]
        argument = line[1]
        instructions[instruction](argument)
    print(accumulator)


def program_is_infinite(instruction_list):
    global pc
    pc = 0

    global accumulator
    accumulator = 0

    visited_steps = set()

    while pc not in visited_steps and pc < len(instruction_list):
        visited_steps.add(pc)
        line = instruction_list[pc]
        instruction = line[0]
        argument = line[1]
        instructions[instruction](argument)

    return pc in visited_steps


def swap_instruction(instruction_num, instruction_list):
    instruction = instruction_list[instruction_num][0]
    new_instruction = None

    if instruction == 'nop':
        new_instruction = 'jmp'

    if instruction == 'jmp':
        new_instruction = 'nop'

    if new_instruction is not None:
        instruction_list[instruction_num][0] = new_instruction

    return new_instruction is not None


if __name__ == '__main__':
    program = load_input('input.txt')

    if program_is_infinite(program):
        print(accumulator)

    for i in range(len(program)):
        new_instruction_list = deepcopy(program)
        if swap_instruction(i, new_instruction_list):
            if not program_is_infinite(new_instruction_list):
                print(accumulator)


