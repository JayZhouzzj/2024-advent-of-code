import bisect
import re
import sys


def extract_mul_instructions(corrupted_string):
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    # Use re.finditer to get match objects and their starting indices
    matches_with_indices = [
        (match.group(0), match.start())
        for match in re.finditer(pattern, corrupted_string)
    ]

    # Extract the actual numbers from the matches
    mul_matches = [
        (
            int(match[0].split(",")[0].strip("mul(")),
            int(match[0].split(",")[1].strip(")")),
        )
        for match in matches_with_indices
    ]

    # Return both the mul matches (as tuples of numbers) and their starting indices
    return mul_matches, [match[1] for match in matches_with_indices]


def find_instruction_indices(instruction):
    # Regular expressions to match 'do()' and 'don't()'
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Find all do() matches with their start indices
    do_matches = [match.start() for match in re.finditer(do_pattern, instruction)]

    # Find all don't() matches with their start indices
    dont_matches = [match.start() for match in re.finditer(dont_pattern, instruction)]
    return do_matches, dont_matches


def find_largest_y(b, x):
    # Use bisect_right to find the insertion point for x
    pos = bisect.bisect_right(b, x)

    # Check if pos > 0, meaning there is at least one element <= x
    if pos > 0:
        return b[pos - 1]  # The largest element <= x
    return None  # No element in b is <= x


def process_instructions(instruction):
    enabled = True
    dos, donts = find_instruction_indices(instruction)
    matches = extract_mul_instructions(instruction)

    res = 0
    for (a, b), idx in zip(matches[0], matches[1]):
        do = find_largest_y(dos, idx)
        dont = find_largest_y(donts, idx)
        if do is None and dont is None:
            enabled = True
        elif do is None or (dont is not None and dont > do):
            enabled = False
        else:
            enabled = True
        if enabled:
            res += a * b

    return res


def solve(expr):
    return sum(x * y for x, y in extract_mul_instructions(expr))


if __name__ == "__main__":
    print(process_instructions(sys.stdin.read().strip()))
