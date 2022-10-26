class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = ""
        for i in range(self.size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        if (not isinstance(n, int)) or (n < 0):
            raise ValueError("deposits should be natural number")
        self.size += n

    def withdraw(self, n):
        if (not isinstance(n, int)) or (n < 0):
            raise ValueError("withdrawals should be natural number")
        self.size -= n

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if (not isinstance(value, int)) or (value < 0):
            raise ValueError("capacity should be natural number")
        self._capacity = value

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)) or (value < 0):
            raise ValueError("size should be natural number")
        if value > self.capacity:
            raise ValueError("too many cookies in the jar")
        self._size = value
