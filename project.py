import random
import itertools
from collections import Counter

class Deck:
    #initialise a shuffled deck 
    def __init__(self):

        self.suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.cards = list(itertools.product(self.ranks, self.suits))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    #take second argument to specify how many cards to deal
    def deal(self, num_cards = 1):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in deck")
        dealt_cards = self.cards[:num_cards]
        #update the deck to only cards after the dealt cards
        self.cards = self.cards[num_cards:]
        return dealt_cards
    
    def burn(self, num_cards = 1):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck")
        burn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return burn_cards
    

    def reset(self):
        self.cards = list(itertools.product(self.ranks, self.suits))
        random.shuffle(self.cards)
    
    def __str__(self):
        return f"Deck with {len(self.cards)}  cards"

def evaluate_hand(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    rank_count = Counter(ranks)

    if is_royal_flush(ranks, suits):
        return ("Royal Flush")
    
    elif is_straight_flush(ranks, suits):
        return ("Straight Flush")
    
    elif is_quads(rank_count):
        return ("Four of a Kind")
    
    elif is_full_house(rank_count):
        return("Full House")
    
    elif is_flush(suits):
        return("Flush")
    
    elif is_straight(ranks):
        return("Straight")
    
    elif is_trips(rank_count):
        return("Three of a Kind")
    
    elif is_two_pair(rank_count):
        return("Two-Pair")
    
    elif is_pair(rank_count):
        return("One-Pair")
    
    else:
        return("High Card")

def is_royal_flush(ranks, suits):
    if not is_flush(suits):
        return False
    
    required_ranks = ["10", "J", "Q", "K", "A"]
    for rank in required_ranks:
        if not rank in ranks:
            return False
    
    return len(ranks)==5
    


def is_straight_flush(ranks, suits):
    if not is_flush(suits):
        return False
    return is_straight(ranks)

   

def is_quads(rank_count: dict):
    if 4 in rank_count.values():
        return True

def is_full_house(rank_count: dict):
    if 3 in rank_count.values() and 2 in rank_count.values():
        return True

def is_flush(suits):
    suit1 = suits[0]
    for suit in suits:
        if suit != suit1:
            return False
    return True

def is_straight(ranks):
    rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    if set(ranks) == {"A", "2", "3", "4", "5"}:
        return True

    if len(ranks)!=5:
        return False
    
    try: 
        rank_indices = sorted([rank_order.index(rank) for rank in ranks])
    except ValueError:
        return False
    
    for i in range (1,5):
        if rank_indices[i] != rank_indices[i-1] + 1:
            return False
    return True

def is_trips(rank_count: dict):
    if 3 in rank_count.values():
        return True

def is_two_pair(rank_count: dict):
    pair_count = list(rank_count.values()).count(2)
    return pair_count == 2

def is_pair(rank_count: dict):
    if 2 in rank_count.values():
        return True

def probability_of_royal_flush(num_sim = 10000):
    rf_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        suits = [card[1] for card in hand]
        ranks = [card[0] for card in hand]
        if is_royal_flush(ranks, suits) == True:
            rf_count+=1
        return f"{(rf_count / num_sim)*100}%"

def probability_of_straight_flush(num_sim = 10000):
    sf_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        suits = [card[1] for card in hand]
        ranks = [card[0] for card in hand]
        if is_straight_flush(ranks, suits) == True:
            sf_count+=1
        
    return f"{(sf_count / num_sim)*100}%"

def probability_of_quads(num_sim = 10000):
    quads_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        rank_count = Counter(ranks)
        if is_quads(rank_count)==True:
            quads_count+=1
    return f"{(quads_count / num_sim)*100}%"

def probability_of_full_house(num_sim=10000):
    fh_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        rank_count = Counter(ranks)
        if is_full_house(rank_count)==True:
            fh_count+=1
    return f"{(fh_count / num_sim)*100}%"

def probability_of_flush(num_sim = 10000):
    flush_count = 0 

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        suits = [card[1] for card in hand]
        if is_flush(suits)==True:
            flush_count+=1
    
    return f"{(flush_count / num_sim)*100}%"

def probability_of_straight(num_sim = 10000):
    straight_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        if is_straight(ranks)==True:
            straight_count+=1

    return f"{(straight_count / num_sim)*100}%"

def probability_of_trips(num_sim = 10000):
    trips_count = 0
    
    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        rank_count = Counter(ranks)
        if is_trips(rank_count)==True:
            trips_count+=1
        
    return f"{(trips_count / num_sim)*100}%"

def probability_of_two_pair(num_sim=10000):
    twopair_count = 0
    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        rank_count = Counter(ranks)
        if is_two_pair(rank_count)==True:
            twopair_count+=1

    return f"{(twopair_count / num_sim)*100}%"

def probability_of_pair(num_sim=10000):
    pair_count = 0

    for _ in range(num_sim):
        deck = Deck()
        hand = deck.deal(5)
        ranks = [card[0] for card in hand]
        rank_count = Counter(ranks)
        if is_pair(rank_count)==True:
            pair_count+=1
        
    return f"{(pair_count / num_sim)*100}%"

    
def main():
    print(f"Flush: {probability_of_flush(num_sim=10000)}")

    print(f"Royal Flush: {probability_of_royal_flush(num_sim = 10000)}")

    print(f"Full House: {probability_of_full_house(num_sim = 10000)}")

    print(f"Straight: {probability_of_straight(num_sim = 10000)}")

    print(f"Three of a Kind: {probability_of_trips(num_sim = 10000)}")

    print(f"Two pair: {probability_of_two_pair(num_sim=10000)}")

    print(f"Pair: {probability_of_pair(num_sim=10000)}")

    
if __name__ == "__main__":
    main()