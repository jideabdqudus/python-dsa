from collections import deque

deque()

x = deque("abcde")
x.append("f")
print(x)


# Queue = FIFO
# Stack = LIFO

""""
    append #Queue
    pop #Queue
    appendleft #Stack 
    popleft    #Stack
"""

#Class for the nodes on the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        print(self.data)
        return self.data

#Class for the linked list
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

llist = LinkedList()
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")
llist.head = first_node
first_node.next = second_node
second_node.next = third_node
llist.remove_node("c")
llist.add_before("b", Node("e"))
llist.add_after("b", Node("cc"))
llist.add_last(Node("e"))
print(llist)


# Doubly Linked Lists
# Circular Linked Lists

