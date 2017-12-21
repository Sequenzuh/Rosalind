text = open("input.txt", "r")
RNA = text.readline()
codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S",
          "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
          "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W", "CUU":"L", "CUC":"L",
          "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
          "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R",
          "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
          "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N",
          "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
          "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A",
          "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
          "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
protein = ""
start = 0

for i in range(len(RNA)):
    if codons[RNA[i:i+3]] == "M":
        start = i + 3
        protein += "M"
        break

for i in range(start, len(RNA)-3, 3):
    if codons[RNA[i:i+3]] == "Stop":    
        break
    else:
        protein += codons[RNA[i:i+3]]

print(protein)

