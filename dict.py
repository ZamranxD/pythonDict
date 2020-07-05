import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


data = json.load(open("data.json"))
userinput = input("Please enter a word : ")


def defword(word):
    word = word.lower()
    if word in data:
       return data[word]
    elif len(get_close_matches(word, data.keys(),cutoff=0.7)) > 0:
        choice = input(f"Did you mean {get_close_matches(word, data.keys())[0]}? Y/N? ")
        if choice=="Y" or choice=="y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Sorry we couldn't find your intended word!"
    else:
        return "Such a word doesn't exist"


mlist = defword(userinput)

if type(mlist) == list:
    for item in mlist:
        print(item)
else:
    print(mlist)













