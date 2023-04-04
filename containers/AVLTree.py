'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder
than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree():
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that
        all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        elif not node:
            return True
        else:
            verifyleft = AVLTree._is_avl_satisfied(node.left)
            verifyright = AVLTree._is_avl_satisfied(node.right)
        return verifyleft and verifyright

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        copyy = node
        if copyy.right:
            altroot = Node(copyy.right.value)
            altroot.left = Node(copyy.value)
            altroot.right = copyy.right.right
            altroot.left.right = copyy.right.left
            altroot.left.left = copyy.left
            return altroot
        else:
            return copyy

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        copyy = node
        if copyy.left:
            altroot = Node(copyy.left.value)
            altroot.left = Node(copyy.value)
            altroot.right = copyy.left.left
            altroot.right.left = copyy.left.right
            altroot.right.right = copyy.right
            return altroot
        else:
            return copyy

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview
        of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for
        your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        if node is None:
            node = Node(value)
            return node
        else:
            if value < node.value:
                lchild = AVLTree._insert(node.left, value)
                node.left = lchild
            else:
                rchild = AVLTree._insert(node.right, value)
                node.right = rchild
        fullt = AVLTree()
        fullt.root = node
        balanced = fullt._rebalance()
        return balanced

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
        else:
            return AVLTree
