from node import Node


class LinkedList:

    def __init__(self) -> None:
        # Initially self.head is at None
        self.head = None

    def push(self, new_data):
        """Inserting new data at the beginning."""
        new_node = Node(new_data)
        new_node.next = self.head
        # When a new data is inserted to 
        # LL the head is pointed to newly 
        # inserted node.
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detect_loop(self):
        s = set()
        temp = self.head
        while(temp):

            # If we already have
            # this node in hashmap it
            # means there is a cycle
            # (Because we are encountering
            # the node second time).
            if (temp in s):
                return True

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
            temp = temp.next

def main():
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(4)
    llist.push(2)
    llist.push(6)
    # Manually creating a loop for testing
    llist.head.next.next = llist.head.next
    if llist.detect_loop():
        print("Loop detected.")
    else:
        print("No Loop found.")
        llist.print_list()

