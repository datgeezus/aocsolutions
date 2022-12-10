from utils import load_input

Instruction = tuple[str,int]

def day10p1(instructions: list[Instruction]) -> int:
    clocks = [20, 60, 100, 140, 180, 220]
    x = 1
    cpu = [x]

    for cmd, val in instructions:
        cpu.append(x)
        if cmd == "addx":
            x += val
            cpu.append(x)

    # print(f"cpu={cpu}")
    strenghts = [clock * cpu[clock-1] for clock in clocks]
    # print(f"strenghts={strenghts}")

    return sum(strenghts)

def parse(input: str) -> Instruction:
    inst = input.split(" ")
    return (inst[0], int(inst[1])) if len(inst) > 1 else (inst[0], -1)

if __name__ == "__main__":
    test_input = [
        "noop",
        "addx 3",
        "addx -5",
    ]
    input = list(map(parse, test_input))

    print("--- Test 1 ---")
    input_raw = load_input.load("./inputs/input10test.txt")
    input = list(map(parse, input_raw))
    ans = day10p1(input)
    print(f"ans={ans}")

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input10.txt")
    input = list(map(parse, input_raw))
    ans = day10p1(input)
    print(f"ans={ans}")
