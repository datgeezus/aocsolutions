from utils import load_input

def parse(inp: str) -> tuple[set[str],set[str]]:
    n = len(inp) // 2
    return (set(inp[:n]), set(inp[n:]))

def build_priority() -> dict[str,int]:
    p = {}
    start = ord('a')
    end = ord('z') + 1
    for c in range(start, end):
        key = chr(c)
        p[key] = ord(key) - start + 1

    start = ord('A')
    end = ord('Z') + 1
    for c in range(start, end):
        key = chr(c)
        p[key] = ord(key) - start + 27

    return p

def prio(input: list[tuple[set[str], set[str]]], priority: dict[str,int]) -> int:
    ans = 0
    for pockets in input:
        common = pockets[0].intersection(pockets[1])
        # print(f"common={common}")
        ans += priority[common.pop()]

    return ans

def grouped_prio(input: list[str], priority: dict[str, int]) -> int:
    ans = 0
    n = len(input)
    for i in range(0, n, 3):
        items1 = set(input[i])
        items2 = set(input[i+1])
        items3 = set(input[i+2])
        common = items1.intersection(items2, items3)
        ans += priority[common.pop()]

    return ans

def test(name:str, expected, actual) -> None:
    print(f"Test: {name}, with value={actual}")
    assert expected == actual, f"FAILURE: expected={expected}, actual={actual}"
    print(f"PASSED\n")

if __name__ == "__main__":
    test_input = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    test_input_parsed = list(map(parse, test_input))
    # print(test_input_parsed)

    priority = build_priority()
    # print(f"priority={priority}")

    ans = prio(test_input_parsed, priority)
    print(ans)


    input_string = load_input.load("./inputs/input3.txt")
    input = list(map(parse, input_string))
    ans = prio(input, priority)
    print(ans)

    print(f"--- Part 2 ---")
    ans = grouped_prio(test_input, priority)
    test("Day 3 Test", 70, ans)

    ans = grouped_prio(input_string, priority)
    test("Day 3 Prod", 2817, ans)
