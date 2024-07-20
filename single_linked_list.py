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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def main():
    linked_list = SinleLinkedList()
    print("Nothing in the linked list yet" or linked_list.print_list())
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(6)
    linked_list.insert_at_beginning(7)
    linked_list.print_list()

if __name__ == "__main__":
    main()