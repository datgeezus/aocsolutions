from utils import load_input

POINTS = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

WINS = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

DRAWS = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

LOSS = 0
DRAW = 3
WIN = 6


def rps(input: list[list[str]]) -> int:
    ans = []

    for opp, you in input:
        point = POINTS[you]
        result = WIN
        if WINS[opp] == you:
            result = LOSS
        elif DRAWS[opp] == you:
            result = DRAW
        # print(f"total={point+result}")
        ans.append(point + result)
        

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
