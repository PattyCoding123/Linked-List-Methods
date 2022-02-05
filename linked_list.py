class Node:
    # The constructor of the data node needs
    # to initialize the data that the node stores, but
    # we will keep the link pointing to None as a default
    # parameter
    def __init__(self, userData, nextNode=None):
        self.data = userData
        self.next = nextNode

    # Overridden method to print out a node
    def __repr__(self):
        return "[%s]" % self.data

class LinkedList:

    # Constructor of Linked list class
    def __init__(self, data: list = None):
        self.head = None
        self.tail = None

        # If the data parameter is not empty,
        # then we will make sure to store the data
        # as nodes in our linked list. We will add it to
        # the end.
        if data:
            for i in range(len(data)):
                node = Node(data[i])
                self.addLast(node)

    # The object instance printing reference
    def __repr__(self):
        node = self.head
        LList = []
        while node is not None:
            if node is self.head:
                LList.append("[Head: %s]" % node.data)
            elif node is self.tail:
                LList.append("[Tail: %s]" % node.data)
            else:
                LList.append("[%s]" % node.data)
            node = node.next

        LList.append("None")
        return " -> ".join(LList)

    # To check if the Linked List is empty
    def isEmpty(self):
        return self.head is None

    # Function to insert data nodes at the beginning of the Linked List
    def addFirst(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node

        # We need to have the node point to whatever the current head is at
        # and then assign head to point to the node. This ensures the node is
        # now at the beginning of the list.
        else:
            node.next = self.head
            self.head = node


    # Function to insert data Nodes at the end of the Linked List
    def addLast(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node

        # To insert at the end, we need to have the tail node
        # point to the input node. Then, we will have tail point to
        # the node in order to show that it is the final node.
        else:
            self.tail.next = node
            self.tail = node


    # Function to delete data nodes starting at the beginning of the list
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("List is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # We set the head to point to whatever it is linked to in order to indicate that the previous
        # head is no longer apart of the list. This works because we the previous head node will
        # now be inaccessible.
        else:
            self.head = self.head.next


    # Function to delete data nodes at the end of the list
    def deleteLast(self):
        if self.isEmpty():
            raise Exception("List is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # We will have a prev pointer starting at the head
            # and a current_node starting at the node pointed by
            # head.next
            # IFF the current_node.next is not None, we will update
            # prev to point to current_node, then have current_node
            # point to whatever node it is pointing to next.
            # IFF current_node.next is None, we will set prev.next to
            # be none, as to show we are deleting current (since prev.next
            # is pointing to current_node), then we will have tail point
            # to prev
            prev = self.head
            current_node = self.head.next
            while current_node.next is not None:
                prev = current_node
                current_node = current_node.next
            prev.next = None
            self.tail = prev

    # Function that is to determine the size of the linked list
    def size(self):
        # if list is empty, return 0
        if self.isEmpty():
            return 0
        else:
            # If not empty, declare a size variable = 0
            # Have a current pointer and initialize it to the
            # head node of the list
            size = 0
            current = self.head

            # While current is pointing to a Node, we will
            # first increase the size to indicate that we
            # have counted a valid node. Then, have current
            # point to the next node.
            while current is not None:
                size += 1
                current = current.next

            return size

    # This function will return a node at our specified index
    def node_at_index(self, index):
        # If our list is empty, raise an exception
        if self.isEmpty():
            print("List is empty!")
            return None

        # If index is 0, return the head
        elif index == 0:
            return self.head

        else:
            # If index is greater than 0, have a current
            # pointer and initialize it to the head of the list
            # Then have a position variable set to 0
            current = self.head
            position = 0

            # While position is less than the target index, we will:
            # FIRST, have current point to the next node in the linked list.
            # SECOND, we will increment the position by 1 to indicate the current
            # node's new index in the linked list (we incremented by 1).
            while position < index:
                current = current.next
                position += 1

            # Once the while loop terminates, we are at the node at the
            # target index. Return current
            return current

    # This function will insert a node in the middle of the
    # linked list
    def insertInMid(self, node):
        # First, check if our linked list is EMPTY! If it is,
        # we will have the head and tail both point to the new
        # node in the linked list
        if self.isEmpty():
            self.head = node
            self.tail = node

        # If our linked list is NOT empty, then we need to determine
        # the middle index by doing integer division. We will call
        # the size method and divide the result by 2, and then subtract by
        # 1 to get the middle index since indices are 0 based.
        else:
            mid = (self.size() // 2) - 1

            # Have our input node's next index point to whatever the
            # middle node's next pointer was originally pointing to
            # (Since it will be in between mid and mid.next).
            # Finally, have the middle node's next pointer now
            # point to our input node. This effectively turns our
            # input node to the new middle node in the linked list.
            node.next = self.node_at_index(mid).next
            self.node_at_index(mid).next = node


myLinkedList = LinkedList([1, 2, 3, 4])
myLinkedList.addLast(Node("A"))
myLinkedList.addLast(Node("B"))
myLinkedList.addLast(Node("C"))
myLinkedList.addLast(Node("D"))

print("Node at index 7 = " + str(myLinkedList.node_at_index(7)))
print("Insert at Middle Index: Cool Beans")
myLinkedList.insertInMid(Node("Cool Beans"))

print(myLinkedList)
print("Count = " + str(myLinkedList.size()))

myLinkedList.deleteLast()

print(myLinkedList)
print("Count = " + str(myLinkedList.size()))

myLinkedList.deleteLast()

print(myLinkedList)

myLinkedList.deleteLast()

print(myLinkedList)

myLinkedList.deleteLast()

print(myLinkedList)




