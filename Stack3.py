class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this – saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER

      
class Stack ():
    def __init__(self):
       self.head = None
       

    def isEmpty (self):
        return self.head == None

    def push (self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        

    def pop (self):
        item = self.head.data
        self.head = self.head.getNext()
        return item

    def peek (self):
        return self.head.data

    def size (self):
        current = self.head
        count = 0
        while current:
            current = current.getNext()
            count += 1
            
        return count

##################################################

def main():

    print("Running Stack3.py")
    myStack = Stack()
    print(myStack.isEmpty())
    myStack.push("cat") 
    myStack.push(4)
    print(myStack.peek())
    myStack.push(False)
    print(myStack.size())
    print(myStack.isEmpty())
    myStack.push(98.6)
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.size())

main()
