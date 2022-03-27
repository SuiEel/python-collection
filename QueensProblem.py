class QueensProblem():

    def __init__(self, numSquares):

        self.board = []
        squares = numSquares

        while squares > 0:
            tempsquares = numSquares
            temp = []

            while tempsquares > 0:

                temp.append("*")
                tempsquares -= 1
            self.board.append(temp)
            squares -= 1
        
        
                
        

    def __str__(self):

        repre = ""
        for i in self.board:
            temp = ""
            for j in i:
                temp += str(j) + " "
            repre += temp + "\n"
            
        return repre
        

    def isValidPlace(self, row, col):

        valid = False

        rowCount = 0

        hasQ = False

        print("Testing for a row of:", row, "and column of:", col)
        

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
            print("South east check")
            while diagRow < (len(self.board) - 1) and diagCol < (len(self.board) -1):
                diagRow += 1
                diagCol += 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False
            diagRow = row
            diagCol = col
            #print(diagRow, diagCol)
            
            #North East Check (-, +)
            print("North East Check")
            while diagRow > 0 and diagCol < (len(self.board) -1):
                diagRow -= 1
                diagCol += 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False

                
            diagRow = row
            diagCol = col
            #print(diagRow, diagCol)
            #North West Check (-, -)
            print("North West Check")
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
            print("South West Check")
            while diagRow < (len(self.board) - 1) and diagCol > 0:
                diagRow += 1
                diagCol -= 1
                #print(diagRow, diagCol)
                if self.board[diagRow][diagCol] == "Q":
                    return False 
        

        

        print("Success")
        

        return True
                
                

        
        


    def solve(self, n):
        
        if n == 0:
            
            return self

        failedValid = False
        valid = False
        
        if "Q" in self.board[n - 1]:
            print("Failed Valid")
            failedValid = True
        
        
        for i in range(len(self.board[n - 1])):
            if failedValid:
                if self.board[n - 1][i] == "Q":
                    self.board[n - 1][i] = "*"
                    print(self)
                    if i + 1 <= (len(self.board[n - 1]) - 1) :
                        #print ("i", i)
                        valid = self.isValidPlace(n - 1, i + 1)
                        if valid:
                            self.board[n - 1][i + 1] = "Q"
                            return self.solve(n - 1)
                    else:
                        #print ("i", i)
                        valid = self.isValidPlace(n - 1, 0)
                        if valid:
                            self.board[n - 1][0] = "Q"
                            return self.solve(n - 1)
          
            else:
                valid = self.isValidPlace(n - 1, i)
                #print ("i", i)
                if valid:
                    self.board[n - 1][i] = "Q"
                    print(self)
                    return self.solve(n - 1)
        if not valid:
            return self.solve(n + 1)
                
            

        return False
                    
            

        

def main():
    

    squares = int(input("Input a number above 4: "))
    while squares < 4:
        squares = int(input("Input a number above 4: "))

    qProblem = QueensProblem(squares)
    print(qProblem)
    print(qProblem.solve(squares))
    
    

main()
    
