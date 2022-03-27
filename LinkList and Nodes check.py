class Node():

    def __init__(self, data):

        self.data = data
        self.next = None

    def setNext(self, newNext):

        self.next = newNext

    def setData (self, newData):

        self.data = newData

    def getNext(self):
        return self.next

    def getData(self):

        return self.data


class LinkedList():

    def __init__(self):

        self.head = None

    def isEmpty(self):

        return self.head == None

    def add(self, item):
        #adds a new node to beginning of a list

        temp = Node(item)

        temp.setNext(self.head)

        self.head = temp

        
    def addLast(self, item):

        temp = Node(item)

        current = self.head

        if current != None:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)

        else:
            self.head = temp
            


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

        listrep = self.head
        listStr = ""

        while listrep != None:
            listStr += str(listrep.data) + " "

            listrep = listrep.getNext()
            
            
        return listStr
            
        

            
def main():

    listy = LinkedList()
    listy2 = LinkedList()

    a = [1, 2, 5, "A", 6]

    for item in a:
        listy.add(item)
    for item in a:
        listy2.addLast(item)

    
    print (listy)
    print (listy2)
    print(listy.remove(5))
    print (listy)
    print(listy.remove(7))

    

main()




        
