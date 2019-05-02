#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d} argument{}{}"
          .format(len(sys.argv) - 1,
                  's' if len(sys.argv) - 1 != 1 else '',
                  '.' if len(sys.argv) - 1 == 0 else ':'))
    if len(sys.argv) - 1 > 0:
        usr_args = sys.argv[1:]
        i = 1
        for arg in usr_args:
            print("{:d}: {}".format(i, arg))
            i += 1
