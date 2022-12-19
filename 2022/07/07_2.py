import sys
import fileinput
from dataclasses import dataclass, field

'''
python 07_2.py input_07.txt
'''


@dataclass
class FileSystem:
    name: str = '/'
    size: int = 0
    parent: str = ''
    children: dict = field(default_factory=dict)


def walk_fs(fs: FileSystem, mem_needed: int, del_dir_size: int):
    if fs.size >= mem_needed and fs.size < del_dir_size:
            del_dir_size = fs.size

    if len(fs.children):
        for k,v in fs.children.items():
            del_dir_size = walk_fs(v, mem_needed, del_dir_size)

    return del_dir_size


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


def get_dir_to_delete(lines: list):
    fs = FileSystem()
    curr = []
    mem_total = 70000000
    mem_req = 30000000
    mem_need = 0
    dir_size_to_delete = 0

    # Build file system
    for line in lines:
        if line[0] == '$':
            fs, curr = exec_cmd(line, fs, curr)
        else:
            fs = parse_item(line, fs, curr)

    # Get needed mem
    mem_need = mem_req - (mem_total - fs.size)

    # Walk file system and get dir size closest to needed mem
    # Start with root dir size
    dir_size_to_delete = fs.size
    dir_size_to_delete = walk_fs(fs, mem_need, dir_size_to_delete)
    return dir_size_to_delete


def main():
    lines = []
    with fileinput.input(encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())

    result = get_dir_to_delete(lines)

    assert result == 5649896
    print(f'Success for result: {result}')


if __name__ == "__main__":
    main()
