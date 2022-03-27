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

   def __str__(self):

      return str(self.items)



##################################################


def getTag(string):

    tagList = []
    tagFound = False
    tempString = ""

    for character in string:

        if character == ">":
            tagFound = False
            tagList.append(tempString)
            tempString = ""

        if tagFound:
            tempString += character

        
        if character == "<":
            tagFound = True

        
        

            
    return tagList



def checkTag(alist):

   theStack = Stack()
   index = 0
   balanced = True
   


   for tag in alist:
      if tag[0] != "/":
         theStack.push(tag)
   print(theStack)


   while index < len(alist) and balanced:
      
      if tag[0] == "/":
         if theStack.items[-1] in tag:
            theStack.pop()
      index += 1
   return theStack
          
      
        




##################################################

def main():

    txtFile = open("htmlfile.txt", "r")
    fileString = ""

    #theStack = Stack()

    for line in txtFile:
        fileString += line

    

    tags = getTag(fileString)

    theStack = checkTag(tags)

    print(tags)

    print(theStack)

    #print(getTag(fileString))

    #print(fileString)

main()
