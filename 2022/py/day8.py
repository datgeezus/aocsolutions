from utils import load_input

VisitSet = set[tuple[int,int]]
Move = tuple[int,int]

def day8p1(trees: list[list[int]]) -> set[tuple[int,int]]:
    COLS = len(trees)
    ROWS = len(trees[0])
    MOVES = [(0,1),(1,0),(0,-1),(-1,0)]
    visible = set()

    def is_valid(r: int, c: int, visited: VisitSet, prev_h: int) -> bool:
        return (
            (r,c) not in visited
            and r >= 0
            and r < ROWS
            and c >= 0
            and c < COLS
            and prev_h <= trees[r][c]
        )

    def dfs(r: int, c: int, visited: VisitSet, prev_h: int, move: Move) -> None:
        if not is_valid(r, c, visited, prev_h):
            return

        if prev_h < trees[r][c]:
            visited.add((r,c))

        height = trees[r][c]
        new_r = move[0] + r
        new_c = move[1] + c
        dfs(new_r, new_c, visited, height, move)

    def traverse_r(r: int, rng, visited: VisitSet) -> None:
        h = -1
        for c in rng:
            height = trees[r][c]
            if height < h:
                # print(f"breaking because ch={height}, h={h}")
                return
            if height > h:
                visited.add((r,c))
            h = height
        # print(visited)
            
    def traverse_c(c: int, rng: range, visited: VisitSet) -> None:
        h = -1
        for r in rng:
            height = trees[r][c]
            if height < h:
                # print(f"breaking because ch={height}, h={h}")
                return
            if height > h:
                visited.add((r,c))
            h = height
        # print(visited)

    east = range(COLS-1, -1, -1)
    west = range(0, COLS, 1)
    north = range(0, ROWS, 1)
    south = range(ROWS-1, -1, -1)

    for c in range(COLS):
        dfs(0, c, visible, -1, MOVES[1])
        dfs(ROWS-1, c, visible, -1, MOVES[3])
        # traverse_r(c, east, visible)
        # traverse_r(c, west, visible)
    
    for r in range(ROWS):
        dfs(r, 0, visible, -1, MOVES[0])
        dfs(r, COLS-1, visible, -1, MOVES[2])
        # traverse_c(r, north, visible)
        # traverse_c(r, south, visible)
    
    # print(f"visible={visible}, n={len(visible)}")
    # visible_trees = [[trees[r][c] if (r,c) in visible else -1
    #     for r in range(ROWS)]
    #     for c in range(COLS)
    # ]
    # pprint_forest(visible_trees)

    return visible

def pprint_forest(forest: list[list[int]]) -> None:
    n_rows = len(forest)
    n_cols = len(forest[0])

    for r in range(n_rows):
        print("\n")
        for c in range(n_cols):
            print(f"[{forest[r][c]}]")


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
