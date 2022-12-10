from utils import load_input

Instruction = tuple[str,int]

def simulate_cpu(instructions: list[Instruction]) -> list[int]:
    x = 1
    cpu = [x]

    for cmd, val in instructions:
        cpu.append(x)
        if cmd == "addx":
            x += val
            cpu.append(x)

    return cpu

def print_crt(crt: list[str], width: int, height: int) -> None:
    i = 0
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(crt[i])
            i += 1
        print("".join(row))

def simulate_crt(cpu: list[int], width: int, height: int) -> list[str]:
    crt = ["." for _ in range(width * height)]
    for cycle,pos in enumerate(cpu):
        x = cycle % width
        if pos-1 <= x and x <= pos+1:
            crt[cycle] = "#"

    return crt

def day10p1(instructions: list[Instruction]) -> int:
    cycles = [20, 60, 100, 140, 180, 220]
    cpu = simulate_cpu(instructions)
    strenghts = [cycle * cpu[cycle-1] for cycle in cycles]
    return sum(strenghts)

def day10p2(instructions: list[Instruction]) -> None:
    WIDTH = 40
    HEIGHT = 6
    cpu = simulate_cpu(instructions)
    crt = simulate_crt(cpu, WIDTH, HEIGHT)
    print_crt(crt, WIDTH, HEIGHT)

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

    print("--- Test 2 ---")
    ans = day10p2(input)
    print(f"ans={ans}")

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input10.txt")
    input = list(map(parse, input_raw))
    ans = day10p1(input)
    print(f"ans={ans}")

    print("--- Part 2 ---")
    ans = day10p2(input)
    """
    ####..##..###...##....##.####...##.####.
    ...#.#..#.#..#.#..#....#.#.......#....#.
    ..#..#....###..#..#....#.###.....#...#..
    .#...#....#..#.####....#.#.......#..#...
    #....#..#.#..#.#..#.#..#.#....#..#.#....
    ####..##..###..#..#..##..#.....##..####.
    """
