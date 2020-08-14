t = int(input())
for _ in range(t):
    line = str(input())
    ln = len(line)
    lst = []
    cnt = 0
    for i in range(0, ln):
        if line[i] == '1':
            cnt += 1
        else:
            if cnt:
                lst.append(cnt)
            cnt = 0
    if cnt:
        lst.append(cnt)

    lst.sort()
    tot = 0
    ln = len(lst)
    if ln % 2 == 1:
        for i in range(ln):
            if i % 2 == 0:
                tot += lst[i]
    else:
        for i in range(ln):
            if i % 2 == 1:
                tot += lst[i]
    print(tot)
