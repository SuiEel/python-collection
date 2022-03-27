#  File: ExpressionTree.py
#  Description: Creates a Binary Tree with an infix pattern and solves it
#  Student's Name: William Sears
#  Student's UT EID: wvs92
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 12/01
#  Date Last Modified: 12/02


class BinaryTree:
    

    def __init__(self, initval = None):
        self.data = initval
        self.left = None
        self.right = None
        self.parent = None

    def insertLeft(self, newNode):
        if self.left == None:
           self.left = BinaryTree(newNode)
        else:
           temp = BinaryTree(newNode)
           temp.left = self.left
           self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
           self.right = BinaryTree(newNode)
        else:
           temp = BinaryTree(newNode)
           temp.right = self.right
           self.right = temp

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, value):
        self.data = value

    def getRootVal(self):
        return self.data

    
    def evaluate(self):
        
        leftChild = self.left
        rightChild = self.right

        if leftChild and rightChild:
            operator = self.data
            if operator == "+":
                return (leftChild.evaluate() + rightChild.evaluate())
            elif operator == "-":
                return (leftChild.evaluate() - rightChild.evaluate())
            elif operator == "*":
                return (leftChild.evaluate() * rightChild.evaluate())
            elif operator == "/":
                return (leftChild.evaluate() / rightChild.evaluate())
        else:
            return self.data

    
    def createTree(self, expr):

        expList = expr.split()
        
        treeLevel = 0
        treeList = []
        treeList.append(self)
        current = self
        
        
        for token in expList:
          
            

            if token == "(":
                treeLevel += 1
                current.insertLeft("")
                treeList.append(current)
                current = current.left
                

            elif token not in "*/+-)":
                
                
                current.setRootVal(eval(token))
                parent = treeList.pop()
                current = parent
                                

            elif token in "*/+-":
                current.setRootVal(token)
                current.insertRight("")
                treeList.append(current)
                current = current.right
                

            

            elif token == ")":
                current = treeList.pop()
                

                
        print("   Value:", self.evaluate())
        print("   Prefix expression: ", end= "")
        
        preorder(self)
        print()


        print("   Postfix expression: ", end= "")
        postorder(self)
        print()
        print()
        

        
        


    
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal(), "", end= "")

      
def preorder(tree):
   if tree != None:
      print(tree.getRootVal(), "", end= "")
      preorder(tree.getLeftChild())
      preorder(tree.getRightChild())

                            
                
        



    #def preOrder (self, root):

    #def postOrder (self, root):


    
def main():
    txtFile = open("treedata.txt", "r")
    for line in txtFile:
        print("Infix expression:", line)
        expTree = BinaryTree("")
        expTree.createTree(line)
    


    
main()





