class Game:
	def __init__(self):
		self.player_1_score = 0
		self.player_2_score = 0
		self.player_1_sets = 0
		self.player_2_sets = 0
		self.player_1_games = 0
		self.player_2_games = 0
		self.is_tie_break = False
		self.is_player_1_serving = True
		self.is_game_over = False
		self.points = ["0", "15", "30", "40"]
		self.was_player_1_serving_before_tie_break = False

	def is_game_over(self):
		return self.is_game_over

	def won_point(self):
		if self.is_game_over:
			return

		if self.is_player_1_serving:
			self.player_1_score += 1
		else:
			self.player_2_score += 1
		self.handle_score()

	def lost_point(self):
		if self.is_game_over:
			return

		if self.is_player_1_serving:
			self.player_2_score += 1
		else:
			self.player_1_score += 1
		self.handle_score()

	def handle_score(self):
		if self.is_game_over:
			return

		if self.is_tie_break:
			if self.check_if_anyone_has_won_the_tie_break_and_adjust_it():
				if self.check_if_anyone_has_won_the_set_and_adjust_it():
					if self.check_if_anyone_has_won_the_match():
						return
					else:
						self.player_1_games = 0
						self.player_2_games = 0
						self.player_1_score = 0
						self.player_2_score = 0
						self.is_tie_break = False

						if self.was_player_1_serving_before_tie_break:
							self.is_player_1_serving = False
						else:
							self.is_player_1_serving = True
				self.change_sides()
			else:
				if self.player_1_score + self.player_2_score == 1:
					self.change_sides()
				elif self.player_1_score + self.player_2_score > 1 and (self.player_1_score + self.player_2_score) % 2 != 0:
					self.change_sides()
		else:
			if self.check_if_anyone_has_won_the_game_and_adjust_it():
				if self.check_if_anyone_has_won_the_set_and_adjust_it():
					if self.check_if_anyone_has_won_the_match():
						return
					else:
						self.player_1_games = 0
						self.player_2_games = 0
						self.player_1_score = 0
						self.player_2_score = 0
						self.is_tie_break = False
				else:
					self.player_1_score = 0
					self.player_2_score = 0
				self.change_sides()

	def change_sides(self):
		self.is_player_1_serving = not self.is_player_1_serving

	def check_if_anyone_has_won_the_game_and_adjust_it(self):
		if (self.player_1_score >= 4 or self.player_2_score >= 4) and abs(self.player_1_score - self.player_2_score) >= 2:
			if self.player_1_score > self.player_2_score:
				self.player_1_games += 1
			else:
				self.player_2_games += 1
			return True
		return False

	def check_if_anyone_has_won_the_tie_break_and_adjust_it(self):
		if (self.player_1_score >= 7 or self.player_2_score >= 7) and abs(self.player_1_score - self.player_2_score) >= 2:
			if self.player_1_score > self.player_2_score:
				self.player_1_games += 1
			else:
				self.player_2_games += 1
			return True
		return False

	def does_anyone_won_the_set(self):
		return (self.player_1_games == 7 or self.player_2_games == 7
				or ((self.player_1_games == 6 or self.player_2_games == 6) and abs(self.player_1_games - self.player_2_games) >= 2))

	def check_if_anyone_has_won_the_set_and_adjust_it(self):
		if self.does_anyone_won_the_set():
			if self.player_1_games > self.player_2_games:
				self.player_1_sets += 1
			else:
				self.player_2_sets += 1
			return True
		elif self.player_1_games == 6 and self.player_2_games == 6:
			self.is_tie_break = True
			self.was_player_1_serving_before_tie_break = self.is_player_1_serving
		return False

	def does_anyone_won_the_match(self):
		return (self.player_1_sets == 3 or self.player_2_sets == 3)

	def check_if_anyone_has_won_the_match(self):
		if self.does_anyone_won_the_match():
			self.is_game_over = True
			return True
		return False

	def get_player_1_score(self):
		score = self.player_1_score

		if self.is_tie_break:
			return str(score)
		elif score <= 3:
			return self.points[score]
		else:
			if score > self.player_2_score:
				if score - self.player_2_score >= 2:
					return "GAME"
				return "ADV"
			else:
				return "40"

	def get_player_2_score(self):
		score = self.player_2_score

		if self.is_tie_break:
			return str(score)
		elif score <= 3:
			return self.points[score]
		else:
			if score > self.player_1_score:
				if score - self.player_1_score >= 2:
					return "GAME"
				return "ADV"
			else:
				return "40"

	def __str__(self):
		return (
			str(self.player_1_sets)
			+ "("
			+ str(self.player_1_games)
			+ ")["
			+ self.get_player_1_score()
			+ "]-"
			+ str(self.player_2_sets)
			+ "("
			+ str(self.player_2_games)
			+ ")["
			+ self.get_player_2_score()
			+ "]"
		)


if __name__ == "__main__":
	game = Game()

	N = int(input())
	results = input()

	if N < 1 or N > 300:
		print("error in input")
		exit()

	if len(results) != N:
		print("error in input")
		exit()

	for i in range(N):
		score = results[i]

		if game.is_game_over():
			print("error in input")
			exit()

		if score == "W":
			game.won_point()
		elif score == "L":
			game.lost_point()
		else:
			print("error in input")
			exit()

	print(game)
