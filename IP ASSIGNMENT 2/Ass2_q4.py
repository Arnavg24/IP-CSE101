import random

def position_checker(guess,word):
    ans=[]
    for i in range(len(word)):
        if guess[i]==word[i]:
            ans.append(guess[i])
    return ans
def letter_checker(guess,word):
    ans=[]
    for i in range(len(word)):
        if (guess[i] in word) and (guess[i]!=word[i]):
            ans.append(guess[i])
    return ans

word_list=['laser','prize','smell','baked','stand','kneel','elect','tasty','clerk','cable','rifle','funny','spray','learn','linen','fleet','north','break','thank','haunt','theme','lemon','witch','shout','lease','jewel','swarm','ample','space','order','curve','vague','flour','store','quota','brink','disco','white','stamp','doubt','track','light','slime','house','lover','trade','ridge','press','slide','fairy']
word=word_list[random.randint(0,49)]
tries=0
flag=False
while tries<6:
    guess=input('Enter a five letter word:')
    if len(guess) != 5:
        print("Invalid guess. Please enter a 5-letter word.")
    else:
        tries += 1
        if guess == word:
            flag = True
            break
        else:
            str1='Following letters are in the correct place:'
            str2='Following letters are in the word but not at the correct place:'
            print(str1,position_checker(guess,word))
            print(str2,letter_checker(guess,word))
    
if flag:
    print('Word guessed in',str(tries),'tries')
else:
    print('No more tries left.','The word was',word)