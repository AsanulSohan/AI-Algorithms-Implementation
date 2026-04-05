def dfs_limited(tree, node, limit, visited, goal):
    # If node is None or already visited in this run
    if node in visited:
        return False

    visited.append(node)  # mark visited

    print(node, end=" ")   # traversal print

    # 🎯 GOAL CHECK (STOP immediately)
    if node == goal:
        return True

    # Depth limit reached → stop expanding
    if limit == 0:
        return False

    # Expand children
    for neighbor in tree.get(node, []):
        found = dfs_limited(tree, neighbor, limit - 1, visited, goal)
        if found:   # if goal found in subtree → stop everything
            return True

    return False


def iterative_deepening(tree, start, goal, max_limit):
    for i in range(max_limit):
        print(f"\nIteration {i + 1} (limit = {i + 1}): ", end="")

        visited = []  # fresh visited list every iteration

        found = dfs_limited(tree, start, i + 1, visited, goal)

        print()  # new line after each iteration

        if found:
            print(f"\n Goal '{goal}' found at depth {i + 1}")
            return

    print(f"\n❌ Goal '{goal}' not found within limit {max_limit}")


if __name__ == "__main__":
    # Example tree
    tree = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H', 'I'],
        'E': [],
        'F': [],
        'G': [],
        'H': [],
        'I': []
    }

    start_node = 'A'
    goal_node = 'H'
    max_depth = 4

    iterative_deepening(tree, start_node, goal_node, max_depth)