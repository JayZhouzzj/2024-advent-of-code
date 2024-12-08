import os


def create_files(x):
    if os.path.exists(f"day{x}.py"):
        overwrite = input(
            f"File day{x}.py already exists. Do you want to overwrite it? (y/n): "
        )
        if overwrite.lower() != "y":
            print(f"Skipping creation of day{x}.py.")
            return
    with open(f"day{x}.py", "w") as py_file:
        py_file.write("def solve():\n")
        py_file.write("    pass\n")
        py_file.write("\n")
        py_file.write("if __name__ == '__main__':\n")
        py_file.write("    solve()\n")
    with open(f"day{x}.in", "w") as in_file:
        pass
    with open(f"day{x}.sample.in", "w") as sample_in_file:
        pass

    print(f"Files day{x}.py, day{x}.in, and day{x}.sample.in have been created.")


if __name__ == "__main__":
    x = int(input("Enter the number for the day: "))
    create_files(x)
