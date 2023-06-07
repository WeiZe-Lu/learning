import ctypes
from line_profiler_pycharm import profile

class List:
    @profile
    def __init__(self):
        self._n = 0
        self._max = 1
        self._A = self._make_array(1)

    @profile
    def __len__(self):
        return self._n

    @profile
    def _append(self, val):
        if self._n == self._max:
            self._A = self._make_array(self._max * 2)
        self._A[self._n] = val
        self._n += 1

    @profile
    def _resize(self, c):
        old = self._A
        self._A = self._make_array(c)
        for i in range(len(old)):
            self._A[i] = old[i]
        self._max = c

    @profile
    def _resizes(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._max = c

    @profile
    def pop(self):
        self._A[self._n] = None
        self._n -= 1

    @profile
    def _make_array(self, c):
        return (c * ctypes.py_object)()

    @profile
    def __getitem__(self, n):
        if not 0 <= n <= self._n:
            raise IndexError('invaild index')
        return self._A[n]


if __name__ == '__main__':
    lists = List()
    pass
