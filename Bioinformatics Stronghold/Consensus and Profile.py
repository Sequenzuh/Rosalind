text = open("input.txt", "r")
lines = text.readlines()

def DNA_to_profile(DNA, profile):
    for nucleotide_index in range(len(DNA)):
        if DNA[nucleotide_index] == "A":
            profile[0][nucleotide_index] += 1
        elif DNA[nucleotide_index] == "C":
            profile[1][nucleotide_index] += 1
        elif DNA[nucleotide_index] == "G":
            profile[2][nucleotide_index] += 1
        elif DNA[nucleotide_index] == "T":
            profile[3][nucleotide_index] += 1
        else:
            continue
    return profile

def profile_to_consensus(profile):
    consensus = ""
    for nucleotide_index in range(len(profile[0])):
        max_count = max(profile[nucleotide][nucleotide_index] for nucleotide in range(4))
        if max_count == profile[0][nucleotide_index]:
            consensus += "A"
        elif max_count == profile[1][nucleotide_index]:
            consensus += "C"
        elif max_count == profile[2][nucleotide_index]:
            consensus += "G"
        elif max_count == profile[3][nucleotide_index]:
            consensus += "T"
        else:
            continue
    return consensus

DNA_sequences = [""] * 10
DNA_sequence_tracker = -1
for line in lines:
    if line[0] == ">":
        new_sequence = False
        DNA_sequence_tracker += 1
        continue
    else:
        DNA_sequences[DNA_sequence_tracker] += line.strip()
        new_sequence = True

profile = [[0 for i in range(len(DNA_sequences[0]))] for i in range(4)]
for DNA_sequence in DNA_sequences:
    if DNA_sequence: # Non empty string
        profile = DNA_to_profile(DNA_sequence, profile)

print(profile_to_consensus(profile))
print("A:", *profile[0], sep=" ")
print("C:", *profile[1], sep=" ")
print("G:", *profile[2], sep=" ")
print("T:", *profile[3], sep=" ")