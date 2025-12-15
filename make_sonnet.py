import random
import json

with open("chain.json") as f:
    chain = json.load(f)

word = "START"
sonnet = ""
while word != "END":
    if word == "START":
        pass
    elif word in "\n,.!?:":
        sonnet += word
    else:
        if sonnet != "" and not sonnet.endswith("\n"):
            sonnet += " "
        sonnet += word

    word = random.choice(chain[word])

print(sonnet)
