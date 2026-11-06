# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None



# def count_length_of_loop(head):
#     temp = head
#     travel = 0
#     my_dict = {}

#     while temp is not None:
#         if temp in my_dict:
#             return travel - my_dict[temp]
#         my_dict[temp] = travel
#         travel += 1
#         temp = temp.next
#     return 0

# # Create Linked List
# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(7)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(2)

# print(count_length_of_loop(head))




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_of_length(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return 0