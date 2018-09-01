class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

        def __str__(self):
            pass

        def __repr__(self):
            pass


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, value):
        pass

    def in_order(self, callable=lambda node: print(node)):
        """
        Go left, visit, go right
        """

        def _walk(node=None):
            if node is None:
                return

            # Go Left
            if node.left is not None:
                _walk(node.left)

            callable(node)
            # Go Right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """
        Visit, then go left, then right!
        """

        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go Left
            if node.left is not None:
                _walk(node.left)

            # Go Right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """
        Go Left, go Right, then visit!
        """

        def _walk(node=None):
            if node is None:
                return

            # Go Left
            if node.left is not None:
                _walk(node.left)

            # Go Right
            if node.right is not None:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)