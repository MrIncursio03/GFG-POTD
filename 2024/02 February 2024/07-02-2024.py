"""

Author : Shuvam Kumar Singh
Date : 07/02/2024
Problem : Min distance between two given nodes of a Binary Tree
Difficulty : Medium

"""


class Solution:
    def findDist(self, root, a, b):
        # Utility function to find the distance between a node and its ancestor
        def distance_to_ancestor(node, target, level):
            if not node:
                return -1
            if node.data == target:
                return level
            left = distance_to_ancestor(node.left, target, level + 1)
            right = distance_to_ancestor(node.right, target, level + 1)
            return max(left, right)

        # Utility function to find LCA of two nodes
        def find_LCA(node, a, b):
            if not node:
                return None
            if node.data == a or node.data == b:
                return node
            left = find_LCA(node.left, a, b)
            right = find_LCA(node.right, a, b)
            if left and right:
                return node
            return left if left else right

        # Find the LCA of nodes 'a' and 'b'
        lca = find_LCA(root, a, b)
        
        # Calculate the distances from LCA to nodes 'a' and 'b'
        dist_a = distance_to_ancestor(lca, a, 0)
        dist_b = distance_to_ancestor(lca, b, 0)

        # Return the sum of distances from LCA to nodes 'a' and 'b'
        return dist_a + dist_b
