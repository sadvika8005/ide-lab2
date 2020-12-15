def list_imports(lines):
    ans = []
    for i in lines.splitlines():
        if i.find('import') == 0:
            ans.append(i.split()[-1])
        elif i.find('from') == 0:
            x = i.split('import')
            l = x[-1].split(',')
            for j in l:
                if 'as ' in j:
                    ans.append(j.split('as')[-1].strip())
                else:
                    ans.append(j.strip())
    return ans
