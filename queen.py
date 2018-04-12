import json

def place(mat,row,col,total):
	#check in row
	for i in range(total):
		if mat[row][i]==1:
			return False
	#check in column
	for i in range(total):
		if mat[i][col]==1:
			return False
	#check in left Digonal
	i=row
	j=col
	while((i>=0) and (j>=0)):
		if mat[i][j]==1:
			return False
		i=i-1
		j=j-1
	#check in right Diagonal
	i=row
	j=col
	while((i>=0) and (j<total)):
		if mat[i][j]==1:
			return False
		i=i-1
		j=j+1		
	return True

def solveNQueen(brd,n,rw):
	if rw==n:
		for i in range(n):
			for j in range(n):
				print str(brd[i][j]) + " ",
			print "\n"
		return True
	#Recursive Call
	#Traversing each column of Specified row
	for pos in range(n):
		if place(brd,rw,pos,n):
			brd[rw][pos]=1
			if(solveNQueen(brd,n,rw+1)):
				return True
			brd[rw][pos]=0
	#Backtracking
	return False

	

#no=int(input("Enter no of queens"))
no=4
with open("input.json") as f:
	data=json.load(f)

board=[[0 for i  in range(no)]for i in range (no)]
board[0][data["Start"]]=1
solveNQueen(board,no,1)
