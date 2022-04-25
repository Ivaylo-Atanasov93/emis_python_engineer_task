class Node:
    def __init__(self, data, pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_the_beggining(self, node):
        node = Node(node, self.head)
        self.head = node

    def insert_after(self, node, data):
        if not node:
            print('The given node must be in the LinkedList object')
            return
        new_node = Node(data, node.pointer)
        node.pointer = new_node

    def append_to_linked_list(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.pointer:
            last = last.pointer
        last.pointer = new_node

    def delete_node(self, position):
        if not self.head:
            print(f'The LinkedList object does not contain any nodes!')
            return
        temp_node = self.head
        if position == 0:
            self.head = temp_node.pointer
            temp_node = None
            return
        for i in range(position - 1):
            temp_node = temp_node.pointer
            if not temp_node:
                break
        if not temp_node:
            return
        if not temp_node.pointer:
            return
        pointer = temp_node.pointer.pointer
        temp_node.pointer = Node
        temp_node.pointer = pointer

    def __repr__(self):
        temp_node = self.head
        output = ''
        while temp_node:
            output += f'{str(temp_node.data)} '
            temp_node = temp_node.pointer
        return output
