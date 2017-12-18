text = open("input.txt", "r")
lines = text.readlines()
DNA = lines[0]
mutated = lines[1]
hamming_distance = 0

for i in range(len(DNA)):
    if DNA[i] != mutated[i]:
        hamming_distance += 1

print(hamming_distance)
