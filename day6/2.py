class Tree:
    def __init__(self,data):
        self.data=data #['drinks'] ['Hot']['Cold']
        self.Tree_List=[]#101   102     103


    def addChild(self, child):
        self.Tree_List.append(child)

    def printTree(self, level=0):
        print('  ' * level + self.data)
        for child in self.Tree_List:
            child.printTree(level + 1)

rootObj = Tree('Drinks')
hot     = Tree('Hot')
cold    = Tree('Cold')

rootObj.addChild(hot)
rootObj.addChild(cold)

tea = Tree('Tea')
coffee = Tree('Coffee')

hot.addChild(tea)
hot.addChild(coffee)

tea.addChild(Tree('Black Tea'))
tea.addChild(Tree('Milk Tea'))

cold.addChild(Tree('Cola'))
cold.addChild(Tree('Juice'))

rootObj.printTree()

