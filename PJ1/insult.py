# This program generates an insult based on a given name through input. - Jakob Delossantos

from random import choice

def getname():
    insultee = input("Who are we insulting today? (type 'exit' to stop insulting): ")
    return insultee

def getnoun():
    nouns = ['dog', 'idiot', 'imbecile', 'dumby', 'noob', 'arse', 'clown', 'bastard', 'fool']
    return choice(nouns)

def getadjective():
    adjectives = ['sweaty', 'stupid', 'small', 'sucky', 'incompetent' , 'annoying', 'thoughtless', 'pathetic', 'weak-willed']
    return choice(adjectives)

if __name__=="__main__":
    
    go = 'go'

    while(go == 'go'):
        name = getname()
        if name == 'exit':
            exit()
    
        noun = getnoun()

        adjective = getadjective()

        print(f"{name} is a {adjective} {noun}!")