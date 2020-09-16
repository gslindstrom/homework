#
# Greg's Homework for Essex 
# 9/15/2020
#
# #################################################################################################
# ##                                                                                             ##
# ## We define the following classes                                                             ##
# ##                                                                                             ##
# ## Card: A single playing card defined with a suit and rank.                                   ##
# ##                                                                                             ##
# ## Deck: A collection of (not neccessarily unique) Cards with the following methods:           ##
# ##                                                                                             ##
# ##       Shuffle: Randomly rearragne the Deck in place. Does not return a value.               ##
# ##                                                                                             ##
# ##       Deal: Remove and Return the "top" card from the Deck (the first card in the array).   ##
# ##                                                                                             ## 
# ##       False Shuffle: Looks like you're shuffling, but you're not. For cheaters.             ##
# ##                                                                                             ##
# #################################################################################################
# ## Note: We could have used unicode characters but that, we feel, would violate the spirit of  ##
# ##       the coding assignment.                                                                ##
# #################################################################################################
import random

# Let's define a standard 52-card deck. Relax, you can override them if you choose.
SUITS = ('Spades','Hearts','Diamonds','Clubs')
RANKS = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

class DeckError(Exception):
    '''Something to throw is we encounter a problem in the Deck'''
    pass

class Card:
    '''A single card consisting of suit and rank'''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # a nice way to print the card
    def __str__(self):
        return f'({self.suit}, {self.rank})'
        
class Deck:
    '''A collection of Cards'''
    def __init__(self, suits=SUITS, ranks=RANKS):
        self.__cards = []
        for suit in suits:
            for rank in ranks:
                self.__cards.append(Card(suit, rank))

    def cards_on_table(self, cards_per_row=13):
        '''print out the remaining cards'''
        print()
        print(f'{len(self.__cards)} left in the deck')
        for n in range(1, 1+len(self.__cards)):
            print(f'{self.__cards[n-1]}, ', end='')
            if ((n)%cards_per_row)==0:
                print()

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.__cards)
        
    def false_shuffle(self):
        '''For the unsavory dealer. Don't be this guy.'''
        pass
        
    def deal(self):
        '''Return a Card form the top of the deck.
           Remove it from the deck'''
        
        if self.__cards:
            return self.__cards.pop(0)
        else:
            # no cards in the deck!
            raise DeckError('No Cards in Deck')
        
# In a production routine I would place test code here. I loke "Nose test" but any
# automated test library would suffice. I do not like manual testing!
if __name__ == '__main__':
    deck = Deck()
    deck.cards_on_table()
    deck.shuffle()
    print('Shuffling Deck')
    deck.cards_on_table()
    card = deck.deal()
    print(card)
    print('Done')
        
            