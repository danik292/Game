#ask for name
import random



name = name = input("What is your name? ")
 #say nice to meet you name
    print("Nice to meet you " + name)
#ask for age
    age = input("How old are you? ")
#if age is more then 18 say you can play the game
    if age is > 18:        print("You can play the game")
    else:
        print("You can't play the game")
    #print plase write a number between 1 and 10 when the nuber is same as my random number you obitain a point
    number = random.randint(1,10)
    print("I am thinking of a number between 1 and 10")
#ask for guess  
    guess = input("Take a guess: ")
#if guess is equal to my random number you obitain a point  
    if int(guess) == number:
        print("You got it right")
    else:
        print("You got it wrong")
#if guess is same than my random number you obitain a point
    if int(guess) == number:
        print("You got it right")
    else:
        print("You got it wrong")