# #################################################################################################
# ##                                                                                             ##
# ## Essex Problem #1: Shuffling Cards                                                           ##
# ## ---------------------------------                                                           ##
# ##                                                                                             ##
# ## Randomly mix the cards in the card deck and return a whole deck of cards with a mixed order.##
# ##                                                                                             ##
# ## Note: We created a Deck object and shuffle it in place. The user would always be "in        ##
# ##       possession" of the deck.                                                              ##
# ##                                                                                             ##
# #################################################################################################
from Essex import Card, Deck

# Create a deck of cards
deck = Deck()  # defaults tp standard 52-card deck (no jokers), in order

# show the prestine deck
print('Here is the new deck....')
deck.cards_on_table()

# shuffle the deck
print()
print('Shuffling....')
print()
print('BTW - There is a 1 in 52! (80,658,175,170,943,878,571,660,636,856,403,766,975,289,505,440,883,277,824,000,000,000,000)')
print('chance that the deck will come back in the original order!')
print()
print('Will this be that time?')
deck.shuffle()

# show the mixed deck
print()
print('Here is the shuffled deck...')
deck.cards_on_table()

print('Done')