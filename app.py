import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):

    word = word.lower()
    close_matches = get_close_matches(word, data.keys())

    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(close_matches) > 0:
        choice = input("Did you mean %s instead?\nPress Y if yes or N if no: " % close_matches[0])
        if choice.lower() == "y":
            return data[close_matches[0]]
        elif choice.lower() == "n":
            return "Unfortunately our wordsmiths seem to be on strike since the office ran out of coffee. Please try again later."
        else:
            return "We didn't understand your query."
    else:
        return ("Our wordsmiths were not able to understand the word %s, please try another word!" % word)

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)