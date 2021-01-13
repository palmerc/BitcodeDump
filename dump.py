#!/usr/bin/env python3
import sys
from macholib.MachO import MachO


def main():
    filename = sys.argv[1]
    m = MachO(filename)

    __LLVM = (cmd for load_cmd, cmd, data in m.headers[0].commands
              if getattr(cmd, 'segname', b'').decode('utf8').rstrip('\0') == '__LLVM')
    for llvm in __LLVM:
        print('__LLVM segment: offset {} size {}'.format(hex(llvm.fileoff), hex(llvm.filesize)))
        f = open(filename, 'rb')
        f.seek(llvm.fileoff)
        open(filename + '.xar', 'wb').write(f.read(llvm.filesize))


if __name__ == "__main__":
    main()
