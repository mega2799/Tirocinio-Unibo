import json
import random

expA = 5

expB = 6

N_POST = 10**expA 

RELATION_FACTOR = 10

N_COMMENT = N_POST * RELATION_FACTOR

SEL_ATT1 = 1e-1 # 1/10

SEL_ATT2 = 1e-2 # 1/100

SEL_ATT3 = 1e-4 # 1/1 000 000

N_ATT1 = SEL_ATT1**-1

N_ATT2 = SEL_ATT2**-1

N_ATT3 = SEL_ATT3**-1

POST = []

COMMENT = []

ATT1 = []

ATT2 = []

ATT3 = []

def build_attributes():
    for i in range(N_ATT1):
        ATT1.append(i)
    for i in range(N_ATT2):
        ATT2.append(i)
    for i in range(N_ATT3):
        ATT3.append(i)   

def choose_option():
    print("Seleziona il metodo con il quale desideri creare la relazione:")
    print("1) referencing di post nei commenti")
    print("2) referencing di commenti nei post")
    print("3) embedding di post nei commenti")
    print("4) embedding di commenti nei post")
    val = input("opzione: ")
    return val 

def referencing_PC():
    for i in range(N_POST):
        POST.append({"AK" : i, "A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "In vel mauris felis. Cras consectetur nisi quis diam molestie dapibus. Donec faucibus non urna et blandit. In ac gravida turpis, suscipit pulvinar arcu. Aenean eros purus, vehicula quis facilisis sit amet, luctus non est. Vestibulum at sapien odio. Nulla at scelerisque justo, vel tristique magna. Nullam semper porta lacinia. Integer neque odio, iaculis quis aliquam sit amet, ultrices quis libero. Vestibulum non feugiat lectus. Aliquam erat volutpat. Proin dignissim sollicitudin pretium. Donec laoreet, nisi a feugiat tristique, enim felis aliquam dui, sed eleifend quam massa eu lorem. Proin pulvinar nunc sit amet eros consequat tristique. Pellentesque sed nisl elit.Fusce elementum fermentum diam, quis tristique turpis vulputate eu. Curabitur laoreet odio enim, at faucibus lacus sodales quis. Proin porta justo vel vestibulum lobortis. Nulla eros turpis, accumsan id efficitur quis, scelerisque eu ex. In eleifend nisi at purus condimentum, nec semper urna sodales. Suspendisse interdum dui."})
        #file.write(json.dumps({"AK" : i, "A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "cacca"}))
    file_p.write(json.dumps(POST))
    for i in range(N_COMMENT):
        COMMENT.append({"BK" : i, "AK" : random.randint(0, N_POST -1) , "B1" : i%N_ATT1, "B2" : i%N_ATT2, "B3" : i%N_ATT3, "B4" : i%N_ATT1, "B5" : i%N_ATT2, "B6" : i%N_ATT3, "B7" : "In vel mauris felis. Cras consectetur nisi quis diam molestie dapibus. Donec faucibus non urna et blandit. In ac gravida turpis, suscipit pulvinar arcu. Aenean eros purus, vehicula quis facilisis sit amet, luctus non est. Vestibulum at sapien odio. Nulla at scelerisque justo, vel tristique magna. Nullam semper porta lacinia. Integer neque odio, iaculis quis aliquam sit amet, ultrices quis libero. Vestibulum non feugiat lectus. Aliquam erat volutpat. Proin dignissim sollicitudin pretium. Donec laoreet, nisi a feugiat tristique, enim felis aliquam dui, sed eleifend quam massa eu lorem. Proin pulvinar nunc sit amet eros consequat tristique. Pellentesque sed nisl elit.Fusce elementum fermentum diam, quis tristique turpis vulputate eu. Curabitur laoreet odio enim, at faucibus lacus sodales quis. Proin porta justo vel vestibulum lobortis. Nulla eros turpis, accumsan id efficitur quis, scelerisque eu ex. In eleifend nisi at purus condimentum, nec semper urna sodales. Suspendisse interdum dui."})
    file_c.write(json.dumps(COMMENT))


def referencing_CP():
    return null

def embedding_PC():
    return null

def embedding_CP():
    return null

file_p = open("post.json", "w")
file_c = open("comment.json", "w")

if __name__ == "__main__":
    choosenOne = choose_option()
    if choosenOne == '1' :
        referencing_PC()
    elif choosenOne == '2':
        referencing_CP()
    elif choosenOne == '3':   
        embedding_PC()
    elif choosenOne == '4':
        embedding_CP()
