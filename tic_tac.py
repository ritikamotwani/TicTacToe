import random
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
status = [1,2,3,4,5,6,7,8,9]
flag1 = ' '
flag2 = ' '
chance = random.randint(1,2)
if chance == 1:
	flag1 = 'X'
	flag2 = 'O'
	print("Player 1 is assigned X and player 2 is assigned O")
else:
	flag1 = 'O'
	flag2 = 'X'
	print("Player 1 is assigned O and player 2 is assigned X")
def printBoard(board):
	print("\n\n")
	print(board[0]+'  |  '+board[1]+'  |  '+board[2])
	print('-------------')
	print(board[3]+'  |  '+board[4]+'  |  '+board[5])
	print('-------------')
	print(board[6]+'  |  '+board[7]+'  |  '+board[8])
	print("\n\n")
printBoard(board)
win = 0

print("\n\n")
print("0   |  1  | 2  ")
print("3   |  4  | 5  ")
print("6   |  7  | 8  ")
print("\n\n")
def player1(ch1):

	global win
	global flag1
	global flag2
	global board
	if board[ch1] == ' ':

		board[ch1] = flag1
		if board[0] == flag1 and board[1] == flag1 and board[2] == flag1 :
			win = 1
		if board[0] == flag1 and board[3] == flag1 and board[6] == flag1 :
			win = 1
		if board[2] == flag1 and board[5] == flag1 and board[8] == flag1 :
			win = 1
		if board[1] == flag1 and board[4] == flag1 and board[7] == flag1 :
			win = 1
		if board[3] == flag1 and board[4] == flag1 and board[5] == flag1 :
			win = 1
		if board[6] == flag1 and board[7] == flag1 and board[8] == flag1 :
			win = 1
		if board[0] == flag1 and board[4] == flag1 and board[8] == flag1 :
			win = 1
		if board[2] == flag1 and board[4] == flag1 and board[6] == flag1 :
			win =1

	else :
		print("Invalid Enter again")
		ch1 = int(input())
		player1(ch1)
	

def player2(ch2):
	global win
	global flag1
	global flag2
	global board
	if board[ch2] == ' ':
		board[ch2] = flag2
		if board[0] == flag2 and board[1] == flag2 and board[2] == flag2 :
			win = 2
		if board[0] == flag2 and board[3] == flag2 and board[6] == flag2 :
			win = 2
		if board[2] == flag2 and board[5] == flag2 and board[8] == flag2 :
			win = 2
		if board[1] == flag2 and board[4] == flag2 and board[7] == flag2 :
			win = 2
		if board[3] == flag2 and board[4] == flag2 and board[5] == flag2 :
			win = 2
		if board[6] == flag2 and board[7] == flag2 and board[8] == flag2 :
			win = 2
		if board[0] == flag2 and board[4] == flag2 and board[8] == flag2 :
			win = 2
		if board[2] == flag2 and board[4] == flag2 and board[6] == flag2 :
			win = 2
		
	else :
		print("Invalid Enter again")
		ch2 = int(input())
		player1(ch2)
	

while win == 0:
	print("Player 1 enter the position ")
	ch1 = int(input())
	player1(ch1)
	printBoard(board)
	
	if win == 1:
		print("Player 1 wins")
		break
	if win == 2:
		print("Player 2 wins")
		break
	g = 0
	for i in board :
		if i == ' ':
			g = 1
	if g == 0:
		print("Match Draw")
		break
		
	print("Player 2 enter the position")
	ch2 = int(input())
	player2(ch2)
	printBoard(board)
	if win == 1:
		print("Player 1 wins")
	if win == 2:
		print("Player 2 wins")
	g = 0
	for i in board :
		if i == ' ':
			g = 1
	if g == 0:
		print("Match Draw")
		break