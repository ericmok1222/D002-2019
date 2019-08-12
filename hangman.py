import random
answer_list=["apple","arrange","quiet","op","pop","cute"]
x=random.randint(0,len(answer_list)-1)
answer = answer_list[x]
print(answer)
print("there are %d letter in the word"%len(answer))
show_answer=[]
count=0
no="_"
for i in range(0,len(answer)):
    show_answer+=[no]
print(show_answer)
while count<11:
    guess=input("guess the letter")
    if guess in answer:
        location=answer.find(guess)
        show_answer[location]=guess
        print(show_answer)
        if show_answer == answer:
            status=win
            break
    else:
        print("wrong guess")
        count+1
        if count >=9:
            status=lose
            break
if status==win:
    print("you get it with %d error only"%count)
else:
    print("you die")
