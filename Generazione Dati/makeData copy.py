from ast import expr_context
from asyncio.windows_events import NULL
from contextlib import nullcontext
from operator import length_hint
import random
import json

expA = 4

expB = 5

N_A = 10**expA 

N_B = 10**expB

A = list(range(0, N_A))

B = list(range(0, N_B))

N_A1 = 10 #N_A/10

N_A2 = N_A/10**(round(expA/2))

N_A3 = N_A/10**(expA - 1)

N_B1 = N_B/10

N_B2 = N_B/10**(round(expB/2))

N_B3 = N_B/10**(expB - 1)

A1 = list(range(0, int(N_A1)))

A2 = list(range(0, int(N_A2)))

A3 = list(range(0, int(N_A3)))

B1 = list(range(0,int(N_B1)))

B2 = list(range(0,int(N_B2)))

B3 = list(range(0,int(N_B3)))

def populateList(rangeList):
    return list(range(0, int(rangeList)))

def getAndDel(cacca):
    print("Me sto rompendo " + str(cacca))
    print(length_hint(cacca))
    print(cacca)
    element = random.choice(cacca)
    ind = cacca.index(element)
    print("remove: " + str(element))
    print("remove ind: " + str(ind))
    cazzo =cacca.pop(ind)
    print("mi sono rotto il " + str(cazzo)) 
    return cazzo
        

if __name__ == "__main__":
    file_AB = open("AB.json", "w")
    for i in range(100):
        el_A1 = getAndDel(A1)
        if el_A1 == NULL:
            print("sei tu?" + str(A1))
            A1 = populateList(N_A1)
            print(A1)
            exit(1)
            el_A1 = getAndDel(A1) 
        # el_A2 = getAndDel(A2)
        # if el_A2 == NULL:
            # A2 = populateList(N_A2)
            # el_A2 = getAndDel(A2) 
        # el_A3 = getAndDel(A3)
        # if el_A3 == NULL:
            # A3 = populateList(N_A3)
            # el_A3 = getAndDel(A3) 
        # file_AB.write(json.dumps({"AK" : getAndDel(A),"A1" : el_A1, "A2" : el_A2, "A3" : el_A3, "A4" : el_A1, "A5" : el_A2,"A6" : el_A3 , "A7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." }) + "\n")
    # for y in range(N_B):
        # el_B1 = getAndDel(B1)
        # if el_B1 == NULL:
            # B1 = populateList(N_B1)
            # el_B1 = getAndDel(B1)
        # el_B2 = getAndDel(B2)
        # if el_B2 == NULL:
            # B2 = populateList(N_B2)
            # el_B2 = getAndDel(B2)
        # el_B3 = getAndDel(B3)
        # if el_B1 == NULL:
            # B3 = populateList(N_B3)
            # el_B3 = getAndDel(B3)
        # file_AB.write(json.dumps({"BK" : getAndDel(B),"B1" : el_B1, "B2" : el_B2, "B3" : el_B3, "B4" : el_B1, "B5" : el_B2, "B6" : el_B3 , "B7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." }) + "\n")