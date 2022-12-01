from utils import load_input
from collections import defaultdict
import heapq

def parse(s: str) -> int:
    return int(s) if s != "" else -1

def count_calories(input: list[int]) -> int:
    count = 0
    max_count = 0
    for s in input:
        if s < 0:
            max_count = max(max_count, count)
            count = 0
        else:
            count += s

    return max_count


def count_calories_top(input: list[int], k:int) -> int:
    count = 0
    # ans = []
    # max_count = 0
    heap = []
    for s in input:
        if s < 0:
            # max_count = max(max_count, count)
            heapq.heappush(heap, count)
            if len(heap) > k:
                heapq.heappop(heap)
            count = 0
        else:
            count += s

    return sum(heap)


if __name__ == "__main__":
    test_input = [
        1000,
        2000,
        3000,
        -1,
        4000,
        -1,
        5000,
        6000,
        -1,
        7000,
        8000,
        9000,
        -1,
        10000,
    ]
    input_string = load_input.load("./inputs/input1.txt")
    input = list(map(parse, input_string))

    ans = count_calories(test_input)
    print(ans)

    ans = count_calories(input)
    print(ans)

    ans = count_calories_top(input, 3)
    print(ans)

    
