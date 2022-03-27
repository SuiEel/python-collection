#  File: LinkedLists.py
#  Description: Tests methods of a linked list object
#  Student's Name: William Sears
#  Student's UT EID: ---
#  Course Name: CS 313E 
#  Unique Number: ---
#
#  Date Created: 10/17/2016
#  Date Last Modified: 10/21/2016

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





class LinkedList():
   
   def __init__(self):
      self.head = None
        


   def __str__(self):

      repre = self.head
      pCount = 0
      strrepre = ""

      while repre != None:
         if pCount == 10:
            strrepre += "\n"
            pCount = 0
         strrepre += repre.getData() + "  "
         repre = repre.getNext()
         pCount += 1
      return strrepre




   def addFirst(self, item):
        
      # add a new Node to the beginning of an existing list
      temp = Node(item)
      temp.setNext(self.head)
      self.head = temp







      




   def addLast(self, item):
      current = self.head
      if current:
         while current.getNext() != None:
            current = current.getNext()
         current.setNext(Node(item))
      else:
         self.head = Node(item)










         

         
   def addInOrder (self, item):
      current = self.head
      previous = None
      stop = False

      while current != None and not stop:
         if current.getData() > item:
            stop = True
         else:
            previous = current
            current = current.getNext()

      temp = Node(item)
      if previous == None:
         temp.setNext(self.head)
         self.head = temp
      else:
         temp.setNext(current)
         previous.setNext(temp)










         
         
   def findUnordered (self, item):
      
      current = self.head
      found = False

      while current != None and not found:
         if current.getData() == item:
            found = True
         else:
            current = current.getNext()

      return found










   


   def findOrdered (self, item):
      current = self.head
      found = False
      stop = False
      while current != None and not found and not stop:
         if current.getData() == item:
            found = True
         else:
            if current.getData() > item:
               stop = True
            else:
               current = current.getNext()

      return found











   

   def delete (self, item):
      
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         elif current.next != None:
            previous = current
            current = current.getNext()
         else:
            return found

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )

      return found









   
   
   def remove (self,item):
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )







         
   
   def copyList (self):

      mainlist = self.head

      copylist = LinkedList()

      done = False

      while not done:
         if mainlist.next == None:
            done = True
         copylist.addLast(mainlist.getData()) 
         mainlist = mainlist.getNext()
         
          
      return copylist








   

   def reverseList (self):
      
      mainlist = self.head

      copylist = LinkedList()

      done = False

      while not done:
         if mainlist.next == None:
            done = True
         copylist.addFirst(mainlist.getData()) 
         mainlist = mainlist.getNext()
         
          
      return copylist







   
   

   def orderList (self):
      mainlist = self.head

      copylist = LinkedList()

      done = False

      while not done:
         if mainlist.next == None:
            done = True
         copylist.addInOrder(mainlist.getData()) 
         mainlist = mainlist.getNext()
         
          
      return copylist









   

   def isOrdered (self):
      current = self.head.getNext()
      ordered = True
      previous = self.head
   
      while current != None and ordered:

            if current.getData() > previous.getData():

               previous = current
               
               current = current.getNext()
            else:
               ordered = False
               

      return ordered







   

   
   def isEmpty(self):
      return self.head == None



   




   def getLength(self):
      current = self.head
      count = 0
      while current != None:
         count += 1
         current = current.getNext()
            
      return count







   
   def mergeList (self, b):
      current = self.head

      current2 = b.head

      copylist = LinkedList()


      done = False

      while not done:
         if current.next == None:
            done = True
         copylist.addInOrder(current.getData()) 
         current = current.getNext()

      done = False

      while not done:
         if current2.next == None:
            done = True
         copylist.addInOrder(current2.getData()) 
         current2 = current2.getNext()

      return copylist






   

   def isEqual (self, b):

      current = self.head
      currenta = current
      
      current2 = b.head
      currentb = current2
      
      done = False

      count = 0
      count2 = 0
      while currenta != None:
         count += 1
         currenta = currenta.getNext()
      while currentb != None:
         count2 += 1
         currentb = currentb.getNext()
      

      if count == count2:
         while not done:
            if current == None:
               done = True
               return True
            if current.getData() == current2.getData():
               current = current.getNext()
               current2 = current2.getNext()
            else:
               return False
               

      else:
         return False






      

   def removeDuplicates (self):
      elemList = []
      elemList2 = []
      copylist = LinkedList()
      

      current = self.head

      while current != None:
         if current.getData() not in elemList:
            elemList.append(current.getData())
            current = current.getNext()
         else:
            current = current.getNext()
      #print (elemList)
      for i in elemList:
         if i in elemList2:
            pass
            
         else:
            elemList2.append(i)
      #print (elemList2)

      for i in elemList2:

         copylist.addLast(i)
      return copylist
      
            
            
         
         

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
