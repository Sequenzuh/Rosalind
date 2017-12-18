text = open("input.txt", "r")
nucleotides = {"A":0, "T":0, "C":0, "G":0}
DNA = text.readline()

for nucleotide in DNA:
    nucleotides[nucleotide] += 1

print(nucleotides["A"], nucleotides["C"], nucleotides["G"], nucleotides["T"])
