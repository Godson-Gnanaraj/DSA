class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self._head = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, val):
        if isinstance(val, Node):
            self._head = val
        elif val is None:
            self._head = None
        else:
            self._head = Node(val)

    def __len__(self):
        if self.head is None:
            return 0

        if self.detect_loop():
            raise StopIteration("Looped List")

        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def printlist(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print(curr_node)

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node

    @staticmethod
    def insert_after(prev_node, data):
        if not isinstance(prev_node, Node):
            return

        node = Node(data)
        node.next = prev_node.next
        prev_node.next = node

    def insert_at_pos(self, pos, data):
        if not self.head:
            return

        curr_node = self.head
        for _ in range(pos - 1):
            if not curr_node:
                return
            curr_node = curr_node.next

        node = Node(data)
        node.next = curr_node.next
        curr_node.next = node

    def search(self, key):
        if not self.head:
            return None
        curr_node = self.head
        while curr_node:
            if key == curr_node.data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return

        prev_node = self.head
        curr_node = prev_node.next
        while curr_node:
            if curr_node.data != key:
                prev_node = curr_node
                curr_node = curr_node.next
                continue
            prev_node.next = curr_node.next
            break

    def delete_at_pos(self, pos):
        if not self.head:
            return

        if pos == 0:
            self.head = self.head.next
            return

        prev_node = self.head
        curr_node = prev_node.next

        for _ in range(pos - 1):
            if not curr_node:
                return
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = curr_node.next

    def delete_list(self):
        self.head = None

    def get_at_pos(self, pos):
        if self.head is None:
            return self.head

        curr_node = self.head
        for _ in range(pos):
            if curr_node is None:
                return None
            curr_node = curr_node.next
        return curr_node

    def get_mid(self, head=None):
        if head is None:
            head = self.head

        if head is None:
            return None

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def count(self, key):
        count = 0
        if self.head is None:
            return count

        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                count += 1
            curr_node = curr_node.next
        return count

    def detect_loop(self):
        if self.head is None:
            return False

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def loop_length(self):
        count = 0
        if self.head is None:
            return count

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is not fast:
                continue

            count = 1
            slow = slow.next
            while slow is not fast:
                count += 1
                slow = slow.next
            return count

        return count

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        return result

    def mergesort(self, head):
        if head is None or head.next is None:
            return head

        mid = self.get_mid(head)
        midnxt = mid.next
        mid.next = None

        left = self.mergesort(head)
        right = self.mergesort(midnxt)

        sorted_list = self._merge(left, right)
        return sorted_list
