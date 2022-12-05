from utils import load_input
from math import ceil

def parse_stacks(input: list[str]) -> list[list[str]]:
    step = ceil(len(input[0]) / 3)
    print(f"step={step}")

    def build_stack(input: str) -> list[str]:
        return [input[i] for i in range(1, len(input), 4)]

    stacks = list(map(build_stack, input))
    # print(f"stacks={stacks}")
    n_stacks = len(stacks[0])
    print(f"n stacks={n_stacks}")

    stack_height = len(stacks) - 2

    crates = [[] for _ in range(n_stacks)]
    # print(f"crates={crates}")
    
    for i in range(n_stacks):
        for r in range(stack_height, -1, -1):
            crate = stacks[r][i]
            if crate != " ":
                crates[i].append(crate)

    return crates

def parse_moves(move: str) -> tuple[int,int,int]:
    m = move.split(" ")
    return (int(m[1]), int(m[3])-1, int(m[5])-1)

def parse(input: list[str]) -> tuple[list[str],list[str]]:
    split = input.index("")
    return (input[0:split], input[split+1:])


def day5(stacks: list[list[str]], moves: list[tuple[int,int,int]]) -> list[str]:
    for n,frm,to in moves:
        for _ in range(n):
            # print(f"from={frm}, to={to}")
            stacks[to].append(stacks[frm].pop())

    return [s[-1] for s in stacks]

if __name__ == "__main__":
    test_input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        "",
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    print("--- Test ---")
    stacks,moves = parse(test_input)
    print(f"stacks={stacks}, moves={moves}")

    moves_parsed = list(map(parse_moves, moves))
    print(f"moves={moves_parsed}")

    stacks_parsed = parse_stacks(stacks)
    print(f"stacks={stacks_parsed}")

    ans = day5(stacks_parsed, moves_parsed)
    print(f"stacks={stacks_parsed}")
    print(f"ans={''.join(ans)}")

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input5.txt")
    stacks,moves = parse(input_raw)

    moves_parsed = list(map(parse_moves, moves))
    # print(f"moves={moves_parsed}")

    stacks_parsed = parse_stacks(stacks)
    # print(f"stacks={stacks_parsed}")
    ans = day5(stacks_parsed, moves_parsed)
    print(f"stacks={stacks_parsed}")
    print(f"ans={''.join(ans)}")
