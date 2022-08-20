
def load(path: str) -> list[str]:
    ret = list()
    with open(path) as f:
        ret = f.read().splitlines()
    return ret
