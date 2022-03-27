#  File: ERsim.py
#  Description: Simulates a treatment queue in an ER
#  Student's Name: William Sears
#  Student's UT EID: wvs92
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 10/09/2016
#  Date Last Modified: 10/14/2016


class Queue:

    def __init__(self):
        self.items = [ ]

    def enqueue(self, item):

        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
#
 #   def enqueue(self, item):
  #      self.items.insert(0, item)

   # def dequeue(self):

    #    return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):

        return self.items[0]

    def __str__(self):

        return str(self.items)

    
def addPatient():       #Add patients to the queue
    
    critical = Queue()
    serious = Queue()
    fair = Queue()

    txtFile = open("ERsim.txt", "r")

    
    fileList = txtFile.readlines()
    
    
        
    

    
    nameString = ""

    for item in fileList:
        #print (item)
        
        

        if "add" in item:
            print()
            
            #if fair condition
            if "Fair" in item:
                for letter in item[3:]:
                    nameString += letter
                    if letter == ".":
                        
                        fair.enqueue(nameString)
                        nameString = ""
                        print(">>> Add patient", fair.items[0], "to fair queue")
                        print()
                        print("   Queues are:")
                        print("   Critical", critical)
                        print("   Serious ", serious)
                        print("   Fair    ", fair)
                        
                        break
                                    
                    
            #if serious condition
            elif "Serious" in item:
                for letter in item[3:]:
                    nameString += letter
                    if letter == ".":
                        serious.enqueue(nameString)
                        nameString = ""
                        print(">>> Add patient", serious.items[0], "to serious queue")
                        print()
                        print("   Queues are:")
                        print("   Critical", critical)
                        print("   Serious ", serious)
                        print("   Fair    ", fair)
                        break
                
               
            #if critical condition
            elif "Critical" in item:
                for letter in item[3:]:
                    nameString += letter
                    if letter == ".":
                        critical.enqueue(nameString)
                        nameString = ""
                        print(">>> Add patient", critical.items[0], "to critical queue")
                        print()
                        print("   Queues are:")
                        print("   Critical", critical)
                        print("   Serious ", serious)
                        print("   Fair    ", fair)
                        break


                    
            #print("fair:", fair)
            #print("Serious:", serious)
            #print("critical:", critical)
            
                
                
        #Treat patients based on conditions
        elif "treat" in item:
            
            if "all" in item:
                print()
                print(">>>Treat all patients")
                print()
                while critical.isEmpty() == False:
                    
                    print("   Treating", critical.peek(), "from critical queue")
                    critical.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    print()
                    
                
                while serious.isEmpty() == False:
                    
                    print("   Treating", serious.peek(), "from serious queue")
                    serious.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    print()
                    
                    
                while fair.isEmpty() == False:
                    
                    print("   Treating", fair.peek(), "from fair queue")
                    fair.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    print()
                if serious.isEmpty() and fair.isEmpty() and critical.isEmpty():
                    print("   No patients in queues")
                    
                #print("fair all treated:", fair)
                #print("Serious all treated:", serious)
                #print("critical all treated:", critical)
                
            elif "Serious" in item:
                print()
                print(">>>Treat all patients in serious condition")
                print()
                if serious.isEmpty() == False:

                    
                    print("   Treating", serious.peek(), "from serious queue")
                    serious.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    
                    
                    
            elif "Critical" in item:
                print()
                print(">>>Treat all patients in critcal condition")
                print()
                if critical.isEmpty() == False:

                    print("   Treating", critical.peek(), "from critical queue")
                    critical.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    
                    
            elif "Fair" in item:
                print()
                print(">>>Treat all patients in fair condition")
                print()
                if fair.isEmpty() == False:

                    print("   Treating", fair.peek(), "from fair queue")
                    fair.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                    

                    
                
            else:
                print()
                print(">>> Treat next patient")
                print()
                if critical.isEmpty() == False:
                    
                    print("   Treating", critical.peek(), "from critical queue")
                    critical.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)

                    
                    
                elif serious.isEmpty() == False:
                    
                    print("   Treating", serious.peek(), "from serious queue")
                    serious.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)

                    
                elif fair.isEmpty() == False:

                    print("   Treating", fair.peek(), "from fair queue")
                    fair.dequeue()
                    print("   Queues are:")
                    print("   Critical", critical)
                    print("   Serious ", serious)
                    print("   Fair    ", fair)
                
                else: # No patients left
                    print("   No patients in queue")
                    
                
        else:
            exit()

    #print("fair final:", fair)
    #print("Serious final:", serious)
    #print("critical final:", critical)
    

    
                
            

    


    
def main():

    
    addPatient()
    txtFile.close()

    
main()    
