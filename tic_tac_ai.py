import random
import  time
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
status = [0,1,2,3,4,5,6,7,8]

flag1 = ' '
flag2 = ' '
def printBoard(board):
		print("\n\n")
		print(board[0]+'  |  '+board[1]+'  |  '+board[2])
		print('-------------')
		print(board[3]+'  |  '+board[4]+'  |  '+board[5])
		print('-------------')
		print(board[6]+'  |  '+board[7]+'  |  '+board[8])
		print("\n\n")

printBoard(board)
chance = random.randint(1,2)
if(chance == 1):
	flag1 = 'X'
	flag2 = 'O'
else:
	flag1 = 'O'
	flag2 = 'X'
print("User has got "+ flag1)
count = 0
def smart(board):
	cpos = random.choice(status)
	if(board[0]==board[1]==flag2 and board[2]==' '):
		cpos=2
	elif(board[1]==board[2]==flag2 and board[0]==' '):
		cpos = 0
	elif(board[0]==board[2]==flag2 and board[1]==' '):
		cpos = 1
	elif(board[3]==board[4]==flag2 and board[5]==' '):
		cpos = 5
	elif(board[4]==board[5]==flag2 and board[3]==' '):
		cpos = 3
	elif(board[3]==board[5]==flag2 and board[4]==' '):
		cpos = 4
	elif(board[6]==board[7]==flag2 and board[8]==' '):
		cpos = 8
	elif(board[7]==board[8]==flag2 and board[6]==' '):
		cpos = 6
	elif(board[6]==board[8]==flag2 and board[7]==' '):
		cpos = 7
	elif(board[0]==board[3]==flag2 and board[6]==' '):
		cpos = 6
	elif(board[3]==board[6]==flag2 and board[0]==' '):
		cpos = 0
	elif(board[0]==board[6]==flag2 and board[3]==' '):
		cpos = 3
	elif(board[1]==board[4]==flag2 and board[7]==' '):
		cpos = 7
	elif(board[4]==board[7]==flag2 and board[1]==' '):
		cpos = 1
	elif(board[1]==board[7]==flag2 and board[4]==' '):
		cpos = 4
	elif(board[2]==board[5]==flag2 and board[8]==' '):
		cpos = 8
	elif(board[5]==board[8]==flag2 and board[2]==' '):
		cpos = 2
	elif(board[2]==board[8]==flag2 and board[5]==' '):
		cpos = 5
	elif(board[0]==board[4]==flag2 and board[8]==' '):
		cpos = 8
	elif(board[4]==board[8]==flag2 and board[0]==' '):
		cpos = 0
	elif(board[0]==board[8]==flag2 and board[4]==' '):
		cpos = 4
	elif(board[2]==board[4]==flag2 and board[6]==' '):
		cpos = 6
	elif(board[4]==board[6]==flag2 and board[2]==' '):
		cpos = 2
	elif(board[2]==board[6]==flag2 and board[4]==' '):
		cpos = 4
	else:
		cpos = random.choice(status)
	
	
	board[cpos]=flag2
	status.remove(cpos)

def check(board):
	if(board[0]==board[1]==board[2]!=' '):
		if(board[1]==flag1):
			return 1
		else:
			return 2
	elif(board[3]==board[4]==board[5]!=' '):
		if(board[4]==flag1):
			return 1
		else:
			return 2
	elif(board[6]==board[7]==board[8]!=' '):
		if(board[7]==flag1):
			return 1
		else:
			return 2
	elif(board[0]==board[3]==board[6]!=' '):
		if(board[0]==flag1):
			return 1
		else:
			return 2
	elif(board[1]==board[4]==board[7]!=' '):
		if(board[1]==flag1):
			return 1
		else:
			return 2
	elif(board[2]==board[5]==board[8]!=' '):
		if(board[2]==flag1):
			return 1
		else:
			return 2
	elif(board[0]==board[4]==board[8]!=' '):
		if(board[0]==flag1):
			return 1
		else:
			return 2
	elif(board[2]==board[4]==board[6]!=' '):
		if(board[2]==flag1):
			return 1
		else:
			return 2
	else:
		return 3
while(True):
	
	print("Enter the position")
	pos = int(input())
	if pos not in status :
		print("Invalid Position ")
		continue
	if board[pos] == ' ':
		board[pos] = flag1
		count = count + 1
		status.remove(pos)
		printBoard(board)
		if(check(board) == 1 or check(board) == 2):
			break
	else:
		print("Invalid Position")
		continue
	if(count == 9):
		break
	print("Computer's Turn")
	smart(board)
	count = count + 1
	printBoard(board)
	if(check(board) == 1 or check(board) == 2):
		break

if(check(board) == 1):
	print("You Win :D")
elif(check(board) == 2):
	print("You lose :(")
else:
	print("Draw :P")