"""
Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]
"""


class Element:
    def __init__(self, input):
        self.input = input
        self.output = []

    @property
    def input(self):
        return self._array

    @input.setter
    def input(self, val):
        if isinstance(val, (int, str, bool)):
            val = list(val)
        self._array = val

    @classmethod
    def find_and_sum_numbers(cls):






l = [-25, -10, -7, -3, 2, 4, 8, 10]
mode = Element(l)


print(mode.find_and_sum_numbers())