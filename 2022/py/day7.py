from utils import load_input
from dataclasses import dataclass, field

@dataclass
class Node:
    type: str
    name: str
    size: int = 0
    parent: 'Node | None' = None
    children: dict[str,'Node'] = field(default_factory=dict)


def build_tree(input: list[str]) -> Node:
    top = Node("dir", "/")
    root = top
    for line in input[1:]:
        cmd = line.split(" ")
        if cmd[0] == "$": # Command
            if cmd[1] == "cd":
                next_ = cmd[2]
                if next_ == "..":
                    root = root.parent if root else None
                else:
                    root = root.children[next_]
            elif cmd[1] == "ls":
                continue
            else:
                pass
        elif cmd[0] == "dir":
            name = cmd[1]
            if root:
                print(f"Buld dir={name} with parent={root.name}")
                root.children[name] = Node("dir", name, parent=root)
        else: # Output
            size = int(cmd[0])
            name = cmd[1]
            if root:
                root.children[name] = Node("file", name, size, parent=root)
                root.size+= size
                if root.parent:
                    root.parent.size += size

    return top

def day7p1(root: Node) -> int:
    size = 0
    def dfs(root: Node):
        if not root:
            return

        nonlocal size

        if root.type == "dir" and root.name != "/" and root.size <= 100000:
            # print(f"name={root.name}, size={root.size}")
            size += root.size

        for _,node in root.children.items():
            dfs(node)

    dfs(root)

    return size


if __name__ == "__main__":
    test_input = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"
    ]

    print("--- Test ---")
    tree = build_tree(test_input)
    print(tree)
    ans = day7p1(tree)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input7.txt")
    tree = build_tree(input_raw)
    ans = day7p1(tree)
    print(ans)
