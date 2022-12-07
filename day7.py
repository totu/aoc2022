#!/usr/bin/env python3
def calc_size(dirs, _dir):
    size = dirs[_dir]["size"]
    for sub_dir in dirs[_dir]["sub_dirs"]:
        sub_dir_size = calc_size(dirs, sub_dir)
        size += sub_dir_size
    return size


if __name__ == "__main__":
    # file_name = "day7_test.input"
    file_name = "day7.input"

    dirs = {}
    prompt = []
    with open(file_name, "r") as input_file:
        prompt = input_file.readlines()

    cur_dir = ""
    path = []
    for index, line in enumerate(prompt):
        line = line.strip()
        if line.startswith("$ cd"):
            cur_dir = line.strip().split(" ")[2]
            if cur_dir == "..":
                path = path[:-1]
                if path == []:
                    path = ["/"]
            else:
                path.append(cur_dir)

        elif line.startswith("$ ls"):
            size = 0
            sub_dirs = []
            for thing in prompt[index + 1 :]:
                if thing.startswith("$"):
                    break
                thing = thing.strip().split(" ")
                if thing[0].isnumeric():
                    size += int(thing[0])
                elif thing[0] == "dir":
                    sub_dirs.append(thing[1])
                else:
                    assert False, thing

            full_path = ".".join(path)
            parent = ".".join(path[:-1])
            assert full_path not in dirs, full_path

            if not parent and cur_dir != "/":
                parent = "/"

            dirs[full_path] = {"size": size, "sub_dirs": []}  # sub_dirs}
            if parent:
                dirs[parent]["sub_dirs"].append(full_path)

    total_size = 0
    for _dir in dirs:
        size = calc_size(dirs, _dir)
        if size <= 100_000:
            total_size += size

    print(total_size)
