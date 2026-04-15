class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board)!=9 or len(board[0])!=9:
            return False
        
        block=[['.' for i in range(3)] for i in range(3)]
        # print(row,col,block)
        for r in board:
            row=['.' for i in range(9)]
            for i,element in enumerate(r):
                if element!='.' and element in row:
                    return False
                row[i]=element
        for i in range(9):
            col=['.' for i in range(9)]
            for j in range(9):
                if board[j][i]!='.' and board[j][i] in col:
                    return False
                col[j]=board[j][i]
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                block=[]
                for s in range(3):
                    for k in board[i+s][j:j+3]:
                        if k!='.' and k in block:
                            return False
                        block.append(k)
                    
        return True