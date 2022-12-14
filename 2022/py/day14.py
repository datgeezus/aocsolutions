from functools import reduce

Point = tuple[int,int]

def gen_point(input: str) -> list[Point]:
    # "498,4 -> 498,6 -> 496,6" -> [(498,4), (498,6), (496,6)]
    return [ tuple(map(int, p.split(","))) for p in input.split(" -> ") ]


def line(a: Point, b: Point, offset:int=0) -> list[Point]:
    ax, ay = a
    bx, by = b
    ans = []
    if ax == bx:
        s = min(ay, by)
        e = max(ay, by)
        for i in range(s,e+1):
            ans.append((ax-offset, i))
    else:
        s = min(ax, bx)
        e = max(ax, bx)
        for i in range(s, e+1):
            ans.append((i-offset, ay))

    return ans

def rocks(points: list[Point], offset:int=0) -> list[Point]:
    rock_lines = []
    n = len(points)
    if n == 1:
        x,y = points[0]
        rock_lines.append((x-offset, y))
    else:
        for i in range(1, n):
            rock_lines.extend(line(points[i-1], points[i], offset))

    return rock_lines

def normalize(input: list[str]) -> tuple[Point, list[list[Point]]]:
    min_x = 1000
    max_y = 0
    ans = []

    for line in input:
        points = gen_point(line)
        min_p = min(map(lambda x: x[0], points))
        max_p = max(map(lambda x: x[1], points))
        min_x = min(min_x, min_p)
        max_y = max(max_y, max_p)
        ans.append(points)

    print(f"min={min_x}, max={max_y}")

    return (min_x, max_y), ans


def traverse(rocks: set[Point], start: Point, limit: Point) -> None:
    X, Y = (9,9)
    MOVES = [(0,1), (-1,1), (1,1)]
    path = [
        ["." for _ in range(12)]
        for _ in range(limit[1]+1)
    ]
    for x,y in rocks:
        path[y][x] = "#"

    def is_valid(point: Point) -> bool:
        x,y = point
        # print(point)
        return (
            x >= 0
            and x < X
            and y >= 0
            and y < Y
            and path[y][x] != "o"
            and path[y][x] != "#"
        )

    def dfs(point: Point, prev: Point) -> None:
        nonlocal path
        x,y = point

        if not is_valid(point):
            px,py = prev
            path[py][px] = "o"
            return

        for dx,dy in MOVES:
            x_ = x + dx
            y_ = x + dy
            dfs((x_, y_), (x, y))

    print_path(path)
    sx, sy = start
    dfs((sx-limit[0], sy), (sx-limit[0], sy))
    print_path(path)

def print_path(path: list[list[str]]) -> None:
    for line in path:
        print(line)
    print("~~~~~~~~~~")

def merge(a: list[Point], b: list[Point]) -> list[Point]:
    print(f"a={a}, b={b}")
    return a + b


if __name__ == "__main__":
    test_input = [
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9",
    ]

    (ox, oy),normalized = normalize(test_input)
    print(f"limit={(ox,oy)}, normalized={normalized}")
    rock = set(reduce(merge, map(lambda x: rocks(x, ox-1), normalized)))
    # print(f"rocks={rock}, n={len(rock)}")
    traverse(rock, (500,0), (ox,oy))
