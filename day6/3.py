class Tree:
    def __init__(self, data):
        self.data = datas
        self.Tree_List = []

    def addChild(self, child):
        self.Tree_List.append(child)

    def printTree(self, level=0):
        print('  ' * level + self.data)
        for child in self.Tree_List:
            child.printTree(level + 1)


n1 = Tree('n1')
n2 = Tree('n2')
n3 = Tree('n3')

n1.addChild(n2)
n1.addChild(n3)

n4 = Tree('n4')
n5 = Tree('n5')

n2.addChild(n4)
n2.addChild(n5)

n4.addChild(Tree('n9'))
n4.addChild(Tree('n10'))

n3.addChild(Tree('n6'))
n3.addChild(Tree('n7'))


n1.printTree()
