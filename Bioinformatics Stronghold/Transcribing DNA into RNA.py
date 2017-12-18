text = open("input.txt", "r")
DNA = text.readline()
RNA = ""

for i in range(len(DNA)):
    if DNA[i] == "T":
        RNA += "U"
    else:
        RNA += DNA[i]

print(RNA)
