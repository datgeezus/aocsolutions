import math
from utils import load_input

Coord = tuple[int,int]

def get_head_coords(steps: list[tuple[str,int]]) -> list[Coord]:
    x = 0
    y = 0
    moves = {
        "L":(-1,0),
        "R":(1,0),
        "U":(0,1),
        "D":(0,-1)
    }

    visited = []
    visited.append((x,y))
    for cmd,n in steps:
        dx,dy = moves[cmd]
        for _ in range(n):
            x += dx
            y += dy
            visited.append((x,y))

    return visited

def get_tail_coords(coords: list[Coord], min_dist: float, n_knots) -> list[Coord]:
    tail = []
    curr = coords[0]

    tail.append(curr)
    for i,coord in enumerate(coords[1:], start=1):
        dist = math.dist(curr, coord)
        if dist > min_dist:
            for k in range(n_knots, 0, -1):
                curr = coords[i-k]
                tail.append(curr)

    return tail

def day9p1(steps: list[tuple[str,int]]) -> int:
    min_dist = math.dist((0,0),(1,1))
    head = get_head_coords(steps)
    tail = get_tail_coords(head, min_dist, 1)
    return len(set(tail))

def day9p2(steps: list[tuple[str,int]]) -> int:
    min_dist = math.dist((0,0),(9,9))
    head = get_head_coords(steps)
    tail = get_tail_coords(head, min_dist, 9)
    return len(set(tail))


def parse(inp: str) -> tuple[str,int]:
    cmd = inp.split(" ")
    return (cmd[0], int(cmd[1]))

if __name__ == "__main__":
    test_input = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2"
    ]

    print("--- Test 1 ---")
    input = list(map(parse, test_input))
    ans = day9p1(input)
    print(ans)

    print("--- Test 2 ---")
    test_input_2 = [
        "R 5",
        "U 8",
        "L 8",
        "D 3",
        "R 17",
        "D 10",
        "L 25",
        "U 20"
    ]
    input = list(map(parse, test_input_2))
    ans = day9p2(input)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input9.txt")
    input = list(map(parse, input_raw))
    ans = day9p1(input)
    print(ans)

    print("--- Part 2 ---")
    input_raw = load_input.load("./inputs/input9.txt")
    input = list(map(parse, input_raw))
    ans = day9p2(input)
    print(ans)
