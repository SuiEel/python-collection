class Node():

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

    def setNext(self, newNext):

        self.next = newNext
    def setPrev(self, newPrev):

        self.prev = newPrev

    def setData (self, newData):

        self.data = newData

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getData(self):

        return self.data


class LinkedList():

    def __init__(self):

        self.head = None
        self.tail = None

    def isEmpty(self):

        return self.head == None

    def add(self, item):

        temp = Node(item)
        temp.setNext(self.head)
        if self.head != None:
            self.head.setPrev(temp)
        self.head = temp
        
        
            
            

        

            



        
    #def addLast(self, item):

            
            

            
            


    def getLength(self):

        current = self.head
        count = 0

        while current != None:

            current = current.getNext()

            count += 1
        return count


    def search(self, item):

        current = self.head
        found = False



        while current != None:

            if current.data == item:
                found = True
                return found
            else:
                current = current.getNext()

        return found


    def remove(self, item):
        current = self.head
        previous = None

        found = False

        while not found:
            if current.getData() == item:
                found = True
            elif current.getNext() != None:
                previous = current
                current = current.getNext()
            else:
                return found
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            

        return found

    def __str__(self):

        listrephead = self.head
        listreptail = self.tail
        listStr = ""
        count = 0

        
            
        if listreptail != None :
            while listreptail != None :
                listreptail = listreptail.getPrev()
                count += 1
            
        if listreptail == None:
            while count > 0:
                listreptail = listreptail.getNext()
                listStr += str(listreptail.data) + " "
                
                count -= 1

        
        while listrephead != None :
            listStr += str(listrephead.data) + " "
            listrephead = listrephead.getNext()
        
            
            
        return listStr
            
        

            
def main():

    listy = LinkedList()
    listy2 = LinkedList()

    a = [1, 2, 5, "A", 6]

    for item in a:
        listy.add(item)
    #for item in a:
    #    listy2.addLast(item)

    
    print (listy)
    #print (listy2)
    print(listy.remove(5))
    print (listy)
    print(listy.remove(7))

    

main()




        
