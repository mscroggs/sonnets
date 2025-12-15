import json

with open("sonnets.txt") as f:
    sonnets = f.read()

chain = {}

for sonnet in sonnets.split("\n\n"):
    if sonnet.count("\n") == 0:
        continue
    while "\n " in sonnet:
        sonnet = sonnet.replace("\n ", "\n")
    for c in ".,:!?\n":
        sonnet = sonnet.replace(c, f" {c} ")
    while "  " in sonnet:
        sonnet = sonnet.replace("  ", " ")
    while ". ." in sonnet:
        sonnet = sonnet.replace(". .", "..")
    words = sonnet.split(" ")
    for a, b in zip(["START"] + words, words + ["END"]):
        if a not in chain:
            chain[a] = []
        chain[a].append(b)

with open("chain.json", "w") as f:
    json.dump(chain, f)

with open("chain.js", "w") as f:
    f.write("var chain = ")
    json.dump(chain, f)
