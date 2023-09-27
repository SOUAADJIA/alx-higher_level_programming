#!/usr/bin/python3
"""Define node in a singly linked list."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data in the node, ensuring it's an integer."""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get the next node that this node points to."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, ensuring it's a Node object or None."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def to_string(self):
        """Convert the linked list to a string for printing."""
        string = ''
        current = self.head
        while current:
            string += str(current.data) + '\n'
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)
        current = self.head

        if current is None:
            # If the list is empty, set the new node as the head.
            self.head = new_node
            return

        if current.data > value:
            # If the new node should be the new head, update the head.
            new_node.next_node = self.head
            self.head = new_node
            return

        while current.next_node is not None:
            # Find the correct position to insert the new node.
            if current.next_node.data > value:
                break
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
