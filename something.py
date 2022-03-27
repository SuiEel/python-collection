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

class CircularList():

    def __init__(self):

        self.head = None

    def add(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.head.setNext(self.head)
        else:
            temp.setNext(self.head.next)
            self.head.setNext(temp)
    
    def __str__ (self):
        repre = self.head
        pCount = 0
        strrepre = ""
        

        while True:
            
            if pCount == 10:
                strrepre += "\n"
                pCount = 0
            #if repre.getData() in itemCheck:
               #allCounted = True
           
            #itemCheck.append(repre.getData())
            #print (repre.data)
            if repre.getData () != self.head.data:
               strrepre += repre.getData() + "  "
               pCount += 1
            repre = repre.getNext()
            
            
            if( repre == self.head) :
               break
            
               
            
        return strrepre
        

def main():
    listy = CircularList()
    count = 0

    for i in range (10):
        
        
        listy.add(str(count))
        
        count += 1
    print(listy)

main()

        

    
