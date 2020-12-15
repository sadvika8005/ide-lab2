def list_variables(lines):
    ans = set()
    for i in lines.splitlines():
        i.strip()
        if '=' in i:
            x = i.split('=')[0]
            if ',' in x:
                l = x.split(',')
                for j in l:
                    ans.add(j.strip())
            else:
                if x !='':
                    ans.add(x.strip())
        elif i.startswith('def'):
            x = i.split('(')[-1].split(')')[0]
            if ',' in x:
                l = x.split(',')
                for j in l:
                    ans.add(j.strip())
            else:
                if x !='':
                    ans.add(x.strip())
        elif i.startswith('for'):
            x = i.split(' in ')[0][4:]
            if ',' in x:
                l = x.split(',')
                for j in l:
                    ans.add(j.strip())
            else:
                if x !='':
                    ans.add(x.strip())
    return ans
