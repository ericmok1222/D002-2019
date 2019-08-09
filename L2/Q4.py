max=0
for a in range(1,60):
    for b in range(1,60):
        for c in range(1,60):
            for d in range(1,60):
                if a+b+c+d==60:
                    t_max=a*b+a*c+c*d
                    if t_max>max:
                        max=t_max
print(max)
