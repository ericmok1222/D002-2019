def ran_answer(answer_list):
    x=random.randint(0,len(answer_list)-1)
    answer = answer_list[x]
    return answer 
def create_show_answer(answer):
    show_answer=[]
    no="_"
    for i in range(0,len(answer)):
        show_answer+=[no]
    return(show_answer)
def get_guess():
    global guess_list
    while True:
        guess=input("guess the letter")
        if guess in guess_list:
            print("enter already")
        else:
            guess_list.append(guess)
            break
    return(guess)
def determind(guess,answer):
    global t_count
    if guess in answer:
        index=0
        for i in answer:
          if i == guess:
              show_answer[index]= guess
              t_count+=1
          index+=1
        print(show_answer)
def final(t_count,answer):
    global count
    global con
    if t_count==len(answer):
            print("you get it with %d error only"%count)
            con = "F"
    else:
        print("wrong guess")
        count+=1
        if count >=9:
             print("you die")







import random
guess_list=[]
answer_list=["apple","arrange","quiet","op","pop","cute"]
answer = ran_answer(answer_list)
print(answer)
print("there are %d letter in the word"%len(answer))
show_answer=create_show_answer(answer)
print(show_answer)
count=0
t_count=0
con = "T"
"T"
while con=="T":
    guess=get_guess()
    determind(guess,answer) 
    final(t_count,answer)
