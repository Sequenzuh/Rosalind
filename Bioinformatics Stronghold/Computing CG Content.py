text = open("input.txt", "r")
FASTA_curr = ""
GC_count = 0
nucleotide_count = 0
GC_content_curr = 0
FASTA_top = ""
GC_content_top = 0

for line in text:
    if line[0] == ">":
        if nucleotide_count != 0:
            GC_content_curr = (GC_count / nucleotide_count) * 100
        if GC_content_curr > GC_content_top:
            GC_content_top = GC_content_curr
            FASTA_top = FASTA_curr
        FASTA_curr = line[1:]
        GC_content_curr = 0
        GC_count = 0
        nucleotide_count = 0
    else:
        for i in range(len(line)):
            if line[i] in ["C", "G"]:
                GC_count += 1
            nucleotide_count += 1

if nucleotide_count != 0:
    GC_content_curr = (GC_count / nucleotide_count) * 100
if GC_content_curr > GC_content_top:
    GC_content_top = GC_content_curr
    FASTA_top = FASTA_curr

print(FASTA_top + "\n" + str(GC_content_top))
