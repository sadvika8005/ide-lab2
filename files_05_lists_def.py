def list_defs(lines):
    ans = []
    for i in lines.splitlines():
        i = i.strip()
        if i.startswith('def'):
            ans.append(i.split()[-1][:-3])
    return ans
