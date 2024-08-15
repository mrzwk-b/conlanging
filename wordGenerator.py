import random
phones = ['m','n','q','p','b','t','d','k','g','f','w','s','l','h','j','i','u','e','o','a']
vowels = ['i','u','e','o','a']

def gen(length):
    lex = ""
    while len(lex) < length:
        seg = random.randint(0,19)
        lex += phones[seg]
        if seg < 15:
            v = random.randint(0,5)
            if v == 5:
                continue
            else:
                lex += vowels[v]
        lex += random.choice(['','','','','n','s'])
    return lex
