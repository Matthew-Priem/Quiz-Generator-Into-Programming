player1 = input("Player 1 choice: ")
player2 = input("Player 2 choice: ")

if player1 == player2:
	print("It's a tie!")
elif (player1 == 'Rock' and player2 == 'Paper') or \
		(player1 == 'Paper' and player2 == 'Scissors') or \
		(player1 == 'Scissors' and player2 == 'Rock'):
	print('player 2 wins!')

else:
	print('player 1 wins!')


