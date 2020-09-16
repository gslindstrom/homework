# #################################################################################################
# ##                                                                                             ##
# ## Essex Problem #4: A Simple Game                                                             ##
# ## -------------------------------                                                             ##
# ##                                                                                             ##
# ## For this game our deck consists of:                                                         ##
# ##      Suits: Green, Yellow and Red                                                           ##
# ##      Ranks: 1, 2, 3, 4, 5                                                                   ##
# ##                                                                                             ##
# ## Deal each of 2-players 3 cards each.                                                        ##
# ## The score of each card is the Rank of the Card times the Color (1 for Green, 2 for Yellow   ##
# ## and 3 for Red).                                                                             ##
# ## The sum of the three cards is the score for the hand.                                       ##
# ## The player with the higher score wins.                                                      ##
# ##                                                                                             ##
# #################################################################################################
from Essex import Card, Deck

# we allow a varying number of cards
MAX_CARDS = 3

SUITS = ['Green','Yellow','Red'] # placed in ascending value order
RANKS = ['1','2','3','4','5']

# create a method to score each hand
def score_hand(cards):
    '''We score the hand as follows:
       green = 1, yellow = 2, red = 3
       The value of each card is color * number
       Total Score we sum the scores for each card'''
    
    score = 0
    for card in cards:
        rank_int = 1+RANKS.index(card.rank)
        suit_int = 1+SUITS.index(card.suit)
        score += (rank_int * suit_int)
    return score

# make a deck of cards for our game and shuffle
deck = Deck(suits=SUITS, ranks=RANKS)
deck.shuffle()

# create arrays to hold the cards for each player
player1 = []
player2 = []

# deal the hands
for card in range(MAX_CARDS):
    player1.append(deck.deal())
    player2.append(deck.deal())
    
# score hands

# Player 1
print()
print('=== Player 1 ===')
for card in player1:
    print(card, end=' ')
print()
score1 = score_hand(player1)
print(f'for {score1} points')


# Player 2
print()
print('=== Player 2 ===')
for card in player2:
    print(card, end=' ')
print()
score2 = score_hand(player2)
print(f'for {score2} points')
print()

# Results
if score1 > score2:
    print('Player 1 Wins!!')
elif score2 > score1:
    print('Player 2 wins!!')
else:
    print("It's a Tie!!")
    

    
