class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Linked List
head = Node(5)
head.next = Node(8)
head.next.next = Node(7)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)

# Reverse the Linked List
temp = head
prev = None

while temp is not None:
    front = temp.next
    temp.next = prev
    prev = temp
    temp = front

# New head
head = prev

# Print the reversed Linked List
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next