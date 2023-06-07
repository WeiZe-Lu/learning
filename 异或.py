class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = 0
        for i in range(n):
            a = a ^ start + 2 * i
        return a


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);
            line = next(lines)
            start = int(line);

            ret = Solution().xorOperation(n, start)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()