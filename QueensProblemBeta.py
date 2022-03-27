class QueensProblem():

    def __init__(self, numSquares):

        self.board = []
        self.num = numSquares
        squares = numSquares
        self.solutions = []
        self.count = 0

        while squares > 0:
            tempsquares = numSquares
            temp = []

            while tempsquares > 0:

                temp.append("*")
                tempsquares -= 1
            self.board.append(temp)
            squares -= 1
        
        
                
        

    def __str__(self):

        answer = ""
        count = 0
        for i in self.solutions:
            #print (i)
            count += 1

            answer += "Solution: " + str(count) + "\n" + "\n"
            
            for j in i:
                temp = ""
                for q in j:
                    temp += str(q) + " "
                answer += temp + "\n"
            answer += "\n"
        return answer
        

    def isValidPlace(self, row, col):

        valid = False

        rowCount = 0

        hasQ = False

        #print("Testing for a row of:", row, "and column of:", col)
        

        for i in range (len(self.board)):
            
            colCount = 0
            if "Q" in self.board[i]:
                #print(i)
                hasQ = True
                if i == row:
                    return False
                else:
                    for j in range (len(self.board[i])):
                        
                        if self.board[i][j] == "Q":
                            
                            if j == col:
                                return False
                            
                        
                
        if hasQ:

            diagRow = row
            diagCol = col
            #print(diagRow, diagCol)

            #South east check (+, +)
       #     print("South east check")
            while diagRow < (len(self.board) - 1) and diagCol < (len(self.board) -1):
                diagRow += 1
                diagCol += 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False
            diagRow = row
            diagCol = col
        #    print(diagRow, diagCol)
            
            #North East Check (-, +)
         #   print("North East Check")
            while diagRow > 0 and diagCol < (len(self.board) -1):
                diagRow -= 1
                diagCol += 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False

                
            diagRow = row
            diagCol = col
          #  print(diagRow, diagCol)
            #North West Check (-, -)
           # print("North West Check")
            while diagRow > 0 and diagCol > 0:
                diagRow -= 1
                diagCol -= 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False

            diagRow = row
            diagCol = col
            #print(diagRow, diagCol)
            #South West Check (+, -)
         #   print("South West Check")
            while diagRow < (len(self.board) - 1) and diagCol > 0:
                diagRow += 1
                diagCol -= 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False 
        

        

        #print("Success")
        

        return True
                
                

        
        


    def solve(self, col):
        if col == self.num:
            self.count +=1
            #temp boards    
            temp = []
        
            for i in range(len(self.board)):
                temp.append(self.board[i][:])

            self.solutions.append(temp)
            return

        for row in range(self.num):
            if self.isValidPlace(row, col):
                self.board[row][col] = "Q"
                self.solve(col + 1)
                self.board[row][col] = "*"

        return self.count
                
                
        
        

        

                
                    
            

        

def main():
    

    squares = int(input("Input a number above 4: "))
    while squares < 4:
        print("Invalid input")
        squares = int(input("Input a number above 4: "))

    qProblem = QueensProblem(squares)
    #print(qProblem)
    print()
    qProblem.solve(0)
    print (qProblem)
    
    

main()
    
