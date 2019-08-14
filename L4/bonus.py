def over(x1,x2,y1,y2):
    for i in range(0,2):
        if (x1[0]<=x2[i]<=x1[1])or (x2[0]<x1[i]<=x2[1]) or (y1[0]<=y2[i]<=y1[1])or(y2[0]<=y1[i]<=y2[1]):
            return 1
        else:
            return 0




x1=[1,8]
y1=[4,2]
x2=[8,11]
y2=[2,1]


status=over(x1,x2,y1,y2)
if status==1:
    print("yes")
else:
    print("no")
