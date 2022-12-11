from utils import load_input
from dataclasses import dataclass
from collections import deque
from functools import reduce
from typing import Callable
import heapq
import sys

sys.set_int_max_str_digits(1000000)

@dataclass
class Monkey:
    items: deque
    op: Callable
    test: int
    if_true: int
    if_false: int
    inpected: int = 0

mod = 1

def update_mod(monkeys: list[Monkey]) -> None:
    global mod
    for monkey in monkeys:
        mod *= monkey.test

def parse_monkeys(input: list[str]) -> list[list[str]]:
    monkeys = []
    monkey = []

    for line in input:
        if line != "":
            monkey.append(line.strip())
        else:
            monkeys.append(monkey)
            monkey = []

    monkeys.append(monkey)

    return monkeys

def create_monkey(input: list[str]) -> Monkey:
    _, items_str, op_str, test_str, if_true_str, if_false_str = input

    items = items_str.split(":")[1].split(",")
    test = int(test_str.split(" ")[-1])
    if_true = int(if_true_str.split(" ")[-1])
    if_false = int(if_false_str.split(" ")[-1])
    op = op_str.split("=")[1]
    nop = lambda old,op=op: eval(op)

    return Monkey(deque(map(int, items)), nop, test, if_true, if_false)

def compute_worry_1(op: Callable, item: int) -> int:
    return op(item) // 3

def compute_worry_2(op: Callable, item: int) -> int:
    worry = op(item)
    worry %= mod
    return worry

def round(monkeys: list[Monkey], compute_worry: Callable[[Callable, int], int]) -> None:
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.popleft()
            monkey.inpected += 1
            worry_level = compute_worry(monkey.op, item)
            test = monkey.test
            if_true = monkey.if_true
            next_monkey_id = monkey.if_false
            if worry_level % test == 0:
                next_monkey_id = if_true
            # print(f"item={item}, worry_level={worry_level}, next_monkey={next_monkey_id}")
            monkeys[next_monkey_id].items.append(worry_level)

def most_active_monkeys(monkeys: list[Monkey], k: int) -> list[tuple[int,int]]:
    active = []
    for idx,monkey in enumerate(monkeys):
        n_items = monkey.inpected
        heapq.heappush(active, (n_items, idx))
        if len(active) > k:
            heapq.heappop(active)

    return active

def print_monkeys(monkeys: list[Monkey]) -> None:
    for monkey in monkeys:
        print(monkey)


def day11p1(monkeys: list[Monkey], n_rounds: int)-> int:
    for _ in range(n_rounds):
        round(monkeys, compute_worry_1)

    most_active = most_active_monkeys(monkeys, 2)
    return reduce(lambda x,y: x*y, map(lambda x: x[0], most_active))

def day11p2(monkeys: list[Monkey], n_rounds: int)-> int:
    for _ in range(n_rounds):
        round(monkeys, compute_worry_2)

    most_active = most_active_monkeys(monkeys, 2)
    return reduce(lambda x,y: x*y, map(lambda x: x[0], most_active))

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
    print(f"n_monkeys={len(monkeys_raw)}")

    print("--- Test 1 ---")
    monkeys = list(map(create_monkey, monkeys_raw))
    ans = day11p1(monkeys, 20)
    print_monkeys(monkeys)
    print(ans)

    print("--- Test 2 ---")
    monkeys = list(map(create_monkey, monkeys_raw))
    update_mod(monkeys)
    ans = day11p2(monkeys, 10000)
    print_monkeys(monkeys)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input11.txt")
    monkeys_raw = parse_monkeys(input_raw)
    monkeys = list(map(create_monkey, monkeys_raw))
    ans = day11p1(monkeys, 20)
    print_monkeys(monkeys)
    print(ans)

    print("--- Part 2 ---")
    monkeys_raw = parse_monkeys(input_raw)
    monkeys = list(map(create_monkey, monkeys_raw))
    update_mod(monkeys)
    ans = day11p2(monkeys, 10000)
    print_monkeys(monkeys)
    print(ans)
