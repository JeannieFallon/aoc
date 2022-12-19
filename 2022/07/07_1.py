import sys
import fileinput
from dataclasses import dataclass, field

'''
python 07_1.py input_07.txt
'''


@dataclass
class FileSystem:
    name: str = '/'
    size: int = 0
    parent: str = ''
    children: dict = field(default_factory=dict)


def walk_fs(fs: FileSystem, total_size: int):
    total_size += fs.size if fs.size < 100000 else 0

    if len(fs.children):
        for k,v in fs.children.items():
            total_size = walk_fs(v, total_size)

    return total_size


def exec_cmd(line: str, fs: FileSystem, curr: list):
    cmd = line[2:4]

    match cmd:
        case 'cd':
            dst = line[4:].strip() # destination dir
            if dst == '..':
                curr.pop()
            else:
                curr.append(dst)
        case 'ls':
            pass
        case _:
            raise ValueError(f"Command not implemented: {cmd}")

    return fs, curr


def parse_item(line: str, fs: FileSystem, curr: list):
    '''
    val1    val2
    dir     <dirname>
    <size>  <filename>
    '''
    val1, val2 = line.split()

    _fs = fs
    if val1 == 'dir':
        for c in curr:
            if c == '/':
                continue
            _fs = _fs.children[c]
        _fs.children[val2] = FileSystem(name=val2, parent=c)
    else:
        _fs.size += int(val1)
        for c in curr[1:]:
            _fs = _fs.children[c]
            _fs.size += int(val1)

    return fs


def get_total_size(lines: list):
    fs = FileSystem()
    curr = []           # list of parent nodes for current location
    total_size = 0

    # Build file system
    for line in lines:
        if line[0] == '$':
            fs, curr = exec_cmd(line, fs, curr)
        else:
            fs = parse_item(line, fs, curr)

    # Walk file system and sum dirs of size < 100000
    total_size = walk_fs(fs, total_size)
    return total_size


def main():
    lines = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    result = get_total_size(lines)

    assert result == 1077191
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
