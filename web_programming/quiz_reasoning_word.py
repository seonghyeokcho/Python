import random
import numpy as np

words = ['apple', 'orange', 'banana']
word = random.choice(words)
print("answer :", word)
letters = ""  # 사용자로부터 지금까지 입력 받은 모든 알파벳

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success !!!")
        break

    letter = input("input letter > ")  # 사용자 입력 받기

    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Currect :)")
    else:
        print("Wrong :(")
    

