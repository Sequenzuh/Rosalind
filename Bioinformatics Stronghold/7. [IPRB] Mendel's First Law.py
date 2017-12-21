text = open("input.txt", "r")
line = text.readline()
k = int(line[0])
m = int(line[1])
n = int(line[2])

total = k+m+n
homo_dom = k / total
hetero = m / total
homo_rec = n / total
prob_dom = 0

for i in range(3):
    if i == 0:
        prob_dom += homo_dom * ((k-1)/(total-1))
        prob_dom += hetero * (k/(total-1))
        prob_dom += homo_rec * (k/(total-1))
    if i == 1:
        prob_dom += homo_dom * (m/(total-1))
        prob_dom += hetero * ((m-1)/(total-1)) * (3/4)
        prob_dom += homo_rec * (m/(total-1)) * (1/2)
    if i == 2:
        prob_dom += homo_dom * (n/(total-1))
        prob_dom += hetero * (n/(total-1)) * (1/2)

print(prob_dom)
