import itertools as it

rf = open("radius.txt", "r")

radii = []
for line in rf.readlines():
    for elem in line.split(","):
        radii.append(int(elem))

partitions = radii[0]
radii = radii[1:]
perm_elem = []

for i in range(partitions):
    perm_elem.append(i + 1)

print(perm_elem)

possible_partitions = list(it.product(perm_elem, repeat=len(radii)))

definitive_partitions = []
for i in possible_partitions:
    suma = 0
    for elem in i:
        suma += elem
    if suma == partitions:
        i.sort()
        if i not in definitive_partitions:
            definitive_partitions.append(i)

max_part = 0.0
for perm in definitive_partitions:
    part = 0.0
    maxim = 0
    for i in range(len(radii)):
        if radii[i] > maxim:
            maxim = radii[i]
