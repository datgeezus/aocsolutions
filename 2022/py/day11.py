from dataclasses import dataclass
from collections import deque
import heapq

@dataclass
class Monkey:
    items: deque
    op: tuple[str, str, str]
    test: int
    if_true: int
    if_false: int

def parse_monkeys(input: list[str]) -> list[list[str]]:
    monkeys = []
    monkey = []

    for line in input:
        if line != "":
            monkey.append(line.strip())
        else:
            monkeys.append(monkey)
            monkey = []

    return monkeys

def create_monkey(input: list[str]) -> Monkey:
    _, items_str, op_str, test_str, if_true_str, if_false_str = input

    items = items_str.split(":")[1].split(",")
    op = tuple(op_str.split("=")[1].strip().split(" "))
    test = int(test_str.split(" ")[-1])
    if_true = int(if_true_str.split(" ")[-1])
    if_false = int(if_false_str.split(" ")[-1])

    return Monkey(deque(map(int, items)), op, test, if_true, if_false)

def parse_op(op: tuple[str,str,str], item: int) -> int:
    return 1

def round(monkeys: list[Monkey]) -> None:
    for monkey in monkeys:
        item = monkey.items.popleft()
        op = monkey.op
        worry_level = parse_op(op, item) // 3
        test = monkey.test
        if_true = monkey.if_true
        next_monkey_id = monkey.if_false
        if worry_level % test == 0:
            next_monkey_id = if_true
        monkeys[next_monkey_id].items.append(item)

def most_active_monkeys(monkeys: list[Monkey], k: int) -> list[tuple[int,int]]:
    active = []
    for idx,monkey in enumerate(monkeys):
        n_items = len(monkey.items)
        heapq.heappush(active, (n_items, idx))
        if len(active) > k:
            heapq.heappop(active)

    return active


def day11p1(monkeys: list[Monkey]) -> int:
    ans = 0
    n_rounds = 1
    for _ in range(n_rounds):
        round(monkeys)

    most_active = most_active_monkeys(monkeys, 2)

    return sum(map(lambda x: x[0], most_active))

if __name__ == "__main__":
    test_input = [
        "Monkey 0:",
        "  Starting items: 79, 98",
        "  Operation: new = old * 19",
        "  Test: divisible by 23",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 3",
        "",
        "Monkey 1:",
        "  Starting items: 54, 65, 75, 74",
        "  Operation: new = old + 6",
        "  Test: divisible by 19",
        "    If true: throw to monkey 2",
        "    If false: throw to monkey 0",
        "",
        "Monkey 2:",
        "  Starting items: 79, 60, 97",
        "  Operation: new = old * old",
        "  Test: divisible by 13",
        "    If true: throw to monkey 1",
        "    If false: throw to monkey 3",
        "",
        "Monkey 3:",
        "  Starting items: 74",
        "  Operation: new = old + 3",
        "  Test: divisible by 17",
        "    If true: throw to monkey 0",
        "    If false: throw to monkey 1",
    ]

    monkeys_raw = parse_monkeys(test_input)
    monkeys = list(map(create_monkey, monkeys_raw))
    ans = day11p1(monkeys)
    print(ans)
