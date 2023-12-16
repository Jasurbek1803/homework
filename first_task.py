class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None



number1 = Node(4)
number2 = Node(2)
number3 = Node(5)
number4 = Node(6)

linkedlist = Linkedlist()
linkedlist.head = number1
number1.next = number2
number2.next = number3
number3.next = number4

while linkedlist.head != None:
    print(linkedlist.head.value, end=" ->")
    linkedlist.head = linkedlist.head.next
print("None")