"""
A custom stack implementation in Python.

Attributes:
    None

Methods:
    isempty(stk: list) -> bool: Check if the stack is empty.
    push(stk: list, item) -> tuple: Push an item onto the stack.
    pop(stk: list): Pop an item from the stack.
    peek(stk: list): Return the top item of the stack without removing it.
    display(stk: list): Display the stack.

Usage:
    Use this class to create and manipulate a stack data structure.
"""

class CustomStack():
    def __init__(self):
        pass

    def isempty(self, stk: list) -> bool:
        """
        Check if the stack is empty.

        Args:
            stk (list): The stack to check.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Raises:
            TypeError: If stk is not a list.
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            if stk == []:
                return True
            else:
                return False

    def push(self, stk: list, item) -> tuple:
        """
        Push an item onto the stack.

        Args:
            stk (list): The stack to push the item onto.
            item: The item to push onto the stack.

        Returns:
            tuple: A tuple containing the updated stack and the index of
            the top element.

        Raises:
            TypeError: If stk is not a list.
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            stk.append(item)
            top = len(stk) - 1
            return (stk, top)

    def pop(self, stk: list):
        """
        Pop an item from the stack.

        Args:
            stk (list): The stack to pop the item from.

        Returns:
            tuple: A tuple containing the updated stack, the index of the
            new top element, and the popped item.

        Raises:
            TypeError: If stk is not a list.
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            if self.isempty(stk):
                print("UnderflowError")
            else:
                item = stk.pop()
                if len(stk) == 0:
                    top = None
                else:
                    top = len(stk) - 1
                return stk, top, item

    def peek(self, stk: list):
        """
        Return the top item of the stack without removing it.

        Args:
            stk (list): The stack to peek at.

        Returns:
            Any: The top item of the stack.

        Raises:
            TypeError: If stk is not a list.
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            if self.isempty(stk):
                return "UnderflowError"
            else:
                top = len(stk) - 1
                return stk[top]

    def display(self, stk: list):
        """
        Display the stack.

        Args:
            stk (list): The stack to display.

        Raises:
            TypeError: If stk is not a list.
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            if self.isempty(stk):
                print("stack is empty")
            else:
                top = len(stk) - 1
                print(stk[top], "<---top")
                for a in range(top - 1, -1, -1):
                    print(stk[a])
