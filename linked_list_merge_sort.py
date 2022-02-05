from linked_list import LinkedList
from linked_list import Node

def merge_sort(linked_list):
    """
    :param linked_list:
    :return: Return a sorted linked list

    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produced sorted sublists until one remains
    Time Complexity: O(kn log(n))
    """

    if linked_list.size() == 1:
        return linked_list

    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    :param linked_list:
    :return:
    Divide the unsorted list at midpoint into sublists
    Time Complexity: O(k log(n))
    """

    # If the linked list is empty, then have the left_half
    # of the linked list be assigned to and then
    # have the right half be none. Return the left half
    # and the right half
    if linked_list.head is None or linked_list is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    # Use the size method to get the size of the linked list,
    # then calculate the mid point
    else:
        size = linked_list.size()
        mid = size // 2

        # The mid node should be mid - 1 since indexing starts
        # at index 0 for our function
        mid_node = linked_list.node_at_index(mid - 1)

        # Assign the left_half linked list to contain the full
        # input linked list
        left_half = linked_list

        # Assign the right_half to be a brand new linked list,
        # then assign mid_node.next to be the head of the right list
        right_half = LinkedList()
        right_half.addLast(mid_node.next)

        # Cut the connection between left and right by assigning
        # mid_node.next = None. This way, the left linked list stops
        # at mid and the right linked list starts at mid + 1
        mid_node.next = None

        return left_half, right_half

def merge(left, right):
    """
    :param left: first half of linked list
    :param right: second half of linked list
    :return: a new merged linked list

    merges two linked list, sorting by data in the nodes

    Time Complexity: O(n)
    """

    # Create a new linked list that contains nodes from
    # merging left and right linked lists

    merged = LinkedList()

    # Add a fake/dummy head that is discarded later
    merged.addLast(Node(0))

    # Assign current to be the head of merged,
    # Then assign left_head and right_head pointers
    # To be assigned to their respective heads of the
    # linked lists
    current = merged.head
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node
    # of either

    while left_head or right_head:
        # If the head node of left is none, we are past its tail.
        # Add the node from the right to merged linked list
        if left_head is None:
            current.next = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next

        # If the head node of right is none, we are past its tail.
        # Add the node from the left to merged linked list
        elif right_head is None:
            current.next = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next

        else:
            # Not either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next = left_head
                # Move left head to the next node
                left_head = left_head.next
            # If data on left is greater than right, set current to right node
            else:
                current.next = right_head
                # Move right head to next node
                right_head = right_head.next
        # Move current to next node
        current = current.next


    # Discard dummy/fake node and set first merged node as head
    merged.tail = current
    merged.head = merged.head.next

    return merged

l = LinkedList([10,2,200, 44,15,100])
print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)



