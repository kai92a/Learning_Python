#Guess my number
#Week 2 Finger Exercise 3
print ("Please think of a number between 0 and 100!")
print ("Is your secret number 50?")
s=[x for x in range (100)]
i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
j=0
k=len(s)
m=50
while i!="c":
    if i!="l":
        if i!="h":
            if i!="c":
                print ("Sorry, I did not understand your input.")
                print ("Is your secret number "+str(s[m])+"?")
                i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if i == "h":
        k=m
        m=int((j+k)/2)
        print ("Is your secret number "+str(s[m])+"?")
        i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if i=="c":
                break
    elif i=="l":
        j=m
        m=int((j+k)/2)
        print ("Is your secret number "+str(s[m])+"?")
        i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if i=="c":
                break
    elif i=="c":
        break
if i=="c":
    print ("Game over. Your secret number was: "+str(s[m]))
