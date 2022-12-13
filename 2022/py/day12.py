from utils import load_input
from collections import deque
from typing import Callable
from dataclasses import dataclass

Point = tuple[int,int]

@dataclass
class Context:
    point: Point = (-1,-1)
    steps: int = -1

def in_bounds(point: Point, curr: Point, grid: list[str], visited: set[Point]) -> bool:
    n_rows = len(grid)
    n_cols = len(grid[0])
    r,c = point

    return (
        point not in visited
        and r >= 0
        and r < n_rows
        and c >= 0
        and c < n_cols
    )

def constraint(next_: Point, curr: Point, grid: list[str]) -> bool:
    nelev = ord(grid[next_[0]][next_[1]])
    celev = ord(grid[curr[0]][curr[1]])
    return celev <= (nelev - 1) or nelev <= celev

def bfs(grid: list[str], start: Point, end: str, on_test: Callable, on_end: Callable, ctx: Context) -> None:
    MOVES = [(1,0), (-1,0), (0,1), (0,-1)]
    # MOVES = [(0,1)]
    visited = set()
    q:deque[Point] = deque()
    q.append(start)
    steps = 0

    while q:
        curr = q.popleft()
        steps += 1
        elev = grid[curr[0]][curr[1]]
        visited.add(curr)
        if  elev == end:
            on_end(curr, steps, ctx)
            return 
        for move in MOVES:
            next_ = (curr[0] + move[0], curr[1] + move[1])
            if in_bounds(next_, curr, grid, visited) and on_test(next_, curr, grid):
                # nelev = grid[next_[0]][next_[1]]
                # if nelev == end:
                #     on_end(next_, steps, ctx)
                #     print(visited)
                #     return 
                q.append(next_)

def bfs2(grid: list[str], start: Point, end: str, on_test: Callable, on_end: Callable, ctx: Context) -> None:
    MOVES = [(1,0), (-1,0), (0,1), (0,-1)]
    # MOVES = [(0,1)]
    visited = set()
    distance = [ [-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q:deque[Point] = deque()
    q.append(start)
    steps = 0
    distance[start[0]][start[1]] = 1

    while q:
        curr = q.popleft()
        dist = distance[curr[0]][curr[1]]
        elev = grid[curr[0]][curr[1]]
        visited.add(curr)
        if  elev == end:
            on_end(curr, dist, ctx)
            return 
        for move in MOVES:
            next_ = (curr[0] + move[0], curr[1] + move[1])
            if in_bounds(next_, curr, grid, visited) and on_test(next_, curr, grid):
                distance[next_[0]][next_[1]] = dist + 1
                # nelev = grid[next_[0]][next_[1]]
                # if nelev == end:
                #     on_end(next_, steps, ctx)
                #     print(visited)
                #     return 
                q.append(next_)

def find_elev(point: Point, steps: int, ctx: Context) -> None:
    print(f"Found {point}")
    ctx.point = point
    ctx.steps = steps

def day12p1(grid: list[str]) -> None:

    start_context = Context()
    bfs(grid, (0,0), "S", lambda x,y,z: True, find_elev, start_context)
    start = start_context.point
    
    end_context = Context()
    bfs2(grid, start, "E", constraint, find_elev, end_context)
    r,c = end_context.point
    print(f"Found {grid[r][c]} at = {(r,c)}, with {end_context.steps} steps")



if __name__ == "__main__":
    test_input = [
        "Sabqponm",
        "abcryxxl",
        "accszExk",
        "acctuvwj",
        "abdefghi",
    ]

    print("--- Test 1 ---")
    day12p1(test_input)

    input_raw = load_input.load("./inputs/input12.txt")
    print("--- Part 1 ---")
    day12p1(input_raw)
