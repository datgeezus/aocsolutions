from utils import load_input
from collections import defaultdict

def day6(input: str, k:int) -> int:
    left = 0
    seen = defaultdict(int)

    for c in input[:k-1]:
        seen[c] += 1

    for right,_ in enumerate(input[k-1:], start=k-1):
        seen[input[right]] += 1

        # window = right - left + 1
        # print(f"window={window}")
        # print(f"left={left}, right={right}, seen={seen}")
        # print(f"n={len(seen)}, sum={sum(seen.values())}")

        if len(seen) == k and sum(seen.values()) == k:
            return right + 1
        else:
            seen[input[left]] -= 1
            if seen[input[left]] <= 0:
                del seen[input[left]]
            left += 1
    return -1

if __name__ == "__main__":
    test_input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    ans = day6(test_input, 4)
    print(ans)

    test_input = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    ans = day6(test_input, 4)
    print(ans)

    test_input = "nppdvjthqldpwncqszvftbrmjlhg"
    ans = day6(test_input, 4)
    print(ans)

    test_input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    ans = day6(test_input, 4)
    print(ans)

    test_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    ans = day6(test_input, 4)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input6.txt")
    ans = day6(input_raw[0], 4)
    print(ans)

    print("--- Part 2 ---")
    input_raw = load_input.load("./inputs/input6.txt")
    ans = day6(input_raw[0], 14)
    print(ans)
