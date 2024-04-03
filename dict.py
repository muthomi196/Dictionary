import json
from difflib import get_close_matches

# Load JSON data into a Python dictionary
with open('data.json') as f:
    data = json.load(f)

# Function to return a definition of a word
def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        check = input("Did you mean %s instead? Enter Y if yes, otherwise N to exit: " % get_close_matches(word, data.keys())[0])
        if check == "Y":
            return get_definition(get_close_matches(word, data.keys())[0])
        elif check == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Sorry, this word is not an English word. Please double check your spelling."

# Get user input
word = input('Enter a word: ')

# Get definition or suggestion
output = get_definition(word)
if type(output) == list:  
    for item in output:
        print(item)
else:
    print(output)