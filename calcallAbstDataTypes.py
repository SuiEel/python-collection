class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)


    
def sumUp(items):
   theStuff = items
   addNum = 0

   if len(theStuff) == 0:
      return addNum
   else:
      addNum += theStuff[0]
      return addNum + sumUp(theStuff[1:])


def main():

    stuffToAdd = "123456789"
    dataType = Stack()
    

    for i in stuffToAdd:
        dataType.push(int(i))

    print(sumUp(dataType.items))

main()

    
        
