
import sys,copy
from termcolor import colored, cprint

colors = {
    0:'grey',
    1:'red',
    2:'magenta',
    3:'yellow',
    4:'blue',
    5:'green',
    6:'cyan',
    7:'white',
}
back_colors = {
    0:'on_grey',
    1:'on_red',
    2:'on_magenta',
    3:'on_yellow',
    4:'on_blue',
    5:'on_green',
    6:'on_cyan',
    7:'on_white',
}

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.cc = 0
        self.res = float('inf')
        board = [[0]*m for i in range(n)]
        self.ans = []

        def print_board():
            for row in board:
                print(row)
            print(' ')
            return

        def find_max_length(i, j):
            max_length = 1
            while i + max_length -1 < n and j + max_length - 1 < m:
                for row in range(i, i + max_length):
                    if board[row][j + max_length - 1] != 0:
                        return max_length - 1
                for col in range(j, j + max_length):
                    if board[i + max_length - 1][col] != 0:
                        return max_length - 1
                max_length += 1
            return max_length - 1
         
        def find_start(i0,j0):
            start = i0*m+j0
            for cur in range(start,m*n):
                    i,j = divmod(cur,m)
                    if board[i][j]==0:
                        return i,j
            return -1,-1
        
        def assert_board(ii,jj,e):
            i,j = -1,-1
            for i in range(ii,ii+e):
                for j in range(jj,jj+e):
                    if i<0 or i>=n or j<0 or j>=m or board[i][j]!=0:
                        return 0,i,j
                    else:
                        board[i][j]=(e,self.cc)
            self.cc+=1
            return 1,i,j+1
        
        def dessert_board(ii,jj,e,it,jt):
            for i in range(ii,ii+e):
                for j in range(jj,jj+e):
                    if (i,j)==(it,jt):
                        return
                    else:
                        board[i][j]=0
            return
            
        def fill_board(i0,j0,cnt):
            if cnt>=self.res:
                return
            
            ii,jj = find_start(i0,j0)    
            
            if (ii,jj)==(-1,-1):
                if cnt<self.res:
                    self.res = cnt
                    self.ans = copy.deepcopy(board)
                return
            
            max_len = find_max_length(ii,jj)
            for i in range(max_len,0,-1):
                valid,it,jt = assert_board(ii,jj,i)
                if valid:
                    fill_board(ii+jt//m,jt%m,cnt+1)
                dessert_board(ii,jj,i,it,jt)
            return
        
        fill_board(0,0,0)
        print(f'Input rectangle is {n} x {m}\n')
        print(f'Minimum number of squres needed is {self.res}\n')
        self.print_ans()
        print(' ')
        return self.res

    def print_ans(self):
        for row in self.ans:
            for n,c in row:
                cprint('{:3} '.format(n),colors[(c+3)%7],back_colors[(c+2)%7],end='')
            print()
        return

if __name__=='__main__':
    n,m = int(sys.argv[1]),int(sys.argv[2])
    s = Solution()
    s.tilingRectangle(n,m)
