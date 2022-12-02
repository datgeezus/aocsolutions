from utils import load_input

POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
}

MAP = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

WINS = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

WINS2 = {
    "A": "C",
    "B": "A",
    "C": "B"
}

LOSES = {
    "C": "A",
    "A": "B",
    "B": "C"
}

DRAWS = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

LOSS = 0
DRAW = 3
WIN = 6

# Part 2
GUIDE = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN
}


def rps(input: list[list[str]]) -> int:
    ans = []

    for opp, you in input:
        point = POINTS[MAP[you]]
        result = WIN
        if WINS[opp] == you:
            result = LOSS
        elif DRAWS[opp] == you:
            result = DRAW
        # print(f"total={point+result}")
        ans.append(point + result)
        

    return sum(ans)

def rps2(input: list[list[str]]) -> int:
    ans = []

    for opp,you in input:
        print(f"opp={opp}, you:{you}")
        result = GUIDE[you]
        point = POINTS[opp]
        if result == LOSS:
            point = POINTS[WINS2[opp]]
        elif result == DRAW:
            point = POINTS[opp]
        else:
            point = POINTS[LOSES[opp]]
        total = point + result
        # print(f"point={point}, result={result}, total={total}")
        ans.append(total)


    return sum(ans)

if __name__ == "__main__":
    test_input = [
        ["A","Y"],
        ["B","X"],
        ["C","Z"],
    ]

    score = rps(test_input)
    print(score)

    input_string = load_input.load("./inputs/input2.txt")
    input = list(map(lambda s: s.split(" "), input_string))
    score = rps(input)
    print(score)

    # Part 2
    print("--- Part 2 ---")
    score = rps2(test_input)
    print(score)

    score = rps2(input)
    print(score)
