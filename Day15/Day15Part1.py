with open("15.in") as file:
    # 0: sensor_x, 1: sensor_y, 2: beacon_x, 3: beacon_y
    lines = [list(map(lambda x: int(x), 
                    line.rstrip().replace("Sensor at x=", "").replace(": closest beacon is at x=", ", y=").split(", y="))) 
                for line in file]

TARGET_Y = 2000000
beacons = []
beacon_count = 0
intervals = []

for line in lines:
    dist = abs(line[2] - line[0]) + abs(line[3] - line[1])
    delta_x = dist - abs(TARGET_Y - line[1])
    
    if delta_x < 0:
        # Target y row too far away
        continue
    if line[3] == TARGET_Y and line[2] not in beacons:
        # Beacon in target y row
        beacons.append(line[2])
        beacon_count += 1
    
    # Merging intervals
    interval = [line[0] - delta_x, line[0] + delta_x]
    to_remove = []
    for i in intervals:
        if interval[0] >= i[0]:
            if interval[1] <= i[1]:
                # Interval already fully contained
                break
            elif interval[0] <= i[1]:
                interval[0] = i[0]
                to_remove.append(i)
        elif interval[1] >= i[0]:
            interval[1] = max([interval[1], i[1]])
            to_remove.append(i)
    for i in to_remove:
        intervals.remove(i)
    intervals.append(interval)

ans = -beacon_count
for i in intervals:
    ans += i[1] - i[0] + 1

print(ans)
