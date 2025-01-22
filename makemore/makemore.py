import torch

# Read the data
names = open("./makemore/names.txt", "r").read().splitlines()

# Create the most frequent bigrams
bigrams = {}

for name in names:
    name = ["<S>"] + list(name) + ["<E>"]
    for ch, ch2 in zip(name, name[1:]):
        bigrams[(ch,ch2)] = bigrams.get((ch,ch2),0)+1

