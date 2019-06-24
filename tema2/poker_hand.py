NCARDS = 52
NSUITS = 4

values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
suits = ["C","D","H","S"]

def rank_card(value, suit):
    for i in range(int(NCARDS/NSUITS)):
        if values[i] == value:
            for j in range(NSUITS):
                if suits[j]==suit:
                    return (i*NSUITS+j)
                
    print("Warning: bad input value="+str(value)+", suit="+suit)
    
def suit(card):
    return (suits[int(card%NSUITS)])

def value(card):
    return (values[int(card/NSUITS)])

def rank_hand(cards):
    cards = sorted(cards)
    flush = [cards[0]]
    same_value = [[cards[0]]]
    straight = [cards[0]]
    high_card = values.index(value(cards[-1]))
    for i,card in enumerate(cards[1:]):
        if values.index(value(card)) > high_card:
            high_card = values.index(value(card))
        if suit(card) == suit(cards[i]):
            flush.append(card)
        if values.index(value(card))-1 == values.index(value(cards[i])):
            straight.append(card)
        aux_taken = False
        for same_cards in same_value:
            if not aux_taken and value(card) == value(same_cards[-1]):
                same_cards.append(card)
                aux_taken = True
        if not aux_taken:
            same_value.append([card])
    same_value.sort(key=len)
    three, pair, double_pair = False, False, False
    if len(flush)==5 and len(straight)==5:
        return (8, high_card, straight)
    else:
        if len(same_value[-1])==4:
            return (7, high_card, same_value)
        elif len(same_value[-1])==3:
            three = True
        elif len(same_value[-1])==2:
            pair = True
        if len(same_value[-2])==2:
            double_pair = True
            
        if double_pair and three:
            return (6, high_card, same_value)
        else:
            if len(flush)==5:
                return (5, high_card, flush)
            else:
                if len(straight)==5:
                    return (4, high_card, straight)
                elif three:
                    return (3, high_card, same_value)
                elif double_pair:
                    return (2, high_card, same_value)
                elif pair:
                    same_value = [[x for y in same_value[:-1] for x in y],same_value[-1]]
                    return (1, high_card, same_value)
                else:
                    return (0, high_card, cards)
    
def compare_hands(black_rank, white_rank):
    if black_rank[0] > white_rank[0]:
        print ("Black wins.")
    elif white_rank[0] > black_rank[0]:
        print ("White wins.")
    else:
        if black_rank[0] in [8,4]:
            if white_rank[1] > black_rank[1]:
                print ("White wins.")
            elif black_rank[1] > white_rank[1]:
                print ("Black wins.")
            else:
                print ("Tie.")
        elif black_rank[0] in [7,6,3]:
            if values.index(value(white_rank[2][-1][-1])) > values.index(value(black_rank[2][-1][-1])):
                print ("White wins.")
            elif values.index(value(black_rank[2][-1][-1])) > values.index(value(white_rank[2][-1][-1])):
                print ("Black wins.")
            else:
                print ("Tie.")
        elif black_rank[0] in [5, 0]:
            check_high_cards(black_rank[2], white_rank[2])
        elif black_rank[0] == 2:
            if not check_pairs(black_rank[2][-1], white_rank[2][-1]):
                if not check_pairs(black_rank[2][-2], white_rank[2][-2]):
                    if values.index(value(black_rank[2][-3][-1])) > values.index(value(white_rank[2][-3][-1])):
                        print ("Black wins.")
                    elif values.index(value(white_rank[2][-3][-1])) > values.index(value(black_rank[2][-3][-1])):
                        print ("White wins.")
                    else:
                        print ("Tie.")
        elif black_rank[0] == 1:
            if not check_pairs(black_rank[2][-1], white_rank[2][-1]):
                check_high_cards(black_rank[2][-2], white_rank[2][-2])
                
                    
def check_pairs(black_pair, white_pair):
    if values.index(value(white_pair[-1])) > values.index(value(black_pair[-1])):
        print ("White wins.")
        return True
    elif values.index(value(black_pair[-1])) > values.index(value(white_pair[-1])):
        print ("Black wins.")
        return True
    else:
        return False
def check_high_cards(black_cards, white_cards):
    tie = True
    for i in range(len(black_cards)-1,-1,-1):
        if values.index(value(white_cards[i])) > values.index(value(black_cards[i])):
            print ("White wins.")
            tie = False
            break
        if values.index(value(black_cards[i])) > values.index(value(white_cards[i])):
            print ("Black wins.")
            tie = False
            break
    if tie:
        print ("Tie.")
 
def read_input():
    player_hands = []
    while (True):
        try:
            aux_deck = input().strip().split(" ")
            hand_tuple = [[],[]]
            for i,elem in enumerate(aux_deck):
                if i < 5:
                    hand_tuple[0].append(rank_card(elem[0], elem[1]))
                else:
                    hand_tuple[1].append(rank_card(elem[0], elem[1]))
            player_hands.append(hand_tuple)
        except EOFError:
            break
    return player_hands

player_hands = read_input()
for hands in player_hands:
    compare_hands(rank_hand(hands[0]), rank_hand(hands[1]))
