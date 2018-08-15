import re
if __name__=='__main__':
    sums=0
    n=''
    i=0
    for i in range(7777700,7777778):
        n=str(i)
        if re.findall('8',n,re.I) or re.findall('9',n,re.I):
            continue
        elif i%2:
            print(i)
            sums+=1
    print(sums)
