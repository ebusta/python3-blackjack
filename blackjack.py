from random import shuffle

class Hand:
	def __init__(self,cards,owner):
		self.cards = cards
		self.owner = owner

	def print_self_dealer(self):
		line1 = line2 = line3 = line4 = line5 = line6 = line7 = line8 = line9 = line10 = line11 = line12 = line13 = line14 = line15 = line16 = ""
		scrubline = "  |???????????????|"

		line1 += "  -----------------" * 2
		print(line1)

		line2 += f"  | {self.cards[0].get_value_for_printing()}           {self.cards[0].get_value_for_printing()} |"
		line2 += scrubline
		print (line2)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'S':
			line3 += "  |       #       |"
		elif self.cards[0].get_suit() == 'C':
			line3 += "  |      ###      |"
		else:
			line3 += "  |               |"
		line3 += scrubline
		print(line3)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'S':
			line4 += "  |      # #      |"
		elif self.cards[0].get_suit() == 'C':
			line4 += "  |     #   #     |"
		else:
			line4 += "  |    ##   ##    |"
		line4 += scrubline
		print(line4)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'S' or self.cards[0].get_suit() == 'C':
			line5 += "  |     #   #     |"
		else:
			line5 += "  |   #  # #  #   |"
		line5 += scrubline
		print(line5)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'S':
			line6 += "  |    #     #    |"
		elif self.cards[0].get_suit() == 'C':
			line6 += "  |      # #      |"
		else: 
			line6 += "  |  #    #    #  |"
		line6 += scrubline
		print(line6)

		if self.cards[0].get_suit() == 'D':
			line7 += "  |   #       #   |"
		elif self.cards[0].get_suit() == 'C':
			line7 += "  |    ##   ##    |"
		elif self.cards[0].get_suit() == 'H':
			line7 += "  |  #         #  |"
		else: 
			line7 += "  |    #     #    |"
		line7 += scrubline
		print(line7)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'H':
			line8 += "  |  #         #  |"
		else:
			# Stop worrying! this one catches clubs and spades
			line8 += "  |   #       #   |"
		line8 += scrubline
		print(line8)

		line9 += "  |   #       #   |"
		line9 += scrubline
		print(line9)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'H':
			line10 += "  |    #     #    |"
		else: 
			line10 += "  |   #  # #  #   |"
		line10 += scrubline
		print(line10)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'H':
			line11 += "  |     #   #     |"
		else: 
			line11 += "  |    ## # ##    |"
		line11 += scrubline
		print(line11)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'C' or self.cards[0].get_suit() == 'H':
			line12 += "  |      # #      |"
		else: 
			line12 += "  |       #       |"
		line12 += scrubline
		print(line12)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'H':
			line13 += "  |       #       |"
		elif self.cards[0].get_suit() == 'C':
			line13 += "  |     #####     |"
		else: 
			line13 += "  |      # #      |"
		line13 += scrubline
		print(line13)

		if self.cards[0].get_suit() == 'D' or self.cards[0].get_suit() == 'H' or self.cards[0].get_suit() == 'C':
			line14 += "  |               |"
		else: 
			line14 += "  |     #####     |"
		line14 += scrubline
		print(line14)

		line15 += f"  | {self.cards[0].get_value_for_printing()}           {self.cards[0].get_value_for_printing()} |"
		line15 += scrubline
		print(line15)

		line16 += "  -----------------" * 2
		print(line16)		

	def print_self(self):
		line1 = line2 = line3 = line4 = line5 = line6 = line7 = line8 = line9 = line10 = line11 = line12 = line13 = line14 = line15 = line16 = ""

		for cd in self.cards:
			line1 += "  -----------------"
		print(line1)

		for cd in self.cards:
			line2 += f"  | {cd.get_value_for_printing()}           {cd.get_value_for_printing()} |"
		print(line2)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'S':
				line3 += "  |       #       |"
			elif cd.get_suit() == 'C':
				line3 += "  |      ###      |"
			else:
				line3 += "  |               |"
		print(line3)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'S':
				line4 += "  |      # #      |"
			elif cd.get_suit() == 'C':
				line4 += "  |     #   #     |"
			else:
				line4 += "  |    ##   ##    |"
		print(line4)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'S' or cd.get_suit() == 'C':
				line5 += "  |     #   #     |"
			else:
				line5 += "  |   #  # #  #   |"
		print(line5)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'S':
				line6 += "  |    #     #    |"
			elif cd.get_suit() == 'C':
				line6 += "  |      # #      |"
			else: 
				line6 += "  |  #    #    #  |"
		print(line6)

		for cd in self.cards:
			if cd.get_suit() == 'D':
				line7 += "  |   #       #   |"
			elif cd.get_suit() == 'C':
				line7 += "  |    ##   ##    |"
			elif cd.get_suit() == 'H':
				line7 += "  |  #         #  |"
			else: 
				line7 += "  |    #     #    |"
		print(line7)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'H':
				line8 += "  |  #         #  |"
			else:
				# Stop worrying! this one catches clubs and spades
				line8 += "  |   #       #   |"
		print(line8)

		for cd in self.cards:
			line9 += "  |   #       #   |"
		print(line9)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'H':
				line10 += "  |    #     #    |"
			else: 
				line10 += "  |   #  # #  #   |"
		print(line10)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'H':
				line11 += "  |     #   #     |"
			else: 
				line11 += "  |    ## # ##    |"
		print(line11)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'C' or cd.get_suit() == 'H':
				line12 += "  |      # #      |"
			else: 
				line12 += "  |       #       |"
		print(line12)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'H':
				line13 += "  |       #       |"
			elif cd.get_suit() == 'C':
				line13 += "  |     #####     |"
			else: 
				line13 += "  |      # #      |"
		print(line13)

		for cd in self.cards:
			if cd.get_suit() == 'D' or cd.get_suit() == 'H' or cd.get_suit() == 'C':
				line14 += "  |               |"
			else: 
				line14 += "  |     #####     |"
		print(line14)

		for cd in self.cards:
			line15 += f"  | {cd.get_value_for_printing()}           {cd.get_value_for_printing()} |"
		print(line15)

		for cd in self.cards:
			line16 += "  -----------------"
		print(line16)

	def add_card(self,new_card):
		self.cards.append(new_card)

	def get_score(self):
		contains_ace = False
		score = 0
		for cd in self.cards:
			if cd.get_value() == 1:
				contains_ace = True
				score += 11
			elif cd.get_value() in [10,11,12,13]:
				score += 10
			else:
				score += cd.get_value()
		if score > 21 and contains_ace:
			score -= 10
		return score

