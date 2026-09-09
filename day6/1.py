#tree is a nonlinear data structure with hierarchical relationships 
#between its element
#without having any cycle ,
#it is bascically reversed from a real life tree 

#quicker and easier acces to the data 
#store hierarchical data,like folder structure, organization structure, xml/html data 
#binary trees are the data structures in which each node has at most two children 
#often refered to as the left and right children 
#binary tree is a family of data structure (BST,heap tree,AVL,red black trees)

#huffman coding problem , heap priority problem and expression parsing 
#problem can be solved efficiently using binary trees

#there are two ways for implementation
#linked list
#python list(array)



#linked list
# +---+---+---+
#                        | • | A | • |  <-- Root Node (A)
#                        +---+---+---+
#                          /       \
#          +--------------+         +--------------+
#          |                                       |
#          v                                       v
#    +---+---+---+                           +---+---+---+
#    | • | B | • |                           | X | C | • |
#    +---+---+---+                           +---+---+---+
#      /       \                                     \
#     /         \                                     \
#    v           v                                     v
# +---+---+---+ +---+---+---+                       +---+---+---+
# | X | D | X | | X | E | X |                       | X | F | X |
# +---+---+---+ +---+---+---+                       +---+---+---+
#  (Leaf Node)   (Leaf Node)                         (Leaf Node)


#python list
# Logical Tree View:
#                         [0] A
#                        /     \
#                 [1] B           [2] C
#                /     \         /     \
#           [3] D       [4] E   [5] F   [6] G

# 1D Memory Array Representation:
# +---------+---------+---------+---------+---------+---------+---------+
# |         |   'B'   |   'C'   |   'D'   |   'E'   |   'F'   |         |
# +---------+---------+---------+---------+---------+---------+---------+
#  Index: 0      1         2         3         4         5         6


