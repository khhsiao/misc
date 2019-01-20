import sys

def print_struct(s):
    print('==', s, '==')
    for k, v in gdb.types.deep_items(gdb.lookup_type(s)):
        print("%15s %10s %5d %5d" % (v.type, v.name, v.bitpos, v.type.sizeof))
    print()

if __name__ == '__main__':
    for struct in sys.stdin:
        print_struct(struct.strip())
