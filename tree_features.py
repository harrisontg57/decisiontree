chats = []

def load_sep(filename):
    storage = []
    f = open(filename)
    for line in f:
        k = line.split(",")
        k[1] = k[1][:1]
        #print(k)
        if k[1] == 'a' or k[1] == 'n':
            storage.append(k)
    return storage

def count_features(chat, features:list):
    fea = []
    for m in features:
        n = chat.count(m)
        fea.append(n)
    return fea

def get_chat():
    return chats

def get_array_from_file(filen, features:list):
    st = load_sep(filen)
    y = []
    x = []
    for m in st:
        if m[1] == 'a': y.append(1)
        else: y.append(0)
        x.append(count_features(m[0], features))
    return x, y

def get_x_from_chat(chat, features:list):
    x = []
    x.append(count_features(chat, features))
    return x

#load_sep('tim.csv')
