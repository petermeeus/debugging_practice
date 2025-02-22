class LinkedList:
    """
    Creates a linked list data structure
    """
    def __init__(self, item = None, next = None):
        self._item = item
        self._next = next

    def _list_empty_error(self) -> None:
        print("List empty")


    def get_first_item(self):
        """
        Returns the first value stored in the linked list
        :return: the first value stored in the linked list
        """
        if self._next is None:
            self._list_empty_error()
            return None
        return self._next._item

    def remove_first_item(self):
        """
        Returns and removes the first value stored in the linked list
        :return: the first value stored in the linked list
        """
        if self._next is None:
            self._list_empty_error()
            return None
        item = self._next._item
        self._next = self._next._next
        return item

    def size(self) -> int:
        """
        Returns the number of items stored in the linked list
        :return: the number of items stored in the linked list
        """
        size = 0
        node = self._next
        while node is not None:
            size += 1
            node = node._next
        return size

    def visit(self, action) -> None:
        """
        Performs an action for every item stored on the list
        :param action: function that takes the value of a node as input
        """
        if self._next is not None:
            action(self._next._item)
            self._next.visit(action)

    def _invalid_position(self) -> None:
        print("Invalid position")

    def _list_too_short_error(self) -> None:
        print("Linked list is too short")

    def get_item(self, pos: int):
        """
        Returns the item at the given position in the linked list
        :param pos: position of the item to return
        :return: the item at the given position in the linked list
        """
        if pos < 0:
            self._invalid_position()
            return None
        if self._next is None:
            self._list_too_short_error()
            return None
        if pos == 0:
            return self._next._item
        return self._next.get_item(pos - 1)

    def add(self, item, pos: int = 0) -> None:
        """
        Adds an item to the linked list
        :param item: item to add
        :param pos: position to add the item (by default at the start of the linked list)
        """
        if pos < 0:
            self._invalid_position()
        elif pos == 0:
            self._next = LinkedList(item, self._next)
        elif self._next is not None:
            self._next.add(item, pos - 1)
        else:
            self._list_too_short_error()

# From Tutorials 2.9 and 2.10

    def add_iterative(self, item, pos: int = 0) -> None:
        node = self
        while node._next is not None and pos != 0:
            node = node._next
            pos -= 1
        if pos == 0:
            node._next = LinkedList(item, node._next)
        else:
            self._invalid_position()

    def get_item_iterative(self, pos: int):
        node = self._next
        while node is not None and pos != 0:
            node = node._next
            pos -= 1
        if node is not None:
            return node._item
        else:
            self._invalid_position()
            return None
        
    def find_recursive(self, value) -> bool:
        node = self
        if node._next is not None:
            if node._next._item == value:
                return True
            return node._next.find(value)
        return False
    
    def find_iterative(self, value) -> bool:
        node = self
        if node == value:
            return True
        while node._next is not None and node._next._item != value:
            node = node._next
        if node._next is not None:
            return True
        return False
    
    def remove_all_r(self, value) -> None:

        node = self

        if node._item == value:
            node._item = node._next._item
            node._next = node._next._next
            node.remove_all_of_value_recursive(value)

        if node._next is not None:
            if node._next._item == value:
                node._item = node._next._item
                node._next = node._next._next
                node.remove_all_of_value(value)
            else:
                node._next.remove_all_of_value(value)
    
    def remove_all(self, value) -> None:
        node = self
        while node._next is not None:
            if node._next._item == value:
                node._next = node._next._next
            else:
                node = node._next
#--------------------------------------------#

    def _value_not_found_error(self):
        print("Value not found")

    def remove(self, value) -> None:
        """
        Removes the first occurrence of a given value
        :param value: value to remove
        """
        if self._next is not None:
            if self._next._item == value:
                self.remove_first_item()
            else:
                self._next.remove(value)
        else:
            self._value_not_found_error()

    def remove_iterative(self, value) -> None:
        node = self
        while node._next is not None and node._next._item != value:
            node = node._next
        if node._next is not None:
            node._next = node._next._next
        else:
            self._value_not_found_error()
