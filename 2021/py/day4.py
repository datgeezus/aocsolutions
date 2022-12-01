"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so
deep that you can't see any sunlight. What you can see, however, is a giant squid that
has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
Numbers are chosen at random, and the chosen number is marked on all boards on which it appears.
(Numbers may not appear on all boards.)
If all numbers in any row or any column of a board are marked, that board wins.
(Diagonals don't count.)

The submarine has a bingo subsystem to help passengers
(currently, you and the giant squid) pass the time.
It automatically generates a random order in which to draw numbers and a random set of
boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners,
but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column
of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated.
Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188.
Then, multiply that sum by the number that was just called when the board won, 24,
to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first.
What will your final score be if you choose that board?
"""
import logging as log
from utils import args, load_input
from dataclasses import dataclass
from collections import deque, defaultdict
from typing import Callable

@dataclass(frozen=True)
class Result:
    found: bool
    cell: tuple[int, int]

@dataclass(frozen=True)
class Winner:
    board_number: int
    value: int

def gen_numbers(input: list[str]) -> list[int]:
    return list(map(int, input[0]))

def get_board(input: list[str]):
    n = len(input)
    j = 0
    while n > 0:
        if input[j] == '':
            print(j)
            j += 1
            n -= 1
            continue
        yield [list(input[i].split()) for i in range(j,j+5,1)]
        n -= 5
        j += 5

def gen_boards(input: list[str]) -> dict[int,list[list[str]]]:
    boards = {i:board for i,board in enumerate(get_board(input))}
    return boards

def value_to_loc(board: list[list[str]]) -> dict[str, tuple[int, int]]:
    return {v:(x,y) 
        for x,row in enumerate(board)
        for y,v in enumerate(row)
    }

def value_to_board(boards: dict[int, list[list[str]]]) -> dict[int, list[int]]:
    ans = defaultdict(list)

    for i,board in boards.items():
        for row in board:
            for value in row:
                ans[int(value)].append(i)

    return ans

def in_bounds(point: tuple[int,int], max_x: int = 0, max_y: int = 0) -> bool:
    return (point[0] >= 0 and point[0] < max_x if max_x > 0 
        else point[1] >= 0 and point[1] < max_y)

def bfs(board: list[list[str]], start: tuple[int,int]) -> bool:
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    deltas = (1,-1)
    c_found = 1
    r_found = 1
    max_x = len(board)
    max_y = len(board[0])
    is_free: Callable[[tuple[int,int]], bool] = lambda x: x not in visited
    is_set: Callable[[tuple[int,int]], bool] = lambda x: board[x[0]][x[1]] == 'x'
    is_valid: Callable[[tuple[int,int]], bool] = lambda x: is_set(x) and is_free(x)
    while q:
        col,row = q.pop() # (x,y)
        for delta in deltas:
            col_new = col + delta
            if in_bounds((col_new,row), max_x=max_x) and is_valid((col_new, row)):
                log.debug(f"col curr:{(col_new,row)}")
                c_found += 1
                q.append((col_new, row))
                visited.add((col_new,row))
    q = deque()
    q.append(start)
    while q:
        col,row = q.pop() # (x,y)
        for delta in deltas:
            row_new = row + delta
            if in_bounds((col,row_new), max_y=max_y) and is_valid((col, row_new)):
                log.debug(f"row curr:{(col,row_new)}")
                r_found += 1
                q.append((col, row_new))
                visited.add((col,row_new))

    log.debug(f"c_found:{c_found}, r_fonud:{r_found}")
    return c_found == max_x or r_found == max_y

def is_winner(board: list[list[str]], point: tuple[int,int]) -> bool:
    board[point[0]][point[1]] = "x"
    return bfs(board, point)

def play_bingo(numbers: list[int], boards: dict[int, list[list[str]]]) -> list[Winner]:

    value_to_board_index = value_to_board(boards)
    log.debug(f"value to board: {value_to_board_index}")

    locs = {i: value_to_loc(board) for i,board in boards.items()}

    # winners = [None for _ in range(len(boards))]
    winners = []
    won = set()

    for num in numbers:
        log.debug(f"n:{num}")
        board_indexes = value_to_board_index.get(num, [])
        log.debug(f"board_indexes:{board_indexes}")
        for board_i in board_indexes:
            if board_i not in won:
                loc = locs[board_i][str(num)]
                log.debug(f"board[{board_i}] location:{loc}")
                winner = is_winner(boards[board_i], loc)
                if winner:
                    won.add(board_i)
                    winners.append(Winner(board_i, num))

    return winners

def prettyprint_board(board: list[list[str]]) -> None:
    for row in board:
        print(row)

def score(board: list[list[str]], num: int) -> int:
    return num * sum(
        [int(val) for row in board for val in row if val != 'x']
    )


if __name__ == "__main__":
    args = args.get_args()
    log.basicConfig(level=args.log_level)

    test_input = [
        "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
        "",
        "22 13 17 11  0",
        " 8  2 23  4 24",
        "21  9 14 16  7",
        " 6 10  3 18  5",
        " 1 12 20 15 19",
        "",
        " 3 15  0  2 22",
        " 9 18 13 17  5",
        "19  8  7 25 23",
        "20 11 10 24  4",
        "14 21 16 12  6",
        "",
        "14 21 17 24  4",
        "10 16 15  9 19",
        "18  8 23 26 20",
        "22 11 13  6  5",
        " 2  0 12  3  7",
    ]


    gen = lambda x: list(map(int, x[0].split(',')))

    log.debug(f"numbers:{test_input[0]}")
    numbers = gen(test_input)
    log.debug(f"numbers:{numbers}")

    boards = gen_boards(test_input[1::])
    log.debug(f"board 0: {boards[0]}")
    log.debug(f"board 1: {boards[1]}")
    log.debug(f"board 2: {boards[2]}")

    # test_board = [
    #     ["22","13","17","11","0"],
    #     ["8" ,"2" ,"23", "4","24"],
    #     ["x","x" ,"x","16","x"],
    #     ["6" ,"10","3" ,"18","5"],
    #     ["1" ,"12","20","15","19"],
    # ]

    # found = is_winner(boards[0], (1,1))
    # log.debug(f"found?:{found}, board 0:{boards[0]} ")
    # found = is_winner(boards[0], (2,4))
    # log.debug(f"found?:{found}, board 0:{boards[0]} ")
    # found = is_winner(test_board, (2,3))
    # log.debug(f"found?:{found}, board 0:{test_board} ")

    winner = play_bingo(numbers, boards)
    if winner:
        first = winner[0]
        last = winner[-1]
        log.debug(f"winner:{winner}")
        log.debug(f"winner: {prettyprint_board(boards[first.board_number])}")
        log.info(f"score:{score(boards[first.board_number], first.value)}")
        assert score(boards[first.board_number], first.value) == 4512
    else:
        log.error(f"NO WINNERS")


    inp = load_input.load("./inputs/input4.txt")
    log.debug(f"numbers:{numbers}")
    numbers = gen(inp)
    log.debug(f"{inp[1:10]}")
    boards = gen_boards(inp[1::])
    log.debug(f"board 0: {boards[0]}")
    winner = play_bingo(numbers, boards)
    if winner:
        first = winner[0]
        last = winner[-1]
        log.debug(f"first winner:{first}")
        log.debug(f"first winner: {prettyprint_board(boards[first.board_number])}")
        log.info(f"first winner score:{score(boards[first.board_number], first.value)}") # 35711
        assert score(boards[first.board_number], first.value) == 35711
        log.debug(f"last winner:{last}")
        log.debug(f"last winner: {prettyprint_board(boards[last.board_number])}")
        log.info(f"last winner score:{score(boards[last.board_number], last.value)}") # 5586
        assert score(boards[last.board_number], last.value) == 5586
    else:
        log.error(f"NO WINNERS")
