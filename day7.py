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
    folder_sizes = []
    for _dir in dirs:
        size = calc_size(dirs, _dir)
        folder_sizes.append((size, _dir))
        if size <= 100_000:
            total_size += size
    print(f"part1: {total_size}")

    actual_size_on_disc = calc_size(dirs, "/")
    fs_size = 70000000
    space_needed_for_update = 30000000
    # print(fs_size - actual_size_on_disc < space_needed_for_update)
    space_needed = space_needed_for_update - (fs_size - actual_size_on_disc)
    folder_sizes = [x for x in sorted(folder_sizes) if int(x[0]) >= space_needed]
    print(f"part2: {folder_sizes[0][0]}")
