'''Test code'''
from linkedlist import LinkedList


def main():
    llist = LinkedList()
    llist.append(1)
    llist.printlist()

    llist.insert_at_pos(1, 3)
    llist.printlist()

    llist.push(0)
    llist.printlist()

    llist.insert_at_pos(2, 0)
    llist.printlist()

    s_node = llist.search(3)
    llist.insert_after(s_node, 4)
    llist.printlist()

    llist.append(-1)
    llist.printlist()

    llist.head = llist.mergesort(llist.head)
    llist.printlist()

    # nth = llist.get_at_pos(2)
    # if nth:
    #     print("element at 2nd index ->", nth.data)

    # mid = llist.get_mid()
    # if mid:
    #     print("middle element ->", mid.data)

    # count = llist.count(0)
    # print("count of 0 is", count)

    # node = llist.get_at_pos(len(llist) - 1)
    # node.next = llist.head
    # print("loop_length ->", llist.loop_length())

    llist.delete(4)
    llist.printlist()

    llist.delete_at_pos(0)
    llist.printlist()

    llist.delete_list()
    llist.printlist()


if __name__ == "__main__":
    main()
