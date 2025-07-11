#!/usr/bin/python3
"""A list that inherits from list object."""


class MyList(list):
    """Represent a custom list class that inherits from list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

    def __str__(self):
        """Return the string representation of the list."""
        return super().__str__()

    def append(self, item):
        """Append item to the list."""
        return super().append(item)

