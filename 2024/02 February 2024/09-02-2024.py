"""

Author : Shuvam Kumar Singh
Date : 09/02/2024
Problem : Check for Children Sum Property in a Binary Tree
Difficulty : Medium

"""


class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # Helper function to check if a node satisfies the sum property
        def is_sum_property_helper(node):
            # If the node is None, it satisfies the sum property
            if not node:
                return True, 0
            # If the node is a leaf node, it satisfies the sum property
            if not node.left and not node.right:
                return True, node.data
            # Recursively check the sum property for left and right subtrees
            left_result, left_sum = is_sum_property_helper(node.left)
            right_result, right_sum = is_sum_property_helper(node.right)
            # Check if the current node satisfies the sum property
            if left_result and right_result and node.data == left_sum + right_sum:
                return True, node.data
            else:
                return False, 0
        
        # Start checking the sum property from the root node
        result, _ = is_sum_property_helper(root)
        return 1 if result else 0
