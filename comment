def remove_comments(lines):
    x=''
    for i in lines.splitlines():
        k = (i+'.')[:-1]
        if k.strip().find('#') == 0:
            continue
        x+=i
        x+='\n'
    return x
