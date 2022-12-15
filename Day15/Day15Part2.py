with open("15.in") as file:
    # 0: sensor_x, 1: sensor_y, 2: beacon_x, 3: beacon_y
    lines = [list(map(lambda x: int(x), 
                    line.rstrip().replace("Sensor at x=", "").replace(": closest beacon is at x=", ", y=").split(", y="))) 
                for line in file]

for TARGET_Y in range(4000001):
    intervals = []
    for line in lines:
        dist = abs(line[2] - line[0]) + abs(line[3] - line[1])
        delta_x = dist - abs(TARGET_Y - line[1])
        
        if delta_x < 0:
            # Target y row too far away
            continue
        
        # Merging intervals
        interval = [max([0, line[0] - delta_x]), min([4000000, line[0] + delta_x])]
        to_remove = []
        to_add = True
        for i in intervals:
            if interval[0] >= i[0]:
                if interval[1] <= i[1]:
                    # Interval already fully contained
                    to_add = False
                    break
                elif interval[0] <= i[1] + 1:
                    interval[0] = i[0]
                    to_remove.append(i)
            elif interval[1] >= i[0] - 1:
                interval[1] = max([interval[1], i[1]])
                to_remove.append(i)
        for i in to_remove:
            intervals.remove(i)
        if to_add:
            intervals.append(interval)

    if len(intervals) == 2 and min(intervals[0][1], intervals[1][1]) < 4000000:
        print(min(intervals[0][1], intervals[1][1]) + 1)
        break
    elif intervals[0][1] == 1:
        print(0)
        break
    elif intervals[0][1] == 3999999:
        print(4000000)
        break

for TARGET_X in range(4000001):
    intervals = []
    for line in lines:
        dist = abs(line[2] - line[0]) + abs(line[3] - line[1])
        delta_y = dist - abs(TARGET_X - line[0])
        
        if delta_y < 0:
            # Target x row too far away
            continue
        
        # Merging intervals
        interval = [max([0, line[1] - delta_y]), min([4000000, line[1] + delta_y])]
        to_remove = []
        to_add = True
        for i in intervals:
            if interval[0] >= i[0]:
                if interval[1] <= i[1]:
                    # Interval already fully contained
                    to_add = False
                    break
                elif interval[0] <= i[1] + 1:
                    interval[0] = i[0]
                    to_remove.append(i)
            elif interval[1] >= i[0] - 1:
                interval[1] = max([interval[1], i[1]])
                to_remove.append(i)
        for i in to_remove:
            intervals.remove(i)
        if to_add:
            intervals.append(interval)
            
    if len(intervals) == 2 and min(intervals[0][1], intervals[1][1]) < 4000000:
        print(min(intervals[0][1], intervals[1][1]) + 1)
    elif intervals[0][1] == 1:
        print(0)
        break
    elif intervals[0][1] == 3999999:
        print(4000000)
        break

