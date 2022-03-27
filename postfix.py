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

def calcPostfix(postfixexp):

    stack = Stack()
    tokenlist = postfixexp.split()
    print(tokenlist)

    for token in tokenlist:
        if token in "+*-/":
            op2 = stack.pop()
            op1 = stack.pop()
            if token == "+":
                result = op2 + op1
                stack.push(result)
                print (stack.items)
            elif token == "-":
                result = op2 - op1
                stack.push(result)
                print (stack.items)
            elif token == "*":
                result = op2 * op1
                stack.push(result)
                print (stack.items)
            else:
                result = op2 / op1
                stack.push(result)
                print (stack.items)

        else:
            stack.push(int(token))
            print (stack.items)
    return stack.peek()

def main():

    a = "1 2 3 4 * + +"

    print(calcPostfix(a))

main()
            
            
        
