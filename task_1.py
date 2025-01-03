class Node:
    """
    This module implements a singly linked list with various operations such as append, reverse, sorted merge, and insertion sort.
    Classes:
        Node: Represents a node in the linked list.
        LinkedList: Represents the linked list and provides methods to manipulate it.
    Methods:
        Node.__init__(self, data):
            Initializes a new node with the given data and sets the next pointer to None.
        LinkedList.__init__(self):
            Initializes an empty linked list with the head set to None.
        LinkedList.append(self, data):
            Appends a new node with the given data to the end of the linked list.
        LinkedList.reverse(self):
            Reverses the linked list in place.
        LinkedList.sorted_merge(self, other):
            Merges the current linked list with another sorted linked list in sorted order.
        LinkedList.insertion_sort(self):
            Sorts the linked list using the insertion sort algorithm.
        LinkedList.sorted_insert(self, head, node):
            Inserts a node into the sorted linked list at the correct position.
        LinkedList.print_list(self):
            Prints the elements of the linked list in a readable format.
    Example usage:
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        self.head = dummy.next

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head, node):
        if not head or node.data <= head.data:
            node.next = head
            return node
        current = head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll1 = LinkedList()
ll1.append(3)
ll1.append(1)
ll1.append(4)
ll1.append(2)

print("Original list:")
ll1.print_list()

ll1.reverse()
print("Reversed list:")
ll1.print_list()

ll1.insertion_sort()
print("Sorted list:")
ll1.print_list()

ll2 = LinkedList()
ll2.append(5)
ll2.append(6)

ll1.sorted_merge(ll2)
print("Merged list:")
ll1.print_list()
# Example usage:
ll1 = LinkedList()
ll1.append(3)
ll1.append(1)
ll1.append(4)
ll1.append(2)

print("Original list:")
ll1.print_list()

ll1.reverse()
print("Reversed list:")
ll1.print_list()

ll1.insertion_sort()
print("Sorted list:")
ll1.print_list()

ll2 = LinkedList()
ll2.append(5)
ll2.append(6)

ll1.sorted_merge(ll2)
print("Merged list:")
ll1.print_list()
