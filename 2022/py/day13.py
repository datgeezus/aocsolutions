from utils import load_input

def gen_input(input: list[str]):
    n = len(input)
    for idx in range(0, n, 3):
        yield (input[idx], input[idx+1])

def compare(left: list[int], right: list[int]) -> bool:
    print(f"left={left}, right={right}, same size={len(left) == len(right)}")

    n_left = len(left)
    n_right = len(right)
    # if n_left > n_right:
    #     return False

    for i in range(n_left):
        if (i > n_right-1):
            return False
            
        l_val = left[i]
        r_val = right[i]
        l_type = type(l_val)
        r_type = type(r_val)
        if l_type == int and r_type == int:
            if l_val == r_val:
                continue
            else:
                return l_val < r_val
        else:
            new_left: list[int] = l_val if l_type == list else [l_val]
            new_right: list[int] = r_val if r_type == list else [r_val]
            return compare(new_left, new_right)

    return True

def day13p1(input: list[str]):
    ans = []
    for idx,pair in enumerate(gen_input(input), start=1):
        l = eval(pair[0])
        r = eval(pair[1])
        left = l if type(l) == list else [l]
        right = r if type(r) == list else [r]
        if compare(left, right):
            ans.append(idx)

    return ans


if __name__ == "__main__":
    test_input = [
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
    ]

    print("--- Test 1 ---")
    ans = day13p1(test_input)
    print(f"ans={ans}, sum={sum(ans)}")

    # print("--- Part 1 ---")
    # input_raw = load_input.load("./inputs/input13.txt")
    # ans = day13p1(input_raw)
    # print(f"ans={ans}, sum={sum(ans)}")
