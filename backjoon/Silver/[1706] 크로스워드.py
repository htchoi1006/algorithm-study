import sys

R, C = map(int, sys.stdin.readline().split())

li = list()
for i in range(R):
    li.append(sys.stdin.readline().rstrip())

new_li = list(map(list, zip(*li)))

res = list()
for i in range(R):
    save = li[i].split("#")
    for j in save:
        if len(j) > 1:
            res.append(j)

for i in range(C):
    save = "".join(new_li[i]).split("#")
    for j in save:
        if len(j) > 1:
            res.append(j)

res.sort()
print(res[0])