import string
import nltk
from nltk.book import *

def task19():
    alpha = string.ascii_lowercase
    def cesar_chiper(text: str, d:int) -> str:
        shifted = alpha[d:] + alpha[:d]
        shifted_maketrans = str.maketrans(alpha, shifted)
        print(text.translate(shifted_maketrans))
        
    cesar_chiper("abc cba test", 20)


# read stop_words
def task20():
    with open("stop_words.txt", 'r') as f:
        stop_words = list(map((lambda s: s.rstrip()), f.readlines()))

    # read book
    with open("alice.txt", 'r') as f:
        alice = f.read()

    print(f"Alice len: {len(alice)}")

    # a)
    # Test string
    # s = "string\n string. string/ aa.. x y your"
    
    def remove(s, remove):
        return s.translate(str.maketrans('', '', remove))

    alice = remove(alice, string.punctuation)
    alice = remove(alice, "\n")
    print(f"Alice len after punctuation removal: {len(alice)}")
   
    alice = " ".join(filter(lambda w: w.lower() not in stop_words, alice.split()))
    print(f"Alice len after stop words removal: {len(alice)}")
    
    # b)
    
    
    
    #  c)
    from collections import Counter

    def most_common_words_100(l: list):
        l_splitted = l.split()
        l_splitted_counter = Counter(l_splitted)
        mc_words = l_splitted_counter.most_common()
        return list(filter(lambda t: t[1]>=100, mc_words))
    
    print(f"Alice most common words: {most_common_words_100(alice)}")
    

def task21():
    users = {'user1': 'Bema 1a',
             'user2': 'Bema 2a',
             'user3': 'Bema 1b',
             'user4': 'Bema 2b',
             'user5': 'Grunwald 12',
             'user6': 'Grunwald 11',
             'user7': 'Akacjowa 31',
             'user8': 'Zielona 5',}
    
    print(sorted(users.items(), key=lambda x: x[1]))

# Import all books from nltk.book. Check how many times the word knight ap-
# pears in text6 (Monty Python) and text7 (Wall Street Journal).
def task22():
    print(f"word knight apperance in text6: {text6.count('knight')}")
    print(f"word knight apperance in text7: {text7.count('knight')}")
    
# task22():

#  Import all books from nltk.book. Construct a set of words that appear in text6
# (Monty Python) but do not appear in text7 (Wall Street Journal).
def task23(t1, t2):
    print(f"len of set t1: {len(set(t1))}")
    print(f"len of set t2: {len(set(t2))}")
    
    return set(t1) & set(t2)

# print(f"len of t1-t2 {len(task23(text6, text7))}")

# Import all books from nltk.book. Construct a set of words that appear in all texts
# text1 - text9.
def task24():
    return set(text1) & set(text2) & set(text3) & set(text4) & set(text4) & set(text5) & set(text6) & set(text7) & set(text8) & set(text9)

# print(f"Words apperance in all texts from 1 to 9: {task24()}")

# Find the longest sentence in text2
def task25(text):
    nltkText_to_string = "".join(text)
    sentences = nltk.sent_tokenize(nltkText_to_string)
    return max(sentences, key = len)

print(task25(text2))    