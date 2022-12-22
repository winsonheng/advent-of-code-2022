monkeys = []

with open("11.in") as file:
    for line in file:
        line = line.rstrip().lstrip()
        if line == "":
            continue
        elif line.startswith("Monkey"):
            monkey = {}
        elif line.startswith("Starting"):
            items = list(map(lambda x: int(x), line.removeprefix("Starting items: ").split(", ")))
            monkey["items"] = items
        elif line.startswith("Operation"):
            ops = line.removeprefix("Operation: new = ").split(" ")
            monkey["ops"] = ops
        elif line.startswith("Test"):
            test = int(line.removeprefix("Test: divisible by "))
            monkey["test"] = test
        elif line.startswith("If true"):
            if_true = int(line.split("monkey ")[1])
            monkey[True] = if_true
        else:
            if_false = int(line.split("monkey ")[1])
            monkey[False] = if_false
            monkeys.append(monkey)
     

monkey_score = [0 for m in monkeys]

for round in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        num_items = len(monkey["items"])
        ops = monkey["ops"]
        for item in monkey["items"]:
            monkey_score[i] += 1
            worry = 0
            op1 = item if ops[0] == "old" else int(ops[0])
            op2 = item if ops[2] == "old" else int(ops[2])
            if ops[1] == "+":
                worry = op1 + op2
            else:
                worry = op1 * op2
            worry = int(worry / 3)
            monkeys[monkey[worry % monkey["test"] == 0]]["items"].append(worry)
        monkey["items"] = monkey["items"][num_items:]


monkey_score.sort(reverse=True)
print(monkey_score[0] * monkey_score[1])
