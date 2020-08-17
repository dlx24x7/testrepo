tot = 0
for i in [5,4,3,2,1]:
    tot = tot + 1
print(tot)

zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
print("after",zork)

def shift_left(L):
    first_item = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item
    return L
