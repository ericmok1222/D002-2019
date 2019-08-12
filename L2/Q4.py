max=0
for a in range(0,61):
    for b in range(0,61):
        for c in range(0,61):
            for d in range(0,61):
                if a+b+c+d==60:
                    t_max=a*b+a*c+c*d
                    if t_max>max:
                        max=t_max
                        print(a,b,c,d)
print(max)
input()
