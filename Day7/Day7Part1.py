tree = {"size": 0, "dirs": {}, "files": {}}
ptr = tree
ptr_stack = []
dir_stack = []

with open("7.in") as file:
    for line in file:
        line = line.rstrip()

        if line.startswith("$"):
            if line.startswith("$ cd"):
                line = line.removeprefix("$ cd ")
                if line == "..":
                    ptr_stack.pop()
                    ptr = ptr_stack[-1]
                    dir_stack.pop()
                else:
                    if line not in ptr["dirs"]:
                        ptr["dirs"][line] = {"size": 0, "dirs": {}, "files": {}}
                    ptr = ptr["dirs"][line]
                    ptr_stack.append(ptr)
                    dir_stack.append(line)

        elif line.startswith("dir"):
            line = line.removeprefix("dir ")
            if line not in ptr["dirs"]:
                ptr["dirs"][line] = {"size": 0, "dirs": {}, "files": {}}
        else: # file
            size, name = line.split(" ")
            size = int(size)
            ptr["files"][name] = size
            for dir in ptr_stack:
                dir["size"] += size


def compute_sum(dir, sum):
    if dir["size"] <= 100000:
        sum += dir["size"]
    for nested_dir in dir["dirs"].values():
        sum = compute_sum(nested_dir, sum)
    return sum


print(compute_sum(tree, 0))


