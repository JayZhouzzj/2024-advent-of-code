import sys
from collections import defaultdict, deque


def is_valid_order(update, ordering_rules):
    # Create a map of page index positions in the update for quick lookup
    page_index = {page: idx for idx, page in enumerate(update)}

    # Check if all ordering rules are respected
    for X, Y in ordering_rules:
        if X in page_index and Y in page_index:
            # X should come before Y
            if page_index[X] > page_index[Y]:
                return False
    return True


def get_middle_page_number(update):
    # The middle page number in the list of pages
    return update[len(update) // 2]


def topological_sort(pages, ordering_rules):
    # Create a graph from the ordering rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Initialize graph for all pages
    for page in pages:
        in_degree[page] = 0

    # Build the graph from the ordering rules
    for X, Y in ordering_rules:
        if X in pages and Y in pages:
            graph[X].append(Y)
            in_degree[Y] += 1

    # Topological sort using Kahn's algorithm
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []

    while queue:
        current_page = queue.popleft()
        sorted_pages.append(current_page)

        for neighbor in graph[current_page]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_pages) != len(pages):
        raise ValueError("There is a cycle, the update cannot be sorted correctly.")

    return sorted_pages


def process_input(input_data):
    # Split input into two sections
    ordering_rules = []
    updates = []
    section = 0  # 0 for rules, 1 for updates

    for line in input_data.splitlines():
        if line.strip() == "":
            section = 1
            continue

        if section == 0:
            # Parse the ordering rules (X|Y)
            X, Y = line.split("|")
            ordering_rules.append((int(X), int(Y)))
        else:
            # Parse the updates
            updates.append([int(x) for x in line.split(",")])

    return ordering_rules, updates


def main(input_data):
    # Process the input data
    ordering_rules, updates = process_input(input_data)

    # Initialize the total sum of middle page numbers for incorrectly ordered updates
    total_sum = 0

    for update in updates:
        if not is_valid_order(update, ordering_rules):
            # If the update is not in the correct order, sort it
            sorted_update = topological_sort(update, ordering_rules)
            # Get the middle page number after sorting
            middle_page = get_middle_page_number(sorted_update)
            total_sum += middle_page

    return total_sum


if __name__ == "__main__":
    print(main(sys.stdin.read().strip()))
