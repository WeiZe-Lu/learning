from line_profiler_pycharm import profile


class Empty(Exception):
    """This is a class defined by myself """
    pass


class LinkedStack(object):
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, e, next):
            """Define the value and the point"""
            self._element = e
            self._next = next

    def __init__(self):
        """Define the bottom and the size,the bottom is the stack's feature and the _size
        is convenient to return the size of the stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """return the size"""
        return self._size

    def __eq__(self, other):
        return type(other) is type(self) and other._size == self._size

    def __ne__(self, other):
        return not (self == other)

    def is_empty(self):
        """return if the stack is empty"""
        return not self._size

    def push(self, e):
        """the _next is point to the bottom"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        """the _head is the bottom ,so when we pop the node ,we can point
        to the near the bottom"""
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head._element = None
        self._head = self._head._next
        self._size -= 1
        return answer


class LinkedQueue(object):
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, e, next=None):
            """Define the value and the point"""
            self._element = e
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("The queue is empty")
        return self._head._element

    @profile
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("This queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size = self._size - 1
        if self.is_empty():
            self._tail = None
        return answer

    @profile
    def enqueue(self, e):
        """The node can't increase casually,the node must need to
        match the characteristics of the queue,the tail must is the newest
        and the head must is the head,the newest address is only one ,either
        Assign value to _head or _tail"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest  # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest
        self._size = self._size + 1


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, next=None):
            self._element = e
            self._next = next

    def __init__(self):
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self.__tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        oldhead = self.__tail._next
        if self.__size == 1:
            self.__tail = None
        else:
            self.__tail._next = oldhead._next
        self.__size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self.__tail._next  # 将新节点连接到链表中
            self.__tail._next = newest  # 将新节点设置为头节点
        self.__tail = newest  # 将尾节点设置为新节点
        self.__size += 1


linkedqueue = LinkedQueue()
for i in range(5):
    linkedqueue.enqueue(i)
for i in range(5):
    linkedqueue.dequeue()
cirqueue = CircularQueue()
print(dir(CircularQueue._Node))
cirqueue.enqueue(1)
cirqueue.enqueue(2)

"""
class _DoublyLinkedBase:
    '''this class need some function'''

class PositionalList(doubly_linked_base._DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            '''Return the element stored at this Position'''
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not self == other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def delete(self,p):
        node=self._validate(p)
        return self._delete_node(node)

    def __iter__(self):
        cursor=self.first()
        while cursor is not None:
            yield cursor.element()
            cursor=self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        newest=super()._insert_between(e,predecessor,successor)
        return self._make_position(newest)

    def add_first(self,e):
        return self._insert_between(e,self._trailer._prev,self._trailer)

    def add_before(self,p,e):
        original = self._validate(p)
        return  self._insert_between(e,original,original._next)





if __name__ == '__main__':
    pass
"""
