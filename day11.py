#!/usr/bin/env python3
import math
import copy


class Monkey:
    def __init__(
        self,
        _id: int,
        items: list[int],
        operation: str,
        test: str,
        if_true: int,
        if_false: int,
    ):
        self.id = _id
        self.items = items
        self.op = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected_items = 0

    def inspect(self, item: int) -> int:
        """Monkey inspects item and returns worry level"""
        self.inspected_items += 1
        return math.floor(
            int(eval(self.op.replace("old", str(item)).replace("new =", ""))) / 3
        )

    def check(self, worry_level: int) -> bool:
        return worry_level % int(self.test.split(" ")[-1]) == 0

    def __repr__(self) -> str:
        return f"Monkey {self.id}: items: {self.items}, inspected {self.inspected_items} items\n"

    def add_item(self, item: int):
        self.items.append(item)


def parse_monkies(file_name: str) -> list[Monkey]:
    monkies: list[Monkey] = []
    with open(file_name, "r") as input_file:
        while True:
            row = input_file.readline()
            if not row.startswith("Monkey"):
                break

            parsed_item_values = eval(input_file.readline().split(":")[1])
            items: list[int] = []
            try:
                items = list(parsed_item_values)
            except TypeError:
                items = [parsed_item_values]

            operation: str = input_file.readline().split("Operation:")[1].strip()
            test: str = input_file.readline().split("Test:")[1].strip()
            if_true: int = int(
                input_file.readline().split("If true:")[1].strip().split(" ")[-1]
            )
            if_false: int = int(
                input_file.readline().split("If false:")[1].strip().split(" ")[-1]
            )
            monkey = Monkey(len(monkies), items, operation, test, if_true, if_false)
            monkies.append(monkey)
            # Read out the line break
            input_file.readline()

    return monkies


if __name__ == "__main__":
    # file_name = "day11_test.input"
    file_name = "day11.input"
    monkies = parse_monkies(file_name)

    rounds = 20
    for _ in range(20):
        for monkey in monkies:
            # print(monkey)
            items = copy.deepcopy(monkey.items)
            monkey.items = []
            for item in items:
                worry_level = monkey.inspect(item)
                check = monkey.check(worry_level)
                if check:
                    new_monkie_id = monkey.if_true
                else:
                    new_monkie_id = monkey.if_false
                monkies[new_monkie_id].add_item(worry_level)

    items_inspected = []
    for monkey in monkies:
        items_inspected.append(monkey.inspected_items)

    items_inspected = sorted(items_inspected, reverse=True)[:2]
    monkey_business_level = items_inspected[0] * items_inspected[1]
    print(monkey_business_level)
