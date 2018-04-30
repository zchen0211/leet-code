import sys






















# Tree related

# BST:
# search: O(log(N)) just go left/right if larger/smaller
# insert: always at leaf
# delete:

# Red-Black Tree
# Members: key(x), color(x), left(x), right(x), parent(x)
# 1. Every node is either red or black.
# 2. Every leaf (NIL) is black.
# 3. If a node is red, then both its children are black.
# 4. Every simple path from a node to a descendant leaf contains the same number of black nodes.
# Lemma 14.1 A red-black tree with n internal nodes has height at most 2*lg(n + 1).
##  Left/right rotate
#    y         x
#  x   z <-> a   y
# a b           b z
##  Insert: insert a red node, then adjust until all properties are met
# case 1: property 3 violated (recolor)
# case 2: rotate left
# case 3: rotate right
# other structures: AVL tree, may require O(log n) rotations
# 2-3 Tree (Hopcroft)
# B-Tree
# i-th order statistics
# augment RB-tree with size(x)

# B-trees
# better at mimizing disk I/O operations

# Trie
class TrieNode():
  def __init__(self):
    self.child = {} # char to other TrieNode
    self.is_end = False

class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for c in word:
      if c not in node.child:
        node.child[c] = TrieNode()
      node = node.child[c]
    node.is_end = True

# Sement-Tree (store ops of an interval, really good problem 307, 308)
