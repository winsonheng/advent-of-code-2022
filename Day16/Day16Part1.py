# {"XX: {"rate": int, "to": ["YY", "ZZ"]}, ... }
tunnels = {}
target_valves = set()
shortest_path = {}
MAX_WEIGHT = 999

with open("16.in") as file:
    for line in file:
        inputs = line.rstrip().replace("Valve ", "").replace(" has flow rate=", ", ")\
            .replace("; tunnels lead to valves ", ", ").replace("; tunnel leads to valve ", ", ").split(", ")
        valve, rate = inputs[0:2]
        leads_to = inputs[2:]
        tunnels[valve] = {"rate": int(rate), "to": leads_to}
        if int(rate) > 0:
            target_valves.add(valve)

        shortest_path[valve] = {next: 1 for next in leads_to}


# Initialise all paths to max
for i in shortest_path:
    for j in shortest_path:
        if j not in shortest_path[i]:
            shortest_path[i][j] = MAX_WEIGHT

# Compute APSP
for k in shortest_path:
    for i in shortest_path:
        for j in shortest_path:
            shortest_path[i][j] = min(shortest_path[i][j], shortest_path[i][k] + shortest_path[k][j])

# Include 1 minute to open the valve
for i in shortest_path:
    for j in shortest_path:
        shortest_path[i][j] += 1


def best_move(curr, mins_left, opened):
    # Moving to another valve and opening it takes >= 2 mins so no need do anything if not enough time
    if mins_left <= 2:
        return 0

    sssp = shortest_path[curr]
    best = 0

    for next in target_valves:
        if next not in opened and mins_left > sssp[next]:
            next_opened = opened.copy()
            next_opened.add(next)
            best = max(best, tunnels[next]["rate"] * (mins_left - sssp[next]) + best_move(next, mins_left - sssp[next], next_opened))

    return best


print(best_move("AA", 30, set()))