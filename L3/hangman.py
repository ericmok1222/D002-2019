import random
answer_list=["apple","arrange","quiet","op","pop","cute"]
x=random.randint(0,len(answer_list)-1)
answer = answer_list[x]
print(answer)
print("there are %d letter in the word"%len(answer))
show_answer=[]
count=0
t_count=0
no="_"
for i in range(0,len(answer)):
    show_answer+=[no]
print(show_answer)
while True:
    guess=input("guess the letter")
    if guess in answer:
        index=0
        for i in answer:
          if i == guess:
              show_answer[index]= guess
              t_count+=1
          index+=1
        print(show_answer)
        if t_count==len(answer):
            print("you get it with %d error only"%count)
            break
    else:
        print("wrong guess")
        count+=1
        if count >=9:
             print("you die")
             break
