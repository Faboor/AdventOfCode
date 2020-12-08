import utils


# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
# 
# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# 
# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.
# 
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?


def get_input():
    return utils.get_input_lines(8)


def decode(lines):
    return  [[(parts := line.split(" "))[0], int(parts[1])] for line in lines]


def exec(instructions):
    acc = 0
    pc = 0
    visited = set()
    while pc not in visited and not (finished := pc >= len(instructions)):
        visited.add(pc)
        instr, op = instructions[pc]
        acc += op if instr == "acc" else 0
        pc += op if instr == "jmp" else 1
    return finished, acc


def part1(lines):
    return exec(decode(lines))[1]


# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.
# if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates!
# With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).
# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

def part2(lines):
    instructions = decode(lines)
    for pc, (instr, op) in enumerate(instructions):
        if instr == "acc":
            continue
        instructions[pc][0] = "nop" if instr == "jmp" else "jmp"
        finished, acc = exec(instructions)
        if finished:
            return acc
        instructions[pc][0] = instr


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