class Player:

	def __init__(self,name,balance=100):
		self.name = name
		self.balance = balance

	def __str__(self):
		return f"{self.name}, you have ${self.balance} left."

	def place_bet(self,amt):
		if amt > self.balance:
			raise ArithmeticError("You're overdrawing your bank account!")
		else:
			self.balance -= amt

	def get_paid(self,amt):
		self.balance += amt

	def get_name(self):
		return self.name

	def get_balance(self):
		return self.balance

class Card:

	def __init__(self,suit,value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return f"{self.value} of {self.suit} "

	def get_value(self):
		return self.value

	def get_value_for_printing(self):
		if self.value == 10:
			return 'T'
		elif self.value == 11:
			return 'J'
		elif self.value == 12:
			return 'Q'
		elif self.value == 13:
			return 'K'
		else:
			return self.value

	def get_suit(self):
		return self.suit

class Deck:

	def __init__(self,full_deck=[]):
		self.full_deck = full_deck

	def __del__(self):
		del self.full_deck[:]

	def __str__(self):
		toprint = ""
		for cd in self.full_deck:
			toprint += str(cd)
		return toprint
		
	def build_deck(self):
		diamonds = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		clubs = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		hearts = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		spades = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		for i in diamonds:
			self.full_deck.append(Card('D',i))
		for i in clubs:
			self.full_deck.append(Card('C',i))
		for i in hearts:
			self.full_deck.append(Card('H',i))
		for i in spades:
			self.full_deck.append(Card('S',i))

	def shuffle_deck(self):
		shuffle(self.full_deck)

	def deal_card(self):
		return self.full_deck.pop()

	def deal_hand(self):
		return [self.deal_card(),self.deal_card()]

def get_name():
	return input("Please enter your name: ").upper()

def get_choice():
	while True:
		choice = input("Do you want to hit or stay? H or S? ").upper()
		if choice not in ['H','S']:
			print("Please make a valid selection!!!")
		else:
			break
	return choice

def get_opening_bet(player):
	while True:
		try:
			print(f"You currently have ${player.get_balance()}")
			bet = int(input("Minimum bet is $10. You can only bet multiples of 5. Please enter your starting bet: "))
			if bet > player.get_balance():
				print("Ya, nice try. You don't have that much!")
			elif bet % 5 != 0:
				print("C'mon, multiples of 5 only.")
			elif bet < 10:
				print("That's too little!.")
			else:
				break
		except ValueError:
				print("You've gotta enter a number.")
	return bet

def get_bet(player):
	while True:
		try:
			bet = int(input("Bet more?? Enter 0 if you don't want to. "))
			if bet > player.get_balance():
				print("Ya, nice try. You don't have that much!")
			elif bet % 5 != 0:
				print("C'mon, multiples of 5 only.")
			else:
				break
		except ValueError:
				print("You've gotta enter a number.")
	return bet

def print_board(player_hand,dealer_hand,name,balance,bet,endgame,final_print):
	print("\n"*20)
	print("                 DEALER     \n")
	if final_print == False:
		print("\n")
	if endgame == False:
		dealer_hand.print_self_dealer()
	else:
		dealer_hand.print_self()
	print("\n")
	player_hand.print_self()
	if final_print == False:
		print("\n")
		if check_if_bust(player_hand):
			pass
		else:
			print(f"      Your score is currently {player_hand.get_score()}")
			print(f"      Your have ${balance} in the bank.")
			print(f"      The current bet is ${bet}.")
	print(f"              {name}")

def check_for_win(player_hand,dealer_hand):
	result = ""
	if check_if_bust(player_hand) and check_if_bust(dealer_hand):
		result = "Draw"
	elif check_if_bust(dealer_hand):
		result = "Win"
	elif check_if_bust(player_hand):
		result = "Lose"
	elif player_hand.get_score() > dealer_hand.get_score():
		result = "Win"
	else:
		result = "Lose"
	return result

def check_if_bust(hand):
	return hand.get_score() > 21

def calculate_payout(bet,hand,result):
	if result == "Win":
		if len(hand.cards) == 2 and hand.get_score() == 21:
			bet *= 3
		else:
			bet *= 2
	print(f"\nYou won ${bet}!!!!")
	return bet

def check_play_again():
	while True:
		again = input("Do you want to play again? Y or N: ").upper()
		if again not in ['Y','N']:
			print("Don't be difficult.")
		else:
			break
	return again

def play_game(player):
	current_bet = 0
	deck = Deck()
	deck.build_deck()
	deck.shuffle_deck()
	player_hand = Hand(deck.deal_hand(),player)
	dealer_hand = Hand(deck.deal_hand(),'Dealer')
	current_bet = get_opening_bet(player)
	player.place_bet(current_bet)
	while True:
		print_board(player_hand,dealer_hand,player.get_name(),player.get_balance(),current_bet,False,False)
		new_bet = get_bet(player)
		current_bet += new_bet
		player.place_bet(new_bet)
		if get_choice() == 'H':
			player_hand.add_card(deck.deal_card())
		else:
			break
		if check_if_bust(player_hand):
			break
	# Dealer plays
	while True:
		print_board(player_hand,dealer_hand,player.get_name(),player.get_balance(),current_bet,True,False)
		if check_if_bust(player_hand):
			break
		elif dealer_hand.get_score() < 17:
			input("It's the dealer's turn. Please press enter.")
			dealer_hand.add_card(deck.deal_card())
		else:
			break
	print_board(player_hand,dealer_hand,player.get_name(),player.get_balance(),current_bet,True,True)
	if check_if_bust(dealer_hand):
		print("The Dealer busts!!")
	else:
		print(f"\nThe Dealer scores {dealer_hand.get_score()}")
	if check_if_bust(player_hand):
		print("You busted!!!")
	else:
		print(f"{player.get_name()} scores {player_hand.get_score()}")
	if check_for_win(player_hand,dealer_hand) == "Win":
		print("YOU WIN!!!!!!")
		player.get_paid(calculate_payout(current_bet,player_hand,"Win"))
	elif check_for_win(player_hand,dealer_hand) == "Draw":
		print("It's a draw.")
		player.get_paid(calculate_payout(current_bet,player_hand,"Draw"))
	else:
		print("YOU LOSE!!!!!!")
		print(f"\nYou lost ${current_bet}")
	del deck

def main_loop():
	player = Player(get_name())
	print(f"\n\nWelcome {player.get_name()}!")
	while True:
		play_game(player)
		print(f"You now have ${player.get_balance()}")
		if player.get_balance() == 0:
			print("You're straight broke. Game over!!!")
			break
		if check_play_again() == "Y":
			continue
		else: 
			print("Thanks for playing!!")
		break

print("\n" * 50)
main_loop()




