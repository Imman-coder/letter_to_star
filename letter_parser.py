e = open("letters.txt").read().split('\n')
p = []
a1, a2, a3, a4, a5 = [], [], [], [], []


def encoder(line):
    s = ""
    t = ""
    f=0
    for i,x in enumerate(line):
        if(i==0):
            t+=x
        elif x in t:
            t += x
        else:
            if f==0 and " " in t:
                s = "0"+str(len(t))
                f=not f
            else:
                s += str(len(t))
            f+=1
            t = x
    s += str(len(t))
    return s

def decoder(line):
    s = ""
    for i,x in enumerate(line):
        for x in range(int(x)):
            s+="*" if i%2==0 else " "
    return s

# x=encoder(" ** ** *")
# print(x)
for x in range(26):
    # p.append((x*6)+5)
    a1.append(encoder(e[(x*6)+0]))
    a2.append(encoder(e[(x*6)+1]))
    a3.append(encoder(e[(x*6)+2]))
    a4.append(encoder(e[(x*6)+3]))
    a5.append(encoder(e[(x*6)+4]))
p.append(a1)
p.append(a2)
p.append(a3)
p.append(a4)
p.append(a5)
print(p)
