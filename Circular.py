#  File: Circular.py
#  Description: Runs through a text and simulates "Hot potato"
#  Student's Name: William Sears
#  Student's UT EID: wvs92
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/24/2016
#  Date Last Modified: 10/28/2016




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


    def __init__ (self):
       sentinel = Node(None)
       self.head = sentinel
       self.head.setNext(self.head)

    def add (self,item):
       current = self.head.next
       temp = Node(item)
       temp.setNext(self.head)

       if current != self.head:
          while current.next != self.head:
             current = current.getNext()
          current.setNext(temp)

       else:
          self.head.setNext(temp)
          
          
          
          
       
          


 
       


       
    def remove (self, rounds, players): #removes based on the number of rounds
       previous = self.head

       if previous.data == None:
          previous = self.head
          self.head = self.head.next
       count = 1
       
       
          
          
       
       
       
       while rounds != count:
          #print("hi")
          #print(previous.data)
          
          #print (self.head.data)


      
          #print()
          if previous.next.data == None:
             previous.setNext(self.head.getNext())
             self.head = previous.next
          

          previous = self.head   

          self.head = self.head.next

          
           
          
          

             

          #print(previous.data)
          
          #print (self.head.data)
          count += 1
          #print (count, rounds)
       if self.head.data == None:
          print(self.head.next.data, "Will be removed")
          previous.setNext(self.head.next.getNext())
          self.head = previous.next
          print()
       else:
          print(self.head.data, "Will be removed")
          previous.setNext(self.head.getNext())
          self.head = previous.next
          print()
       
          #if self.head.data == None:
             #count -= 1



          
             
          
             
             
       
       #print()
       #print(previous.data)
       #print (self.head.data)
          
       
       

       
       
       

       
   
    def isEmpty (self):
       return self.head.getNext() == None

    def onlyOneNode (self):
       if self.head.getNext() == self.head:
          return True
       else:
          return False
        
        
        

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
            if repre.getData () != None:
               strrepre += repre.getData() + "  "
               pCount += 1
            repre = repre.getNext()
            
            if( repre == self.head) :
               break
            
               
            
        return strrepre


    def getLength(self):
       current = self.head.getNext()
       count = 0
      
       while current != self.head:
          count += 1
          current = current.getNext()
            
       return count
        

def main():

    txtFile = open("HotPotatoData.txt", "r")
    numPeople = ""
    hitNumber = ""
    space = False
    digitFound = False
    funBegins = False
    
    for item in txtFile:
        item = item.strip('\n')
        
        if item[0].isdigit():
            players = CircularList()
            playerCount = 0
            digitFound = True
            
            tempnumPeople = ""
            temphitNumber = ""
            for letter in item:
                if not space:
                    if not letter.isdigit():
                        space = True
                    else:
                        tempnumPeople += letter
                else:
                    temphitNumber += letter
                    
        else:
            #print(players)
            if digitFound:
               
               numPeople = int(tempnumPeople)
               hitNumber = int(temphitNumber)
               #print(numPeople, hitNumber)
               digitFound = False
               playerCount += 1
               players.add(item)
            else:
               playerCount += 1
               space = False
               players.add(item)
               if playerCount == numPeople:
                  print(players)
                  print(players.getLength())
                  print()
                  print()
                  itNum = 0
                  while players.getLength() > 0:
                     itNum += 1
                     
                     print("Iteration:", itNum)
                     print("Current players:", players)
                     players.remove(hitNumber, numPeople)

                     
                     
                     
                     print("Only one?", players.onlyOneNode())
                     print()
                  print()
                  print()

                  print("The sole survivor is:", players)
                  print(players.onlyOneNode())
                  #exit()
                  
                  print()
                  print()
                  #while players.getLength() > 1:
                     
                   #  players.remove(hitNumber, numPeople)
                    # print(players)
                     #playerCount -= 1
                     #print(playerCount)
                     
                     

                     
                     
                     

               
            
            #print(numPeople, hitNumber)
            
    #print(players)
         

    

main()
