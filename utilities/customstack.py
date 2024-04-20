"""
A custom stack implementation in Python.

Attributes:

Methods:
    isempty() -> bool: Check if the stack is empty.
    push(cls.stk: list, item) -> tuple: Push an item onto the stack.
    pop(cls.stk: list): Pop an item from the stack.
    peek(cls.stk: list): Return the top item of the stack without removing it.
    display(cls.stk: list): Display the stack.

Usage:
    Use this class to create and manipulate a stack data structure.
"""


class CustomStack:
    stk = None

    def __init__(self, stk):
        self.stk = stk

    @classmethod
    def push(cls, item) -> tuple:
        """
        Push an item onto the stack.

        Args:
            cls.stk (list): The stack to push the item onto.
            item: The item to push onto the stack.

        Returns:
            tuple: A tuple containing the updated stack and the index of
            the top element.

        Raises:
            TypeError: If cls.stk is not a list.
        """
        if not isinstance(cls.stk, list):
            raise TypeError
        else:
            cls.stk.append(item)
            top = len(cls.stk) - 1
            return cls.stk, top

    @classmethod
    def pop(cls):
        """
        Pop an item from the stack.

        Args:
            cls.stk (list): The stack to pop the item from.

        Returns:
            tuple: A tuple containing the updated stack, the index of the
            new top element, and the popped item.

        Raises:
            TypeError: If cls.stk is not a list.
        """
        if not isinstance(cls.stk, list):
            raise TypeError
        else:
            if cls.isempty():
                print("UnderflowError")
            else:
                item = cls.stk.pop()
                if len(cls.stk) == 0:
                    top = None
                else:
                    top = len(cls.stk) - 1
                return cls.stk, top, item

    @classmethod
    def peek(cls):
        """
        Return the top item of the stack without removing it.

        Args:
            cls.stk (list): The stack to peek at.

        Returns:
            Any: The top item of the stack.

        Raises:
            TypeError: If cls.stk is not a list.
        """
        if not isinstance(cls.stk, list):
            raise TypeError
        else:
            if cls.isempty():
                return "UnderflowError"
            else:
                top = len(cls.stk) - 1
                return cls.stk[top]

    @classmethod
    def display(cls):
        """
        Display the stack.

        Args:
            cls.stk (list): The stack to display.

        Raises:
            TypeError: If cls.stk is not a list.
        """
        if not isinstance(cls.stk, list):
            raise TypeError
        else:
            if cls.isempty():
                print("stack is empty")
            else:
                top = len(cls.stk) - 1
                print(cls.stk[top], "<---top")
                for a in range(top - 1, -1, -1):
                    print(cls.stk[a])

    @classmethod
    def isempty(cls) -> bool:
        """
        Check if the stack is empty.

        Args:
            cls.stk (list): The stack to check.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Raises:
            TypeError: If cls.stk is not a list.
        """
        if not isinstance(cls.stk, list):
            raise TypeError
        else:
            if not len(cls.stk):
                return True
            else:
                return False

    @classmethod
    def size(cls):
        return len(cls.stk)
