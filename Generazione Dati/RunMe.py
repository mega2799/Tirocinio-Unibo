import json
import random
from xml.dom.minidom import Element

expA = 3

expB = 4

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

ATT4 = []

ATT5 = []

ATT6 = []

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
        POST.append({"AK" : i, "A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "testo"})
    lists = {"id" : 1 , "Post" : POST}
    file_p.write(json.dumps(lists))
    for i in range(N_COMMENT):
        COMMENT.append({"BK" : i, "AK" : random.randint(0, N_POST -1) , "B1" : i%N_ATT1, "B2" : i%N_ATT2, "B3" : i%N_ATT3, "B4" : i%N_ATT1, "B5" : i%N_ATT2, "B6" : i%N_ATT3, "B7" : "testo"})
    lists = {"id" : 2, "Comment" : COMMENT}
    file_c.write(json.dumps(lists))


def referencing_CP():
    for i in range(N_COMMENT):
        COMMENT.append({"BK" : i, "B1" : i%N_ATT1, "B2" : i%N_ATT2, "B3" : i%N_ATT3, "B4" : i%N_ATT1, "B5" : i%N_ATT2, "B6" : i%N_ATT3, "B7" : "In vel mauris felis. Cras consectetur nisi quis diam molestie dapibus. Donec faucibus non urna et blandit. In ac gravida turpis, suscipit pulvinar arcu. Aenean eros purus, vehicula quis facilisis sit amet, luctus non est. Vestibulum at sapien odio. Nulla at scelerisque justo, vel tristique magna. Nullam semper porta lacinia. Integer neque odio, iaculis quis aliquam sit amet, ultrices quis libero. Vestibulum non feugiat lectus. Aliquam erat volutpat. Proin dignissim sollicitudin pretium. Donec laoreet, nisi a feugiat tristique, enim felis aliquam dui, sed eleifend quam massa eu lorem. Proin pulvinar nunc sit amet eros consequat tristique. Pellentesque sed nisl elit.Fusce elementum fermentum diam, quis tristique turpis vulputate eu. Curabitur laoreet odio enim, at faucibus lacus sodales quis. Proin porta justo vel vestibulum lobortis. Nulla eros turpis, accumsan id efficitur quis, scelerisque eu ex. In eleifend nisi at purus condimentum, nec semper urna sodales. Suspendisse interdum dui."})
    lists = {"id" : 2, "Comment" : COMMENT}
    file_c.write(json.dumps(lists))
    for i in range(N_POST):
        POST.append({"AK" : i, "BK" : random.randint(0, N_COMMENT - 1) ,"A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "In vel mauris felis. Cras consectetur nisi quis diam molestie dapibus. Donec faucibus non urna et blandit. In ac gravida turpis, suscipit pulvinar arcu. Aenean eros purus, vehicula quis facilisis sit amet, luctus non est. Vestibulum at sapien odio. Nulla at scelerisque justo, vel tristique magna. Nullam semper porta lacinia. Integer neque odio, iaculis quis aliquam sit amet, ultrices quis libero. Vestibulum non feugiat lectus. Aliquam erat volutpat. Proin dignissim sollicitudin pretium. Donec laoreet, nisi a feugiat tristique, enim felis aliquam dui, sed eleifend quam massa eu lorem. Proin pulvinar nunc sit amet eros consequat tristique. Pellentesque sed nisl elit.Fusce elementum fermentum diam, quis tristique turpis vulputate eu. Curabitur laoreet odio enim, at faucibus lacus sodales quis. Proin porta justo vel vestibulum lobortis. Nulla eros turpis, accumsan id efficitur quis, scelerisque eu ex. In eleifend nisi at purus condimentum, nec semper urna sodales. Suspendisse interdum dui."})
    lists = {"id" : 1 , "Post" : POST}
    file_p.write(json.dumps(lists))
 


def embedding_CP():
    for i in range(N_COMMENT):
        COMMENT.append({"BK" : i, "B1" : i%N_ATT1, "B2" : i%N_ATT2, "B3" : i%N_ATT3, "B4" : i%N_ATT1, "B5" : i%N_ATT2, "B6" : i%N_ATT3, "B7" : "testo"})
    for i in range(N_POST):
        POST.append({"AK" : i, "FBK" : random.choices(COMMENT, k=3) , "A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "testo"})
    lists = {"Post with comment" : POST}
    file_cp.write(json.dumps(lists))



def embedding_PC():
    for i in range(N_POST):
        POST.append({"AK" : i, "A1" : i%N_ATT1, "A2" : i%N_ATT2, "A3" : i%N_ATT3, "A4" : i%N_ATT1, "A5" : i%N_ATT2, "A6" : i%N_ATT3, "A7" : "testo"})
    for i in range(N_COMMENT):
        COMMENT.append({"BK" : i,"FAK" : random.choices(POST, k=3), "B1" : i%N_ATT1, "B2" : i%N_ATT2, "B3" : i%N_ATT3, "B4" : i%N_ATT1, "B5" : i%N_ATT2, "B6" : i%N_ATT3, "B7" : "testo"})
    lists = {"Comment with post" : COMMENT}
    file_pc.write(json.dumps(lists))
    

def getAndDel(array):
    element = random.choice(array)
    array.remove(element)
    return element

def buildAB():
    built = list(range(0, 100)) # magic number
    builtB = list(range(0, 1000)) # magic number
    for i in range(100):
        el = getAndDel(built)
        file_A.write(json.dumps({"AK" : el,"A1" : random.randint(0, N_ATT1), "A2" : random.randint(0, N_ATT2), "A3" : random.randint(0, N_ATT3), "A4" : random.randint(0, N_ATT1), "A5" : random.randint(0, N_ATT2), "A6" : random.randint(0, N_ATT3), "A7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." }) + "\n")
        for j in range(RELATION_FACTOR):
            el = getAndDel(builtB)
            file_A.write(json.dumps({"BK" : el,"B1" : random.randint(0, N_ATT1), "B2" : random.randint(0, N_ATT2), "B3" : random.randint(0, N_ATT3), "B4" : random.randint(0, N_ATT1), "B5" : random.randint(0, N_ATT2), "B6" : random.randint(0, N_ATT3), "B7" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacinia eget arcu et maximus. Ut tempus est sit amet tortor commodo, sit amet facilisis mi rhoncus. Donec et elit venenatis, consequat tellus eu, tristique orci. Duis tristique sem ut nulla ullamcorper, a porta risus efficitur. Cras sed neque et nisl tincidunt vestibulum. Phasellus tristique tempor facilisis. Sed facilisis lectus eros, sed aliquet lacus elementum sed. Integer vel dictum mi. Maecenas pharetra tempus eros, efficitur mattis erat cursus in. Nulla sit amet quam velit. Nullam tempus dictum lacus id porttitor. Vestibulum facilisis pulvinar fermentum. Ut elementum maximus feugiat. In at mollis leo, eu facilisis magna. Vestibulum sed nisi ultricies, tincidunt enim ac, fringilla ex. Phasellus pharetra mollis nisi a fermentum. In nec faucibus nulla, eget molestie magna. Vivamus in gravida ex. Aenean scelerisque gravida ipsum, nec congue enim posuere sit amet. Donec vitae felis id sem congue blandit eget non justo quis." }) + "\n")
 





file_A = open("AB.json", "w")


if __name__ == "__main__":
    buildAB()
    # choosenOne = choose_option()
    # if choosenOne == '1' :
    #     file_p = open("post.json", "w")
    #     file_c = open("comment.json", "w")
    #     referencing_PC()
    # elif choosenOne == '2':
    #     file_c = open("comment.json", "w")
    #     file_p = open("post.json", "w")
    #     referencing_CP()
    # elif choosenOne == '3':   
    #     file_pc = open("postAndComment.json", "w")
    #     embedding_PC()
    # elif choosenOne == '4':
    #     file_cp = open("commentAndPost.json", "w")
    #     embedding_CP()


