class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Appends a new node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        """Reverses the linked list in-place by modifying node references."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Merges two sorted linked lists into a new sorted linked list."""
        dummy = Node(0)
        tail = dummy
        a = list1.head if list1 else None
        b = list2.head if list2 else None

        while a and b:
            if a.data <= b.data:
                tail.next = Node(a.data)
                a = a.next
            else:
                tail.next = Node(b.data)
                b = b.next
            tail = tail.next

        # Додати залишкові елементи
        remaining = a if a else b
        while remaining:
            tail.next = Node(remaining.data)
            tail = tail.next
            remaining = remaining.next

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def insertion_sort(self):
        """Sorts the linked list using the insertion sort algorithm."""
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            # Створюємо копію вузла, щоб не порушувати оригінальний список
            sorted_head = self._sorted_insert(sorted_head, Node(current.data))
            current = next_node
        self.head = sorted_head

    def _sorted_insert(self, head, new_node):
        """Inserts a node into the correct position in a sorted linked list."""
        if not head or new_node.data <= head.data:
            new_node.next = head
            return new_node
        current = head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head

    def print_list(self):
        """Prints the linked list elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Приклад використання:
if __name__ == "__main__":
    # Створення та сортування першого списку
    ll1 = LinkedList()
    ll1.append(3)
    ll1.append(1)
    ll1.append(4)
    ll1.append(2)
    print("Original list 1:")
    ll1.print_list()

    ll1.insertion_sort()
    print("Sorted list 1:")
    ll1.print_list()

    # Створення та сортування другого списку
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(6)
    ll2.append(0)
    print("\nOriginal list 2:")
    ll2.print_list()

    ll2.insertion_sort()
    print("Sorted list 2:")
    ll2.print_list()

    # Об'єднання двох відсортованих списків
    merged = LinkedList.merge_sorted_lists(ll1, ll2)
    print("\nMerged sorted list:")
    merged.print_list()

    # Реверсування об'єднаного списку
    merged.reverse()
    print("Reversed merged list:")
    merged.print_list()