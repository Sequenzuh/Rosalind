text = open("input.txt", "r")
lines = text.readlines()
DNA = lines[0]
motif = lines[1]
position = []

for i in range(len(DNA) - len(motif)):
    if DNA[i:i+len(motif)] == motif:
        position.append(i+1)

for i in range(len(position)):
    print(position[i], end=" ")
