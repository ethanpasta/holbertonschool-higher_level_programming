#!/usr/bin/python3
class Node:
    """ Node class
    """

    def __init__(self, data, next_node=None):
        """ Initialization of Node object

        Args:
            data: value of node
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter of data property
        """
        return self.__data

    @property
    def next_node(self):
        """ Getter of next_node property
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Setter of data property

        Args:
            value: new value for data
        """
        if type(value) is not int:
            raise TypeErorr('data must be an integer')
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Setter of next_node property

        Args:
            value: new value for next_node
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """ SinglyLinkedList Class
    """

    def __init__(self):
        """ Initialization of singly linked list object
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Method to insert new node into list

        Args:
            value: value of new node to insert
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            tmp = self.__head
            if value < tmp.data:
                self.__head = Node(value, self.__head)
                return
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            newN = Node(value, tmp.next_node)
            tmp.next_node = newN

    def __str__(self):
        """ Method to return string representation of linked list
        """
        strS = ""
        tmp = self.__head
        while tmp:
            strS += str(tmp.data)
            strS += '\n' if tmp.next_node else ''
            tmp = tmp.next_node
        return strS
