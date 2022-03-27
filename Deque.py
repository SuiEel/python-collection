class Deque():

    def __init__(self):

        self.items = []

    def addFront(self, item):

        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):

        return len(self.items)

    def peekRear(self):

        return self.items[-1]

    def peekFront(self):

        return self.items[0]

    #def __str__(self):

        

     #   print (self.items)


def main():

    a = 88
    b = "C"
    c = "actually c"
    d = "*"
    e = "eh"


    dek = Deque()

    print(dek.isEmpty())
    dek.addFront(a)
    dek.addFront(e)
    print(dek.isEmpty())
    print(dek.items)

    print("Rear", dek.peekRear())
    print("Front", dek.peekFront())

    dek.addFront(c)

    print(dek.items)

    dek.removeRear()
    print(dek.items)
    dek.addRear(d)
    print("Rear", dek.peekRear())
    print("Front", dek.peekFront())
    print(dek.items)
    dek.addFront(d)
    print("Rear", dek.peekRear())
    print("Front", dek.peekFront())
    print(dek.items)
    



main()
    





    
    
