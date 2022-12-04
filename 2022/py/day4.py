from utils import load_input
from typing import Callable

Comparator = Callable[[tuple[int,int], tuple[int,int]], bool]

def parse(inp: str) -> list[tuple[int,int]]:
    pairs = inp.split(",")
    ans = []
    for pair in pairs:
        rng = pair.split("-")
        ans.append((int(rng[0]), int(rng[1])))
    return ans

def is_contained(this: tuple[int,int], that: tuple[int,int]) -> bool:
    return this[0] <= that[0] and that[1] <= this[1]

def overlaps(this: tuple[int,int], that: tuple[int,int]) -> bool:
    return (this[0] <= that[0] and that[0] <= this[1]
        or this[0] <= that[1] and that[1] <= this[1])


def ans1(input: list[list[tuple[int,int]]], compare: Comparator) -> int:
    ans = 0

    for pair in input:
        contained = compare(pair[0], pair[1]) or compare(pair[1], pair[0])
        ans += 1 if contained else 0

    return ans

if __name__ == "__main__":
    test_input = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]

    test_input_parsed = list(map(parse, test_input))
    print(test_input_parsed)

    print("--- Test ---")
    ans = ans1(test_input_parsed, is_contained)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input4.txt")
    input = list(map(parse, input_raw))
    ans = ans1(input, is_contained)
    print(ans)

    print("--- Part 2 ---")
    input_raw = load_input.load("./inputs/input4.txt")
    input = list(map(parse, input_raw))
    ans = ans1(input, overlaps)
    print(ans)
