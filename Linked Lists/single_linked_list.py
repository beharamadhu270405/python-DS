class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is not None:
            p = self.head
            while p is not None:
                print(p.data, " ", end='')
                p = p.next
            print()
        return

    def count_nodes(self):
        p = self.head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        print("Number of Nodes in the list = ", n)

    def search(self, x):
        position = 1
        p = self.head
        while p is not None:
            if p.data == x:
                print(x, " is at position ", position)
                return True
            position += 1
            p = p.next
        return False

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_after_specific_node(self, prev_node, data):
        if prev_node is not None:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node


if __name__ == '__main__':
    singleLinkedList = SingleLinkedList()
    singleLinkedList.insert_at_beginning("Madhu")
    singleLinkedList.insert_at_beginning("Prakash")
    singleLinkedList.insert_at_end("Behara")
    singleLinkedList.insert_at_end("Every Day")
    singleLinkedList.display_list()
