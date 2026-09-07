import random
def game_win(user,computer):
    if user==computer:
        return None
    #snake vs Water
    if user=="s" and computer=="w":
        return True
    if user=="w" and computer=="s":
        return False
    #water and GUn

    if user=="w" and computer=="g":
            return True
    if user=="g" and computer=="w":
         return False

    #gun vs snake
    if user=="g" and computer=="s":
            return True
    if user=="s" and computer=="g":
         return False

    
rand_no=random.randint(1,3)
print("Computer's turn:Snake(s),Wtaer(w),Gun(g)")
if rand_no==1:
    computer="s"
elif rand_no==2:
    computer="w"
else:
    compiter="g"
user=input("Your's turn:Snake(s),Wtaer(w),Gun(g)").lower()
result=game_win(user,computer) # return true if you win false for lose ,none for tie
print(f"\nYou choose:{user}")
print(f"\nComputer choose:{computer}")
if result is None:
    print("it's tie")
elif(result):
    print("You win!")
else:
    print("You lose!")
