class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    print("Name:", elements)
    return root

if __name__ == '__main__':
    name = ["K", "Y", "L", "A", "C", "A", "M","I", "L", "L", "E", "A", ".", "L","I", "W", "A", "N", "A", "G"]
    name_tree = build_tree(name)
    print("\nMinimum Value:", name_tree.find_min())
    print("Maximum Value:", name_tree.find_max())

    print("\nIn order traversal:", name_tree.in_order_traversal())
    print("Pre order traversal:", name_tree.pre_order_traversal())
    print("Post order traversal:", name_tree.post_order_traversal())

    print("\nIs letter K in the list?", name_tree.search("K"))
    print("Is letter S in the list?", name_tree.search("S"))

    name_tree.delete("A")
    print("After Deleteing A", name_tree.in_order_traversal())
    name_tree.delete("L")
    print("After Deleteing L", name_tree.in_order_traversal())

    name_tree.delete("I")
    print("After Deleteing I", name_tree.in_order_traversal())
