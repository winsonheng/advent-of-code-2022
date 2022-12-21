target_cycles = [20 + 40 * i for i in range(6)]
target_id = 0
cycle = 0
signal = 1
sum_signal = 0

with open("10.in") as file:
    for line in file:
        cycle += 1
        line = line.rstrip()

        if target_id < len(target_cycles) and cycle == target_cycles[target_id]:
            sum_signal += cycle * signal
            target_id += 1

        if line == "noop":
            continue
        else:
            cycle += 1
            if target_id < len(target_cycles) and cycle == target_cycles[target_id]:
                sum_signal += cycle * signal
                target_id += 1
            signal += int(line.removeprefix("addx "))
        

print(sum_signal)