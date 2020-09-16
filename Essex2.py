# #################################################################################################
# ##                                                                                             ##
# ## Essex Problem #2: Dealing Cards                                                             ##
# ## -------------------------------                                                             ##
# ##                                                                                             ##
# ## Get one card from the top of the card deck and return it. If there is not cards left in     ##
# ## the deck return an error or exception (we choose exception).                                ##
# ##                                                                                             ##
# #################################################################################################
from Essex import Card, Deck, DeckError

deck = Deck() # defaults to a standard 52-card deck (no jokers)

print('We will deal from an unshuffled deck....')
print('1st 13 cards should be all the Spades, from 2 to Ace')
for n in range(13):
    card = deck.deal()
    print(f'{1+n:2d}: {card}')

# we will skip the next 37 cards to get the the last card in the deck
for n in range(38):
    deck.deal()
    
# the last card
print('the final card in the deck should be the Ace of Clubs')
card  = deck.deal()
print(card)

print('Deal a Card, but nothing is left...Raise an exception!')
try:
    card = deck.deal()
except DeckError as e:
    print(e)
else:
    print('We should never see this card...')
    print(card)
