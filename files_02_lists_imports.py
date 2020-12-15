def remove(lines, q):
    x=''
    c = 0
    for i in lines.splitlines():
        k = (i+'.')[:-1]
        k =k.strip()
        if k.find(q) == 0 and  c==0:
            if k[-3:] ==q and len(k)!=3:
                continue
            else:
                c = 1
                continue
        if c == 1 and k[-3:] == q:
            c = 0
            continue
        if c == 0:
            i+='\n'
            x+=i
    return x
