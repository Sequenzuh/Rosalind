text = open("input.txt", "r")
DNA = text.readline()
DNA_comp = ""

for nucleotide in DNA:
    if nucleotide == "T":
        DNA_comp += "A"
    elif nucleotide == "A":
        DNA_comp += "T"
    elif nucleotide == "C":
        DNA_comp += "G"
    else:
        DNA_comp += "C"

print(DNA_comp[::-1])
