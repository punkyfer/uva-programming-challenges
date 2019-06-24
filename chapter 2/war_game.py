from collections import deque

NCARDS = 52
NSUITS = 4
MAXSTEPS = 1000

values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
suits = ["c","d","h","s"]

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

def read_input():
    player_queues = []
    while (True):
        try:
            aux_deck = input().split(" ")
            aux_queue = deque()
            for elem in aux_deck:
                aux_queue.append(rank_card(elem[0], elem[1]))
            player_queues.append(aux_queue)
        except EOFError:
            break
    return (player_queues)

def join_queues(a, b):
    while(len(b)>0):
        a.appendleft(b.pop())

def war(a, b):
    steps=0
    c = deque()
    inwar = False
    while ( len(a)>0 and (len(b)>0 and steps<MAXSTEPS)):
        steps += 1
        x = a.pop()
        y = b.pop()
        c.appendleft(x)
        c.appendleft(y)
        #print (c)
        if (inwar):
            inwar=False
        else:
            if value(x) > value(y):
                join_queues(a, c)
            elif value(x) < value(y):
                join_queues(b, c)
            elif value(x) == value(y):
                inwar = True
    if (len(a)>0 and len(b)==0):
        print ("a wins in "+str(steps)+" steps")
    elif (len(a)==0 and len(b)>0):
        print ("b wins in "+str(steps)+" steps")
    elif (len(a)>0 and len(b)>0):
        print ("game tied after "+str(steps)+" steps, |a|="+str(len(a))+" |b|="+str(len(b)))
    else:
        print("a and b tie in "+str(steps)+" steps")
        

player_queues = read_input()
war(player_queues[0], player_queues[1])