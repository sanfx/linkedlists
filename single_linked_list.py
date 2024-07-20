class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            # setting the next new node when data is inserted
            self.head = new_node
        else:
            # setting the next node when data is inserted.
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, key):
            current = self.head
            prev = None

            # Traverse until we find the node with the given key
            while current:
                if current.data == key:
                    break
                prev = current
                current = current.next

            # If node not found
            if current is None:
                print(f"Node with key {key} not found.")
                return

            # Update pointers to skip the current node
            if prev:
                prev.next = current.next
            else:
                # If deleting the head node
                self.head = current.next

    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position. Position must be non-negative.")
            return

        current = self.head
        prev = None
        index = 0

        # Traverse until we reach the desired position
        while current and index < position:
            prev = current
            current = current.next
            index += 1
            if current:
                print(current.data)

        # If position exceeds the list length
        if not current:
            print(f"Position {position} is out of range.")
            return

        # Update pointers to skip the current node
        if prev:
            prev.next = current.next
            print("Update pointers to skip the current node: ", prev.data)
        else:
            # If deleting the head node
            self.head = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next

def main():
    linked_list = SinleLinkedList()
    print("Nothing in the linked list yet" or linked_list.print_list())
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(6)
    linked_list.insert_at_beginning(7)
    linked_list.print_list()
    print("\nNow deleting the node with data 5.\n")
    linked_list.delete_node(5)
    linked_list.print_list()
    linked_list.insert_at_end(2)
    print("\nDeleting node from linked list based on the position.\n")
    linked_list.delete_at_position(2)
    linked_list.print_list()

if __name__ == "__main__":
    main()