class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            # check if .right exists
            if self.right is not None:
            # if so, make that node call insert with the same value
                self.right.insert(value)

            ##if not, create a node with that value, set node as right child
            else:
                new_node = BSTNode(value)
                self.right = new_node
        
        # else, go left
        else:
            # check if .left exists
            if self.left is not None:
                self.left.insert(value)
            else:
                new_node = BSTNode(value)
                self.left = new_node
 
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False

        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        
    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right
        
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)