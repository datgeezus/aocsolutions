import math
from utils import load_input

Coord = tuple[int,int]

def get_coords(steps: list[tuple[str,int]]) -> list[Coord]:
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
        # x += n * dx
        # y += n * dy
        for _ in range(n):
            x += dx
            y += dy
            visited.append((x,y))

    return visited

def get_diffs(coords: list[Coord]) -> list[int]:
    diffs = []
    curr = coords[0]
    for coord in coords[1:]:
        dist = math.dist(curr, coord)
        if dist > 1:
            diffs.append(dist-1)
            curr = coord

    return diffs

def day9p1(steps: list[tuple[str,int]]) -> int:
    coords = get_coords(steps)
    # print(f"coords={coords}")
    diffs = get_diffs(coords)
    # print(f"diffs={diffs}, sum={sum(diffs)}")
    return math.ceil(sum(diffs)) + 2



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

    input = list(map(parse, test_input))
    ans = day9p1(input)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input9.txt")
    input = list(map(parse, input_raw))
    ans = day9p1(input)
    print(ans)
