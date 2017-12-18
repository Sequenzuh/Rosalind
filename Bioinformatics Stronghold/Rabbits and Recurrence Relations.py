text = open("input.txt", "r")
line = text.readline()

n = int(line[0])
k = int(line[1])
F1 = 1
F2 = 1
Fn = 0

for i in range(n-2):
    Fn = F1 + F2 + ((k-1)*F1)
    F1 = F2
    F2 = Fn

print(Fn)
