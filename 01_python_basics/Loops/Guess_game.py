import random
Guess = random.randint(1,10)
print(Guess)
ans = '-1'
move = 0
print("------------------ Guessing Game started -----------------")
while(True):
    ans = input("Guess the no. btw 1 to 10 or 'q' to quit : ")
    move += 1
    if(ans.strip().lower() == 'q'):
        print("YOU LOSE !")
        print("You quit the game.")
        break
    if not ans.isdigit():
            print("Enter the valid numeric value.")
            continue
    ans = int(ans)
    if(ans == Guess):
        print("YOU WON !")
        print(f"You guess the correct number in {move} move.")
        break
    elif(ans > Guess):
        print("HINT ! -- Guess lower.")
    else:
        print("HINT ! -- Guess higher.")