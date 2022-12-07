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
                # print(f"Buld dir={name} with parent={root.name}")
                root.children[name] = Node("dir", name, parent=root)
        else: # Output
            size = int(cmd[0])
            name = cmd[1]
            if root:
                root.children[name] = Node("file", name, size, parent=root)

    return top

def compute_sizes(root: Node) -> None:
    
    def sizes(root: Node) -> int:
        if root.type == "file":
            return root.size

        for _,node in root.children.items():
            root.size += sizes(node) 
        return root.size

    root.size = sizes(root)

def sizes(root: Node) -> list[tuple[str,int]]:
    ans = []

    def dfs(root: Node) -> None:
        if not root:
            return

        if root.type == "dir":
            # print(f"dir={root.name}")
            ans.append((root.name, root.size))

        for _,node in root.children.items():
            dfs(node)

    dfs(root)

    return ans

def day7p1(sizes: list[tuple[str,int]]) -> int:
    return sum(map(lambda x: x[1] if x[1] <= 100000 else 0, sizes))


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
    compute_sizes(tree)
    print(tree)
    size = sizes(tree)
    print(size)
    ans = day7p1(size)
    print(ans)

    print("--- Part 1 ---")
    input_raw = load_input.load("./inputs/input7.txt")
    tree = build_tree(input_raw)
    compute_sizes(tree)
    size = sizes(tree)
    # print(size)
    ans = day7p1(size)
    print(ans)
