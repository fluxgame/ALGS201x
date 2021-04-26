# python3

import argparse

class Node:
    def __init__(self, val):
        self.children = []
        self.val = val


def compute_height(parents):
    nodes = [Node(i) for i in range(len(parents))]
    root = None

    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])

    max_height = 1
    this_level = [root]
    next_level = []
    curr = root
    
    while this_level:
        node = this_level.pop(0)
        if node.children:
            if not next_level:
                max_height += 1
            next_level += node.children
        if not this_level:
            this_level = next_level
            next_level = []

    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(parents))


def test():
    samples = [([4, -1, 4, 1, 1], 3), ([-1, 0, 4, 0, 3], 4), ([9, 7, 5, 5, 2, 9, 9, 9, 2, -1], 4)]
    for parents, expected in samples:
        result = compute_height(parents)
        if result == expected:
            print("passed")
        else:
            print(f"FAILED: expected: {expected}, got: {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="run unit tests", action="store_true")
    args = parser.parse_args()

    if args.test:
        test()
    else:
        main()

