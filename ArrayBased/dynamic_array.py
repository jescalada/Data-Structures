import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)  # Low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("Invalid Index")
        return self._A[k]

    def __str__(self):
        temp = ['[']
        temp.extend(f'{str(self._A[i])}, ' for i in range(self._n))
        temp.append(']')
        return "".join(temp)

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):  # Shifts all the right side elements one step to the right
            self._A[j] = self._A[j-1]
        self._A[k] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)  # Creates a new array
        for k in range(self._n):  # Copies the values of the current array into the new array
            B[k] = self._A[k]
        self._A = B  # Sets the array in this object to the new array
        self._capacity = c  # Sets the new capacity of the array

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()
