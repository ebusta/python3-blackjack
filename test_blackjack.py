import unittest
import blackjack

class TestBlackJack(unittest.TestCase):

	def test_player_unique_start_balance(self):
		name = "Joe"
		balance = "50"
		new_player = blackjack.Player(name,balance)
		result = str(new_player)
		self.assertEqual(result, "Joe, you have $50 left.")

	def test_player_default_start_balance(self):
		name = "Joe"
		balance = "100"
		new_player = blackjack.Player(name,balance)
		result = str(new_player)
		self.assertEqual(result, "Joe, you have $100 left.")

if __name__=='__main__':
	unittest.main()