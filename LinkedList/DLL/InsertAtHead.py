class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at Head
    def insert_at_Head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node