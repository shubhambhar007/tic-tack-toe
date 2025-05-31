class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

class Board:
    def __init__(self, size):
        self.reset(size)

    def reset(self,size):
        self.size = size
        self.board = [["" for i in range(size)] for j in range(size)]
        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.size = size

    def place(self,player,x,y):
        marker=player.marker
        if self.board[x][y]!='':
            raise Exception("Cell already occupied")
        else:
            self.board[x][y]=marker

            self.rowCounts[x]=self.rowCounts.get(x,{})
            self.rowCounts[x][marker]=self.rowCounts[x].get(marker,0)+1

            if self.rowCounts[x][marker]==self.size:
                return True
            
            self.colCounts[y]=self.colCounts.get(y,{})
            self.colCounts[y][marker]=self.colCounts[y].get(marker,0)+1

            if self.colCounts[y][marker]==self.size:
                return True
            
            if x==y:
                self.diagCounts["forwards"]=self.diagCounts.get("forwards",{})
                self.diagCounts["forwards"][marker]=self.diagCounts["forwards"].get(marker,0)+1

                if self.diagCounts["forwards"][marker]==self.size:
                    return True
                
            if x+y==self.size-1:
                self.diagCounts["backwards"]=self.diagCounts.get("backwards",{})
                self.diagCounts["backwards"][marker]=self.diagCounts["backwards"].get(marker,0)+1

                if self.diagCounts["backwards"][marker]==self.size:
                    return True
            return False

class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def playGame(self):
        curTurn=1
        gameDone=False
        while not gameDone:
            currPlayer=self.player1 if curTurn%2==1 else self.player2
            print(f"{currPlayer.name}'s turn")
            x=int(input("Enter x coordinate: "))
            y=int(input("Enter y coordinate: "))
            if self.board.place(currPlayer, x, y):
                print(f"{currPlayer.name} wins!")
                gameDone=True
            else:
                curTurn+=1
                printer(board)
    
def printer(board):
    for row in board.board:
        print(" | ".join([cell if cell else " " for cell in row]))
        print("-" * (board.size * 4 - 1))
    print()

# Example usage
# Create players, board, and game
jordan=Player("Jordan", "x")
shubham=Player("Shubham", "o")
board=Board(3)
game=Game(jordan,shubham,board)

game.playGame()