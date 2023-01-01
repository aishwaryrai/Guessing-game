import random
loop = True
score = 0
while loop == True:
    count = 0
    startRange = int(input("Enter the lower bound of the range_"))
    endRange = int(input("Enter the upper bound of the range_"))
    randomNumber = random.randint(startRange, (endRange+1))
    correctAnswer = 0
    while count<3:
        guess = int(input("Enter your guess_"))
        if guess == randomNumber:
            print("Yay! You guessed the number correctly!")
            score+=1
            correctAnswer = 1
        elif guess>=randomNumber:
            print("Your guess was too high! Have one more try :)")
        elif guess<=randomNumber:
            print("Your guess was too small! Have one more try :)")
        count+=1
        if correctAnswer == 1:
            break
    if correctAnswer == 0:
        print("Aww... You lost :(")
    print("Score:", score)
    while True:    
        choice = input("Would you like to play again? Y/N")
        if choice in 'yYYesyes':
            loop = True       
            break
        elif choice in 'nNnoNo':
            print("Thanks for playing! See ya!")
            loop = False
            break
        else:
            print("Invalid choice!")
            loop = False
            break