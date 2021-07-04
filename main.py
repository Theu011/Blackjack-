from card import *

game_deck = Deck()
game_deck.shuffle()

# Data inputs
name = input('Enter your name ')
bet = int(input('Please place a bet '))
player_1 = Player(bet, name)

# Dealer and player cards
dealer_cards = []
player_cards = []

player_goal = 0
dealer_goal = 0

# Value of ace to be determined
ace_value = 0

# Putting cards on the table
for card in range(2):
    dealer_cards.append(game_deck.deal_one())
    dealer_goal += dealer_cards[card].value
for card in range(2):
    player_cards.append(game_deck.deal_one())
    if(player_cards[-1].rank == 'Ace'):
            ace_value = int(input('Do you wanna your ace to be 1 or 11? '))
            player_cards[-1].value = ace_value   
    player_goal += player_cards[card].value 
game_on = True

# Game
while game_on:
    # Dealer's cards
    print("\nDealer's cards: ")
    print(dealer_cards[0])

    # Player's cards
    print("\nPlayer's cards")
    for card in player_cards:
        print(card)
    print("\n")
    
    # Check if the player wants to hit or stay
    hit = int(input('Do you want to hit(1) or stay(0)'))
    if(hit == 1):
        player_cards.append(game_deck.deal_one())
        if(player_cards[-1].rank == 'Ace'):
            ace_value = int(input('Do you wanna your ace to be 1 or 11? '))
            player_cards[-1].value = ace_value
        player_goal += player_cards[-1].value
    elif(hit == 0):
        # Player won
        if(player_goal == 21):
            player_1.won()
            print(f'{player_1.name} you won {player_1.bankroll} =D ')
            game_on = False
        # Machine Dealer playing
        elif(player_goal < 21):
            # Hitting until the dealer goal be greater than the player goal
            while(player_goal > dealer_goal):
                dealer_cards.append(game_deck.deal_one())
                dealer_goal += dealer_cards[-1].value
            # Dealer bust
            if(dealer_goal > 21):
                player_1.won()
                print(f'{player_1.name} you won {player_1.bankroll} =D ')
                game_on = False
            # Dealer won
            if((dealer_goal > player_goal) and (dealer_goal < 21)):
                player_1.lose()
                print(f'{player_1.name} you lose your money =( \nThis was your hand')
                for card in player_cards:
                    print(card)
                print("\nThis was the dealer's hand")
                for card in dealer_cards:
                    print(card)
                print("\n")
                game_on = False

    # Player bust
    if(player_goal > 21):
        player_1.lose()
        print(f'{player_1.name} you lose your money =( \nThis was your hand')
        for card in player_cards:
            print(card)
        print("\nThis was the dealer's hand")
        for card in dealer_cards:
            print(card)
        print("\n")
        game_on = False
