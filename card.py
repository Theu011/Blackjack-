import random 

# Assign a number to a string
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Queen': 10, 'Jack': 10, 'King': 10, 'Ace': 1}

# Suits
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
# Ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Queen', 'Jack', 'King', 'Ace')

# Card
# rank, value, suit
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

# Deck
# 52 cards, shuffled
class Deck():
    def __init__(self):
        # List with all cards
        self.all_cards = []
        for rank in ranks:
            for suit in suits:
                # Create the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    # Shuffle the cards of the deck
    def shuffle(self):
        random.shuffle(self.all_cards)
    # Deals a card from the deck
    def deal_one(self):
        return self.all_cards.pop(0)

# Player
class Player():
    def __init__(self, bankroll, name):
        self.bankroll = bankroll
        self.name = name
        self.all_cards = []
    def __str__(self):
        return f'{self.name} bet {self.bankroll}'
    def won(self):
        self.bankroll *= 2
    def lose(self):
        self.bankroll *= 0