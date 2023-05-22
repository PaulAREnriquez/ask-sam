
import json
import random
with open('./data/intents.json', 'r') as f:
    intents = json.load(f)

tag = "goodbye"
for intent in intents["intents"]:
    if tag in intent["tag"]:
        print(type(intent["tag"]))
        print(random.choice(intent['responses']))
    