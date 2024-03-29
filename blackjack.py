import random
'''
Global Variables
'''
suits = ('Hearts', 'Diamonds', 'spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values =  {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}



Playing = True


class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank} of {self.suit}'


class Deck:
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += '\n '+card.__str__()
		return "The deck has : " + str(deck_comp)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

'''
test

test_deck = Deck()
print(test_deck)
'''
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == "Ace":
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1
'''
test

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.value

for card in test_player.cards:
    print(card)
'''

class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0
	def win_bet(self):
		self.total += self.bet
	def lose_bet(self):
		self.total -= self.bet


def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("What's your bet? : "))
		except ValueError:
			print("Numbers only bitch!")
		else:
			if chips.bet > chips.total or chips.bet < 1:
				print("You don't have enough.")
			else:
				break



def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing
	while True:
		
		x = input("type h or s for Hit or Stand : ")
		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("You stand... Dealer is playing.")
			playing = False
		else:
			print("invalid entry")
			continue
		break
		

		

def show_some(player,dealer):
	print("\nDealer's hand:")
	print("\n<card hidden>")
	print('',dealer.cards[1])
	print("\nPlayers hand:", *player.cards, sep='\n ')


def show_all(player,dealer):
	print("\nDealer's hand:", *dealer.cards, sep='\n')
	print("Dealer value: " ,dealer.value)
	print("\nPlayers hand:", *player.cards, sep='\n ')
	print("Player's vlaue: ",player.value)

def player_busts(player,dealer,chips):
	print("You bust!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("You win!:)")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer busts")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("The dealer wins")
	chips.lose_bet()

def push(player,dealer):
	print("It's a push!")

chips = Chips()
'''
ONTO THE GAME>>>>
'''
while True:
	print("Welcome to BlackJack.. GAME ON")
	deck = Deck()
	deck.shuffle()
	player = Hand()
	player.add_card(deck.deal())
	player.add_card(deck.deal())
	dealer = Hand()
	dealer.add_card(deck.deal())
	dealer.add_card(deck.deal())
	

	print("\nYour chip balance is :",chips.total)
	take_bet(chips)
	show_some(player,dealer)
	playing = True
	while playing:
		hit_or_stand(deck,player)
		show_some(player,dealer)
		if player.value > 21:
			player_busts(player,dealer,chips)
			break

	if player.value <= 21:
		while dealer.value < 17:
			hit(deck,dealer)

		show_all(player,dealer)

		if dealer.value > 21:
			dealer_busts(player,dealer,chips)

		elif player.value > dealer.value:
			player_wins(player,dealer,chips)
		elif player.value < dealer.value:
			dealer_wins(player,dealer,chips)
		else:
			push(player,dealer)
	print("\nYour chip balance is :",chips.total)

	new_game = input("Wanna play another hand? Y or N : ")
	if new_game[0].lower()=='y':
		Playing=True
		continue
	else:
		print("Bye!")
		break

