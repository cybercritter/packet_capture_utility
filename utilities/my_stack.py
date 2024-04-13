
class CustomStack():
    def __init__(self):
        pass

    def isempty(self, stk: list) -> bool:
        """
        The isempty function checks if the stack is empty.
            Args:
                stk (list): The stack to be checked.
            Returns:
                bool: True if the stack is empty, False otherwise.

        :param self: Refer to the class instance itself
        :param stk: list: Check if the stack is empty
        :return: A boolean value
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
        The push function takes a list and an item as arguments.
        It then appends the item to the end of the list, and returns a tuple
        containing the updated stack (list) and its top index.

        :param self: Allow the function to be called from within the class
        :param stk: list: Specify the stack that we want to push an item onto
        :param item: int: Specify the type of data that is being pushed
                          onto the stack
        :return: A tuple containing the stack and the top of the stack
        """
        if not isinstance(stk, list):
            raise TypeError
        else:
            stk.append(item)
            top = len(stk) - 1
            return (stk, top)

    def pop(self, stk: list):
        """
        The pop function removes the top item from a stack.
            Args:
                stk (list): The stack to pop an item from.
            Returns:
                list, int, object: The new stack with the popped item removed,
                                    the index of the new top of the stack and
                                    a reference to that element in memory.

        :param self: Represent the instance of the class
        :param stk: list: Specify the stack that is being used
        :return: The stack, top and item
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
        The peek function returns the top element of a stack.

        :param self: Represent the instance of the class
        :param stk: list: Specify the stack that is being passed to
                          the function
        :return: The last element of the stack
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
        The display function prints the contents of a stack.
            The top element is printed first, followed by each element
            in descending order.
            If the stack is empty, it prints &quot;stack is empty&quot;.

        :param self: Represent the instance of the class
        :param stk: list: Pass the stack to the function
        :return: Nothing
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
