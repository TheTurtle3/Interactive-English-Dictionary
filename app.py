import json
from difflib import get_close_matches

# creating a dict out of the data.json file
data = json.load(open("data.json"))

# function that finds the def of word
def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        maybe = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead? (Y/N) " % maybe).lower()
        if yn == "y":
            return data[maybe]
        elif yn == "n":
            return "The word does not exist in the Dictionary!"
        else:
            return "We didn't unserstand what you entered."
    else:
        return "The word does not exist in the Dictionary!"

# get user word and print its def
while True:
    user_input = input("Enter a word: ")
    output = meaning(user_input)
    
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    if(input("Do you want to continue? (Y/N) ").lower() == "n"):
        break
