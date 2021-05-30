class ttToe:
	"""A simple tic tac toe game."""

	def __init__(self):
		"""Initialising game resources."""
		self.flag = True
		self.player = 0
		self.board =  {
		"top_L" : " ", "top_M" : " ", "top_R" : " ",
		"mid_L" : " ", "mid_M" : " ", "mid_R" : " ",
		"low_L" : " ", "low_M" : " ", "low_R" : " "
		}


	def _printBoard(self):
		"""Helper method to print game board on screen."""
		print(self.board["top_L"] + "|" + self.board["top_M"] + "|" +self.board["top_R"])
		print("-+-+-")
		print(self.board["mid_L"] + "|" + self.board["mid_M"] + "|" +self.board["mid_R"])
		print("-+-+-")
		print(self.board["low_L"] + "|" + self.board["low_M"] + "|" + self.board["low_R"])

	def _emptySlots(self):
		"""Helper method to print empty slots for user to choose from."""
		for key in self.board.keys():
			if self.board[key] == " ":
				print (key)

	def _entries(self):
		"""Helper method to accept user inputs and place pawn accordingly."""
		pos = input("Enter Position :: ")
		if pos in self.board:
			if self.board[pos] == " ":

				#Checking which player's turn it is to place the correct pawn
				self.player = self.player % 2
				if self.player == 0:
					pawn = "x"
				else:
					pawn = "o"
				#Placing pawn in position specified by player
				self.board[pos] = pawn
				self._checkWin()
				self.player += 1
		else:
			print("wrong input")
			self.flag = False

	def _checkWin(self):
		"""Helper method to watch board for winning formations."""

		formations = [
			(self.board["top_R"], self.board["top_M"], self.board["top_L"]),
			(self.board["mid_R"], self.board["mid_M"], self.board["mid_L"]),
			(self.board["low_R"], self.board["low_M"], self.board["low_L"]),
			(self.board["top_R"], self.board["mid_R"], self.board["low_R"]),
			(self.board["top_M"], self.board["mid_M"], self.board["low_M"]),
			(self.board["top_L"], self.board["mid_L"], self.board["low_L"]),
			(self.board["top_R"], self.board["mid_M"], self.board["low_L"]),
			(self.board["top_L"], self.board["mid_M"], self.board["low_R"])
			]
		for line in formations:
			if line[0] == line[1] == line[2] != " ":
				self._printBoard()
				print(f"Player {self.player + 1} is the winner.")
				self.flag = False
			#Moving to next player
			#self.player += 1
	def run(self):
		"""Method to run game's main loop."""
		while self.flag:
			self._printBoard()
			self._emptySlots()
			self._entries()



if __name__ == "__main__":
	game = ttToe()
	game.run()
