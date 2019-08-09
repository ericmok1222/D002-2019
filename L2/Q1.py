
while True:
    n=int(input("Please input an positive integer number larger than 2\n"))
    if n>2:
        t_n=0
        if n<10:
            if ((n==3)or(n==5)or(n==7)):
                print("it is a prime number")
            else:
                print("it is not a prime number")
        else:        
            for i in range(1,9):
                if n%i==0:
                    t_n+=1
            if t_n > 1:
                print("it is not a prime number")
            else:
                print("it is a prime number")
   
