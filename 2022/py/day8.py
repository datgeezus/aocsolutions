from utils import load_input

VisitSet = set[tuple[int,int]]
Move = tuple[int,int]

def day8p1(trees: list[list[int]]) -> set[tuple[int,int]]:
    ROWS = len(trees)
    COLS = len(trees[0])
    MOVES = [(0,1),(1,0),(0,-1),(-1,0)]
    east = set()
    west = set()
    north = set()
    south = set()

    def is_valid(r: int, c: int, visited: VisitSet, prev_h: int) -> bool:
        return (
            (r,c) not in visited
            and r >= 0
            and r < ROWS
            and c >= 0
            and c < COLS
            and prev_h < trees[r][c]
        )

    def dfs(r: int, c: int, visited: VisitSet, prev_h: int, move: Move) -> None:
        if not is_valid(r, c, visited, prev_h):
            return

        visited.add((r,c))
        height = trees[r][c]
        new_r = move[0] + r
        new_c = move[1] + c
        # print(f"({r},{c}) = {height}")
        dfs(new_r, new_c, visited, height, move)

    for c in range(COLS):
        dfs(0, c, north, -1, MOVES[1])
        dfs(ROWS-1, c, south, -1, MOVES[3])
    
    for r in range(ROWS):
        dfs(r, 0, west, -1, MOVES[0])
        dfs(r, COLS-1, east, -1, MOVES[2])
    
    # print(f"north={north}")
    # print(f"south={south}")
    # print(f"east={east}")
    # print(f"west={west}")

    return east.union(west, north, south)


def to_number(input: str) -> list[int]:
    return [int(x) for x in input]

if __name__ == "__main__":
    test_input = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
    ]

    input = list(map(to_number, test_input))

    print("--- Test ---")
    ans = day8p1(input)
    print(ans)
    print(len(ans))

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input8.txt")
    input = list(map(to_number, input_raw))
    ans = day8p1(input)
    print(len(ans))
