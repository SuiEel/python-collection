#  File: htmlChecker.py
#  Description: Checks the tags of an html page
#  Student's Name: William Sears
#  Student's UT EID: wvs92
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/01/2016
#  Date Last Modified: 10/07/2016



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


def getTag(string): #Checks a string for tags
   
      
    tagList = []
    tagFound = False
    tempString = ""
    VALIDTAGS = []
    exceptions = ["br","hr","meta"]

    for character in string:

        if tagFound == True and (character == ">" or character.strip() == ""):
           
            tagFound = False

            if tempString in exceptions: # If it's an exception, ignore it
               print("Tag", '"' + tempString + '"', "does not need to match,  Exceptions:", exceptions)
               tempString = ""


            elif tempString in VALIDTAGS: #if it's already in VALIDTAGS, add it to the list of tags, but not to valid tags
               tagList.append(tempString)
               tempString = ""
                  
            elif tempString[0] != "/": #If it's not in VALIDTAGS, add it 
               print("New tag",'"' +  tempString + '"', "found and added to list of valid tags")
               VALIDTAGS.append(tempString)
               tagList.append(tempString)
               tempString = ""
                  
            else:
               tagList.append(tempString)
               tempString = ""
                  
            
        if tagFound:
            tempString += character

        
        if character == "<":
            tagFound = True
            

        
    print("")   
    #print(VALIDTAGS)
          
    return (tagList, VALIDTAGS, exceptions)
   



def checkTag(alist):
   print("")

   theStack = Stack()
   index = 0
   balanced = True
   opened = False


   for tag in alist: #checks for matches in the stack, pops and pushes when needed, produces an error for unmatching tags
      if "/" in tag:
         if tag[1:] == theStack.peek():
            theStack.pop()
            print("Tag:", tag,  ", matches top of stack. The stack is now:", theStack) 
            
         else:
            print("Error:  tag is", tag, "but top of stack is", theStack.peek())
            exit()
      else: 
         theStack.push(tag)
         print("Tag", tag, "pushed:  stack is now", theStack)


   #while index < len(alist) and balanced:
      
    #  if tag[0] == "/":
     #    if theStack.items[-1] in tag:
      #      theStack.pop()
    #  index += 1
   return theStack
          
      
        




##################################################

def main():
   
   
    txtFile = open("htmlfile.txt", "r")
    fileString = ""

    #theStack = Stack()
    

    for line in txtFile:
        fileString += line

    tagsAndValEx = getTag(fileString)

    tags = tagsAndValEx[0]
    valid = tagsAndValEx[1]
    exceptions = tagsAndValEx[2]

    valid.sort()

    print("")

    print("List of tags:", tags)
    

    theStack = checkTag(tags)
    print("")

    if theStack.items == []:
       print("Processing complete.  No mismatches found.")

    else:
       print("Processing complete.  Unmatched tags remain on stack:",  theStack.items)
       print(theStack)
    print("")
    print ("Valid Tags:", valid)
    print ("Exceptions:", exceptions)
    #print(theStack)

    #print(getTag(fileString))

    #print(fileString)
    txtFile.close()
main()
