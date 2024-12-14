from collections import defaultdict
import sys


def simulate_guard_path(map):
    # Directions mapping: up, right, down, left
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}  # Right turns mapping

    # Find the initial position of the guard and the initial direction
    rows = len(map)
    cols = len(map[0])
    start_pos = None
    start_direction = None

    # Find the initial position and direction
    for r in range(rows):
        for c in range(cols):
            if map[r][c] in directions:
                start_pos = (r, c)
                start_direction = map[r][c]
                break
        if start_pos:
            break

    def check_obstruction(x, y):
        """Simulate guard's movement after placing an obstruction at (x, y)."""
        visited = set()
        cx, cy = start_pos
        direction = start_direction

        while 0 <= cx < rows and 0 <= cy < cols:
            if (cx, cy, direction) in visited:
                return True  # Loop detected
            visited.add((cx, cy, direction))

            # Move in the current direction
            dx, dy = directions[direction]
            nx, ny = cx + dx, cy + dy

            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                return False
            if map[nx][ny] == "#" or (nx, ny) == (x, y):
                # If there's an obstacle or out of bounds, turn right
                direction = turn_right[direction]
            else:
                # Move forward
                cx, cy = nx, ny
        return False

    obstruction_count = 0
    # Try placing an obstruction at every valid position (except the initial guard position)
    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and map[r][c] != "#":
                if check_obstruction(r, c):
                    obstruction_count += 1

    return obstruction_count


if __name__ == "__main__":
    input_map = [list(line.strip()) for line in sys.stdin.readlines()]
    result = simulate_guard_path(input_map)
    print(result)
